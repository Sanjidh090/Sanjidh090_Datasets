"""
Lipi-Ghor BN-882 ASR Dataset Chunker
======================================
For researchers & engineers using the Lipi-Ghor-bn-882-SSTT dataset
for large-scale Bengali ASR training.

This script:
  1. Reads chunking manifests from  asr_train_ready/  on HuggingFace
  2. Downloads the corresponding MP3 audio files from the same repo
  3. Cuts each MP3 into 16 kHz mono WAV chunks using the JSON timestamps
  4. Writes a metadata.csv (compatible with HuggingFace datasets / ESPnet / NeMo)

Output structure:
  <OUTPUT_DIR>/
  ├── wavs/
  │   ├── 007T9XKT_sE_0001_2512_20034.wav
  │   ├── 007T9XKT_sE_0002_20600_38210.wav
  │   └── ...
  └── metadata.csv   ← columns: file_name, duration, text, video_id, chunk_id

Requirements:
  pip install huggingface_hub pydub tqdm
  apt-get install ffmpeg   (or brew install ffmpeg on mac)

Usage:
  python lipi_ghor_chunker.py

  # Process only specific videos:
  python lipi_ghor_chunker.py --videos VIDEO_ID1 VIDEO_ID2

  # Limit total hours collected:
  python lipi_ghor_chunker.py --max_hours 50
"""

import argparse
import json
import os
import csv
import shutil
from pathlib import Path

from huggingface_hub import hf_hub_download, list_repo_files
from pydub import AudioSegment
from tqdm import tqdm

# ══════════════════════════════════════════════════════
#  CONFIGURATION  —  edit these if needed
# ══════════════════════════════════════════════════════
REPO_ID         = "Sanjidh090/Lipi-Ghor-bn-882-SSTT"
ASR_JSON_DIR    = "asr_train_ready"       # folder with *_asr.json files
AUDIO_DIR       = "audio"                 # folder with *.mp3 files in the repo
                                          # (change if the repo uses a different name)
OUTPUT_DIR      = "lipi_ghor_asr_chunks"  # where wavs + metadata.csv will be saved
SAMPLE_RATE     = 16000                   # Hz  — standard for ASR
CHANNELS        = 1                       # mono
HF_TOKEN        = None                    # set to your token if repo is private
# ══════════════════════════════════════════════════════


def get_manifest_paths(video_filter: list = None) -> list:
    """List all *_asr.json paths in asr_train_ready/ on HF."""
    print("🔍  Scanning HuggingFace repo for ASR manifests …")
    all_files = list(list_repo_files(REPO_ID, repo_type="dataset", token=HF_TOKEN))
    paths = [
        f for f in all_files
        if f.startswith(ASR_JSON_DIR + "/") and f.endswith("_asr.json")
    ]
    if video_filter:
        paths = [p for p in paths if any(v in p for v in video_filter)]
    print(f"   ✅  Found {len(paths)} manifests.\n")
    return paths


def download_json(remote_path: str) -> dict:
    local = hf_hub_download(
        repo_id=REPO_ID,
        filename=remote_path,
        repo_type="dataset",
        token=HF_TOKEN,
    )
    with open(local, "r", encoding="utf-8") as f:
        return json.load(f)


def find_audio_path(video_id: str, all_files: list) -> str | None:
    """
    Looks for an audio file matching the video_id in the repo.
    Tries common extensions: mp3, wav, m4a, opus.
    """
    for ext in ["mp3", "wav", "m4a", "opus"]:
        candidate = f"{AUDIO_DIR}/{video_id}.{ext}"
        if candidate in all_files:
            return candidate
    # fallback: loose match anywhere in the repo
    for f in all_files:
        name = os.path.basename(f)
        if name.startswith(video_id) and any(
            name.endswith(e) for e in [".mp3", ".wav", ".m4a", ".opus"]
        ):
            return f
    return None


def load_audio(remote_path: str) -> AudioSegment:
    local = hf_hub_download(
        repo_id=REPO_ID,
        filename=remote_path,
        repo_type="dataset",
        token=HF_TOKEN,
    )
    ext = Path(local).suffix.lstrip(".")
    audio = AudioSegment.from_file(local, format=ext)
    # Normalise to 16 kHz mono immediately
    audio = audio.set_frame_rate(SAMPLE_RATE).set_channels(CHANNELS)
    return audio


def ms(seconds: float) -> int:
    return int(seconds * 1000)


def chunk_and_save(
    audio: AudioSegment,
    segments: list,
    video_id: str,
    wav_dir: Path,
    metadata_rows: list,
    total_sec_collected: float,
    max_sec: float,
) -> float:
    """
    Cuts audio into chunks using segment timestamps.
    Returns seconds added in this call.
    """
    added = 0.0
    for seg in segments:
        if max_sec and (total_sec_collected + added) >= max_sec:
            break

        start_ms = ms(seg["start"])
        end_ms   = ms(seg["end"])
        text     = seg["text"].strip()

        if not text or end_ms <= start_ms:
            continue

        chunk = audio[start_ms : end_ms + 50]   # +50ms tail buffer

        # filename: videoId_chunkId_startMs_endMs.wav
        fname = f"{video_id}_{seg['id']:04d}_{start_ms}_{end_ms}.wav"
        wav_path = wav_dir / fname
        chunk.export(str(wav_path), format="wav")

        duration = (end_ms - start_ms) / 1000.0
        added   += duration

        metadata_rows.append({
            "file_name": f"wavs/{fname}",
            "duration":  round(duration, 3),
            "text":      text,
            "video_id":  video_id,
            "chunk_id":  seg["id"],
        })

    return added


