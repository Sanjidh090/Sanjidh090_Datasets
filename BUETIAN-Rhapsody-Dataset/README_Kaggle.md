# BUETIAN Rhapsody — Anonymous Campus Voices (2023–2025)
**Tagline:** *Echoes of the campus, voices of the unheard.*

**Author:** You (dataset creator)  

**Records:** 977 posts  

**Columns:** 5 (`text`, `likes`, `comments`, `time`, `url`)  

**Timespan:** 2023-02-06 to 2025-09-02 (Asia/Dhaka)  

**Source:** Public posts from the **BUETIAN Rhapsody** page

---

## 1) Context
Student confession and creative pages (like **BUETIAN Rhapsody**) capture authentic campus life: hopes, stress, humor, social issues, and community sentiment. This dataset provides a structured, anonymized corpus for **NLP research**, **social computing**, and **computational social science**. It builds on the author's previous *KUET Whispers* dataset to enable **cross-campus comparisons**.

**Potential research questions**
- What topics dominate student discourse? How do they change over time?
- What features drive engagement (likes/comments)?
- Can we identify toxicity, harassment, or mental-health related signals responsibly?
- Are there stylistic differences between BUET and KUET pages?

---

## 2) What’s inside
- `Buetian-Rhapsody-Dataset.csv` — the main table.

### Schema
{
  "text": "string - the full anonymized post text from BUETIAN Rhapsody",
  "likes": "integer - number of reactions/likes captured at scrape time",
  "comments": "integer - number of comments captured at scrape time",
  "time": "string/datetime - original timestamp as displayed (parseable to ISO)",
  "url": "string - permalink to the original post (public source URL)"
}

**Notes**
- All rows include a `url` to the public source.
- `time` is parseable into a timezone-aware datetime (Asia/Dhaka).
- `likes` and `comments` are counts at the time of collection (not live).

---

## 3) Collection & Quality
- **Collection period:** Feb 2023 – Sep 2025.
- **Method:** Public web scraping of BUETIAN Rhapsody posts; no login, no circumventing access controls.
- **Anonymity:** Posts are anonymous at source; still, please avoid deanonymization attempts.
- **Cleaning:** Minimal normalization (whitespace, stray HTML). No text truncation.

**Known artifacts**
- ~16 duplicated texts (cross-posts or FB re-edits). Consider de-duplication (`text` exact match).
- ~17 very short posts (<10 chars); keep or drop based on task.
- Engagement is heavy-tailed (long-tail likes/comments). Clip or log-transform when modeling.

---

## 4) Licensing & Use
**License (recommended): CC BY-NC 4.0** — free to share/adapt with attribution, **non‑commercial use only**.  
The source platform’s **Terms of Service** also apply. Do **not** use the data to identify individuals or for harassment.

**Attribution example**
> SubsCheap (2025). BUETIAN Rhapsody — Anonymous Campus Voices (2023–2025). Kaggle Dataset.

---

## 5) Ethical Considerations (Read before use)
- **Privacy:** Do not attempt to link posts to real persons; do not publish deanonymized examples.
- **Sensitive content:** Posts may include references to mental health, harassment, or adult themes.
- **Harm mitigation:** If you publish models (e.g., toxicity classifiers), include false‑positive analyses to avoid unfair moderation of benign content.
- **Data removal:** If the page owners request takedown, de‑list or remove mirrors promptly.

---

## 6) Getting Started (Python)
```python
import pandas as pd
df = pd.read_csv('/kaggle/input/buetian-rhapsody/Buetian-Rhapsody-Dataset.csv')
df['time'] = pd.to_datetime(df['time'], errors='coerce')
df['text_len'] = df['text'].astype(str).str.len()

# Simple TF-IDF + Logistic Regression baseline for sentiment/toxicity (requires labels if you add them)
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Suppose you later add a 'label' column (0/1)
# X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42, stratify=df['label'])
# vec = TfidfVectorizer(min_df=3, ngram_range=(1,2), max_features=50000)
# Xtr = vec.fit_transform(X_train); Xte = vec.transform(X_test)
# clf = LogisticRegression(max_iter=200)
# clf.fit(Xtr, y_train)
# print("Test AUC:", roc_auc_score(y_test, clf.predict_proba(Xte)[:,1]))
```

## 7) Suggested Tasks
- **Topic modeling** (LDA/BERTopic) to map campus themes.
- **Engagement prediction**: regress `likes`/`comments` on lexical & temporal features.
- **Temporal analysis**: track topic/sentiment changes across semesters.
- **Toxicity detection**: fine-tune classifiers responsibly (consider class imbalance & fairness).

---

## 8) Versioning & Changelog
- **v1.0 (2025‑09‑02):** Initial release, 977 posts, 5 columns.

---

## 9) Citation
If you use this dataset, please cite:
```
@dataset{buet_rhapsody_2025,
  author    = {SubsCheap},
  title     = {BUETIAN Rhapsody — Anonymous Campus Voices (2023–2025)},
  year      = {2025},
  publisher = {Kaggle},
  url       = {https://kaggle.com/datasets/<your-handle>/buetian-rhapsody}}
```

---

## 10) Acknowledgements
Thanks to the BUET student community and page moderators for maintaining a space that makes this research possible.
