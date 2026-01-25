# Dataset Card: BUETIAN Rhapsody (2023–2025)

## Motivation
Anonymous student posts offer a lens into campus culture, wellbeing, and public discourse. The dataset supports research in NLP, social computing, and HCI with a focus on South Asian academic contexts.

## Composition
- **Instances:** 977 posts
- **Fields:** text, likes, comments, time, url
- **Language:** Primarily English and Bangla (code‑mixed).
- **Sensitive content:** Possible; use content warnings in publications.

## Collection
- **Method:** Public scraping of posts visible without login, between 2023‑02‑06 and 2025‑09‑02 (Asia/Dhaka).
- **Sampling:** Near‑exhaustive for the page within the window.
- **Preprocessing:** Minimal cleanup; no paraphrasing; no translation.

## Uses
- Topic modeling, sentiment/affect, toxicity moderation research, engagement modeling, trend analysis.
- **Not for** surveillance, deanonymization, or punitive profiling.

## Distribution
- **License:** CC BY‑NC 4.0 (recommended)
- **Access:** Kaggle download. Mirrors must preserve license and this card.

## Risks & Limitations
- Cultural nuance and sarcasm can confound classifiers.
- Engagement counts are snapshots, not live totals.
- Contains duplicates (≈16) and very short posts (≈17).

## Maintenance
- **Owner:** Sanjidh090
- **Contact:** <sanjidh090/sanjid9657@gmail.com>
- **Update plan:** Optional quarterly refreshes. Submit issues or removal requests via Kaggle discussion.