def write_metadata(rows: list, out_dir: Path):
    csv_path = out_dir / "metadata.csv"
    fieldnames = ["file_name", "duration", "text", "video_id", "chunk_id"]
    mode = "a" if csv_path.exists() else "w"
    with open(csv_path, mode, newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if mode == "w":
            writer.writeheader()
        writer.writerows(rows)


def already_done(out_dir: Path) -> set:
    """Returns video_ids already in metadata.csv so we can skip them."""
    csv_path = out_dir / "metadata.csv"
    if not csv_path.exists():
        return set()
    done = set()
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            done.add(row["video_id"])
    return done


def current_hours(out_dir: Path) -> float:
    csv_path = out_dir / "metadata.csv"
    if not csv_path.exists():
        return 0.0
    total = 0.0
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                total += float(row["duration"])
            except Exception:
                pass
    return total / 3600.0


# ─────────────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────────────
def main(video_filter=None, max_hours=None):
    out_dir  = Path(OUTPUT_DIR)
    wav_dir  = out_dir / "wavs"
    wav_dir.mkdir(parents=True, exist_ok=True)

    max_sec = max_hours * 3600 if max_hours else None

    # ── All repo files (for audio lookup) ────────────────────────
    print("🔍  Fetching full repo file list …")
    all_repo_files = set(list_repo_files(REPO_ID, repo_type="dataset", token=HF_TOKEN))

    # ── Manifests ─────────────────────────────────────────────────
    manifest_paths = get_manifest_paths(video_filter)

    # ── Resume support ────────────────────────────────────────────
    done_ids = already_done(out_dir)
    if done_ids:
        print(f"⏭️   Skipping {len(done_ids)} already-chunked videos.\n")
    manifest_paths = [p for p in manifest_paths
                      if os.path.basename(p).replace("_asr.json","") not in done_ids]

    collected_hours = current_hours(out_dir)
    print(f"📊  Already collected : {collected_hours:.2f} hours")
    if max_hours:
        print(f"🎯  Target            : {max_hours} hours")
    print(f"📋  Manifests to process: {len(manifest_paths)}\n")
    print("=" * 60)

    stats = {"videos": 0, "chunks": 0, "no_audio": 0, "errors": 0}
    total_sec = collected_hours * 3600

    for manifest_path in tqdm(manifest_paths, unit="video"):
        if max_sec and total_sec >= max_sec:
            print(f"\n🎉  Reached {max_hours}h target — stopping.")
            break

        video_id = os.path.basename(manifest_path).replace("_asr.json", "")

        # ── Load manifest ─────────────────────────────────────────
        try:
            manifest = download_json(manifest_path)
        except Exception as e:
            tqdm.write(f"⚠️  [{video_id}] Failed to load manifest: {e}")
            stats["errors"] += 1
            continue

        segments = manifest.get("segments", [])
        if not segments:
            tqdm.write(f"⚠️  [{video_id}] No segments in manifest — skipping.")
            continue

        # ── Find + load audio ─────────────────────────────────────
        audio_path = find_audio_path(video_id, all_repo_files)
        if not audio_path:
            tqdm.write(f"❌  [{video_id}] No audio file found in repo — skipping.")
            stats["no_audio"] += 1
            continue

        try:
            audio = load_audio(audio_path)
        except Exception as e:
            tqdm.write(f"⚠️  [{video_id}] Audio load error: {e}")
            stats["errors"] += 1
            continue

        # ── Chunk ─────────────────────────────────────────────────
        metadata_rows = []
        try:
            added = chunk_and_save(
                audio, segments, video_id,
                wav_dir, metadata_rows,
                total_sec, max_sec,
            )
        except Exception as e:
            tqdm.write(f"⚠️  [{video_id}] Chunking error: {e}")
            stats["errors"] += 1
            continue

        if not metadata_rows:
            continue

        # ── Append to metadata.csv immediately (crash-safe) ───────
        write_metadata(metadata_rows, out_dir)

        total_sec       += added
        stats["videos"] += 1
        stats["chunks"] += len(metadata_rows)

        tqdm.write(
            f"✅  {video_id} — {len(metadata_rows)} chunks | "
            f"{added:.1f}s | total {total_sec/3600:.2f}h"
        )

    # ── Summary ───────────────────────────────────────────────────
    print(
        f"\n🎉  Done!\n"
        f"   Videos processed : {stats['videos']}\n"
        f"   Total chunks     : {stats['chunks']}\n"
        f"   Total audio      : {total_sec/3600:.2f} hours\n"
        f"   No audio found   : {stats['no_audio']}\n"
        f"   Errors           : {stats['errors']}\n"
        f"   Output directory : {OUTPUT_DIR}/\n"
        f"   Metadata CSV     : {OUTPUT_DIR}/metadata.csv\n"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Chunk Lipi-Ghor BN-882 dataset for ASR training"
    )
    parser.add_argument(
        "--videos", nargs="+", default=None,
        help="Optional: process only these video IDs"
    )
    parser.add_argument(
        "--max_hours", type=float, default=None,
        help="Optional: stop after collecting this many hours"
    )
    args = parser.parse_args()
    main(video_filter=args.videos, max_hours=args.max_hours)
