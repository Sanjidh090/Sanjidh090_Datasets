# 🗣️ Lipi-Ghor | লিপিঘর — Bengali Speech Dataset (bn-882-SSTT)

[![Language](https://img.shields.io/badge/Language-Bengali%20(bn)-green)](https://huggingface.co/datasets/Sanjidh090/Lipi-Ghor-bn-882-SSTT)
[![Hours](https://img.shields.io/badge/Audio-882%20hrs-blue)](https://huggingface.co/datasets/Sanjidh090/Lipi-Ghor-bn-882-SSTT)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)
[![DL Sprint](https://img.shields.io/badge/DL%20Sprint-4.0-orange)](https://github.com/Sanjidx090)

**Lipi-Ghor** (লিপিঘর, meaning *"House of Scripts"*) is a large-scale Bengali speech dataset designed for automatic speech recognition (ASR), speaker diarization, and spoken language research. It is one of the largest open Bengali speech corpora with aligned speaker, transcription, and timestamp annotations.

Built by **Team_Villagers** as part of **DL Sprint 4.0**.

---

## Dataset Details

### Dataset Description

Lipi-Ghor is a large-scale, multi-domain Bengali speech corpus covering ~882 hours of audio sourced from 1,019 YouTube videos across 596 unique channels. Each video has been processed through speaker diarization (pyannote-audio) and aligned with Bengali caption transcripts to produce structured SSTT (Speaker, Speech, Transcription, Timestamp) annotations. The dataset covers a wide range of spoken Bengali domains, registers, and regional dialects, making it one of the most diverse open Bengali speech resources available.

- **Curated by:** Team_Villagers — Sanjid Hasan, A H M Fuad, Risalat Labib, Bayazid Hasan
- **Competition:** DL Sprint 4.0
- **Language(s):** Bengali / Bangla (`bn`)
- **License:** CC BY 4.0

### Dataset Sources

- **Repository:** [Sanjidh090/Lipi-Ghor-bn-882-SSTT](https://huggingface.co/datasets/Sanjidh090/Lipi-Ghor-bn-882-SSTT)
- **Source data:** YouTube (public videos with Bengali caption tracks)

---

## Dataset at a Glance

| Field                   | Value                                      |
|-------------------------|--------------------------------------------|
| **Total hours sourced** | ~882 hours                                 |
| **Fully annotated**     | ~856 hours (diarization + transcription)   |
| **Pending upload**      | ~194 hours (~321 videos)                   |
| **Total videos**        | 1,019                                      |
| **Unique channels**     | 596                                        |
| **Language**            | Bengali / Bangla (`bn`)                    |
| **Annotation format**   | SSTT — Speaker, Speech, Transcription, Timestamp |
| **Audio format**        | MP3 (pyannote-segmented)                   |
| **Diarization**         | pyannote-audio (SOTA)                      |
| **License**             | CC BY 4.0                                  |

---

## Uses

### Direct Use

This dataset is intended for:

- **Bengali ASR model training** — fine-tuning Whisper, wav2vec2, MMS, and similar models
- **Speaker diarization research** — "who spoke when" tasks in Bengali
- **Bengali TTS** — speaker-labeled segments can inform voice synthesis pipelines
- **Dialect identification** — the dataset covers Standard Dhaka Bengali, Chittagonian, Sylheti, Rangpuri, and Barishal variants
- **Multilingual NLP benchmarking** — Bengali is consistently under-represented in multilingual benchmarks

### Out-of-Scope Use

- **Surveillance or speaker re-identification** — speaker labels (`SPEAKER_00`, `SPEAKER_01`, etc.) are local to each video and do not track identity across videos
- **High-stakes production ASR without filtering** — the majority of transcripts are sourced from auto-generated YouTube captions and may contain recognition errors; human verification is recommended before deployment in critical applications

---

## Dataset Structure

```
Lipi-Ghor-bn-882-SSTT/
├── data/                                    # Audio segments (.wav, pyannote-segmented)
├── diarization_results/                     # Per-video diarization output (*_output.json)
├── diarization_results_with_transcription/  # Diarization + transcript aligned (*_unified.json)
├── diarization_transcription_final/         # Cleaned final outputs (*_unified.json)
└── test/                                    # Test samples (.wav)
```

### File Naming Convention

All annotation files use the YouTube **video ID** as the base filename:
- `{video_id}_output.json` — raw diarization output
- `{video_id}_unified.json` — diarization + transcription merged

### Annotation Format (SSTT)

Each `_unified.json` contains an array of segments:

```json
[
  {
    "speaker": "SPEAKER_00",
    "start": 12.34,
    "end": 18.72,
    "text": "আমরা আজকে এই বিষয়টি নিয়ে কথা বলব।"
  }
]
```

| Field     | Type   | Description                         |
|-----------|--------|-------------------------------------|
| `speaker` | string | Speaker label from diarization      |
| `start`   | float  | Segment start time (seconds)        |
| `end`     | float  | Segment end time (seconds)          |
| `text`    | string | Bengali transcript for this segment |

---

## Content & Categories

| Category              | Videos | Hours  |
|-----------------------|--------|--------|
| Talk-show             | 357    | 240.0  |
| Audio-book            | 248    | 218.3  |
| Movie                 | 31     | 67.3   |
| Podcast               | 37     | 45.4   |
| Cartoon               | 56     | 36.3   |
| Audiobook (variant)   | 17     | 28.7   |
| Natok (drama)         | 21     | 21.4   |
| Bangla Cinema         | 14     | 20.0   |
| Drama                 | 20     | 19.9   |
| Kirton                | 14     | 16.4   |
| Waz / Islamic Sermon  | 20     | 16.2   |
| Kolkata Bangla Movie  | 8      | 16.0   |
| + 150 more categories | ...    | ...    |

Dialectal coverage includes: Standard Dhaka Bengali, Chittagonian, Sylheti, Rangpuri, and Barishal variants.

---

## Top Channels by Hours

| Channel                        | Videos | Hours  |
|--------------------------------|--------|--------|
| My AudioBook                   | 229    | 202.4  |
| Roy Parrett                    | 132    | 113.7  |
| BanglaVision NEWS              | 144    | 97.3   |
| Abhijit Story Zone             | 92     | 89.9   |
| Audio Book Bangla by Faheem    | 71     | 87.0   |
| ATN Bangla Talk Show           | 105    | 86.6   |
| GTV News                       | 70     | 73.9   |
| Eso Galpo Shuni                | 81     | 63.9   |
| Golpo Toru                     | 63     | 48.9   |
| AudioKothon with RAJIA         | 52     | 47.2   |

---

## Dataset Creation

### Curation Rationale

Bengali is spoken by over 230 million people yet remains severely under-resourced in ASR and spoken language research. Existing open Bengali ASR datasets are typically small (5–40 hours), limited to read speech, and lack speaker annotations. Lipi-Ghor was created to address this gap with a large-scale, multi-domain, diarized corpus that reflects the diversity of real spoken Bengali across dialects, topics, and recording conditions.

### Source Data

#### Data Collection and Processing

1. **Video Selection** — YouTube video IDs were collected across 596 Bengali channels covering diverse domains. Only videos with existing Bengali caption tracks (manual or community-contributed) were retained to ensure baseline transcription quality.
2. **Audio & Transcript Extraction** — [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) was used to download audio (MP3) and pull Bengali caption/subtitle tracks (`bn` language code).
3. **Speaker Diarization** — [`pyannote-audio`](https://github.com/pyannote/pyannote-audio) was applied to each audio file to segment speech into speaker turns with precise timestamps. Outputs stored as `*_output.json`.
4. **Alignment** — YouTube transcripts were aligned with pyannote speaker segments to produce SSTT-format `*_unified.json` files. A cleaned final version is stored in `diarization_transcription_final/`.

#### Who are the Source Data Producers?

The source audio and transcripts are derived from publicly available YouTube content created by Bengali-language content creators across Bangladesh and West Bengal. Content spans professional news channels, independent creators, audiobook narrators, and community contributors.

### Annotations

#### Annotation Process

Speaker diarization was performed automatically using pyannote-audio. Transcription was sourced from existing YouTube caption tracks — 86 videos have manually created captions; the remaining 1,254 use auto-generated YouTube captions. Alignment between diarization segments and caption timestamps was performed programmatically.

#### Who are the Annotators?

Diarization: pyannote-audio (automated). Transcription: YouTube caption system and original content creators. Post-processing and pipeline: Team_Villagers (Sanjid Hasan, A H M Fuad, Risalat Labib, Bayazid Hasan).

#### Personal and Sensitive Information

The dataset contains publicly broadcast speech from YouTube. Speaker labels are anonymous (`SPEAKER_00`, etc.) and are not linked to real-world identities. No cross-video speaker identity tracking is performed. Content creators retain their original copyright; this dataset is intended for research and non-commercial use only.

> If you are a content creator and wish to have your content removed from this dataset, please open an issue or contact us directly.

---

## Bias, Risks, and Limitations

- **Transcript quality varies** — 86 videos have human-verified captions; 1,254 use auto-generated YouTube captions which may contain recognition errors, especially for dialectal speech and code-switching.
- **Audio quality varies** — sourced from diverse YouTube content; some recordings contain background music, overlapping speakers, or artifacts.
- **~194 hours pending** — approximately 321 videos are sourced and diarized but not yet fully uploaded to this repository.
- **Speaker labels are local** — `SPEAKER_00`, `SPEAKER_01` etc. are per-video labels only. Cross-video speaker identity is not tracked.
- **Code-switching** — some content contains Bengali-English mixing, which reflects real usage but may affect monolingual ASR models.
- **Geographic bias** — the majority of content originates from Dhaka-centric media channels; rural and minority dialects may be underrepresented relative to their speaker populations.

### Recommendations

Users training ASR models should consider filtering by transcript type (`manual` vs `auto`) and evaluating on a held-out human-verified subset before deployment. For dialect-robust training, stratified sampling across the category and channel distribution is recommended.

---

## Citation

If you use Lipi-Ghor in your research, please cite:

**BibTeX:**

```bibtex
@dataset{lipighor2025,
  title     = {Lipi-Ghor: A Large-Scale Bengali Speech Dataset with Speaker Diarization and Transcription},
  author    = {Hasan, Sanjid and Fuad, A H M and Labib, Risalat and Hasan, Bayazid},
  year      = {2026},
  publisher = {HuggingFace},
  DOI       = {https://doi.org/10.57967/hf/7877}
  url       = {https://huggingface.co/datasets/Sanjidh090/Lipi-Ghor-bn-882-SSTT},
  note      = {DL Sprint 4.0, Team\_Villagers}
}
```

**APA:**

Hasan, S., Fuad, A. H. M., Labib, R., & Hasan, B. (2025). *Lipi-Ghor: A Large-Scale Bengali Speech Dataset with Speaker Diarization and Transcription* [Dataset]. HuggingFace. https://huggingface.co/datasets/Sanjidh090/Lipi-Ghor-bn-882-SSTT

---

## Glossary

| Term | Definition |
|------|-----------|
| **SSTT** | Speaker, Speech, Transcription, Timestamp — the annotation schema used in this dataset |
| **Diarization** | The process of segmenting audio by speaker ("who spoke when") |
| **pyannote-audio** | State-of-the-art open-source speaker diarization library |
| **yt-dlp** | Open-source tool for downloading YouTube audio and subtitles |
| **bn** | ISO 639-1 language code for Bengali/Bangla |

---

## Dataset Card Authors

**Team_Villagers** — DL Sprint 4.0

- Sanjid Hasan
- A H M Fuad
- Risalat Labib
- Bayazid Hasan

## Dataset Card Contact

Open an issue on the HuggingFace repository or contact via the repository discussion tab.

---

## Acknowledgements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for audio and caption extraction
- [pyannote-audio](https://github.com/pyannote/pyannote-audio) for speaker diarization
- All Bengali content creators whose work made this dataset possible
- DL Sprint 4.0 organizers

---

*লিপিঘর — বাংলা ভাষার জন্য, বাংলা ভাষার গবেষকদের জন্য।*
*Lipi-Ghor — for the Bengali language, for Bengali language researchers.*
