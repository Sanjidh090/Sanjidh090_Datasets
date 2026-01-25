# KUET Whispers Dataset

**Author**: Sanjid Hasan   
**Institution**: Khulna University of Engineering & Technology (KUET)   
**Dataset Type**: Text (Facebook posts)   
**License**: For research and academic use only.

---

## 📌 Overview

The **KUET Whispers Dataset** contains anonymized Facebook posts from the "KUET Whispers" page, a platform used by students at KUET to share opinions, confessions, experiences, and discussions. This dataset aims to provide insights into the social, academic, and emotional dynamics of students in a university environment. To download:
https://www.kaggle.com/datasets/sanjidh090/kuet-whispers

---

## 📂 File Description

### `whispers.csv`

| Column Name   | Description                                             |
| ------------- | ------------------------------------------------------- |
| `post_id`     | Unique identifier for each post                         |
| `text`        | The main content of the post (confession or message)    |
| `date_posted` | Date when the post was published                        |
| `length`      | Character length of the post                            |
| `is_question` | Boolean indicating whether the post contains a question |

---

## 🔍 Potential Use Cases

* **Natural Language Processing (NLP)**

  * Sentiment Analysis
  * Emotion Classification
  * Text Summarization
* **Social Analysis**

  * Topic Modeling (LDA, BERTopic)
  * Gender/Identity Expression in Anonymous Speech
  * Mental Health Trends among University Students
* **Time Series Exploration**

  * Trends in post frequency
  * Term evolution over semesters/years

---

## 🛠 How to Use

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('whispers.csv')

# Preview the dataset
print(df.head())
```

---

## 💡 Example Projects

* Visualizing most common keywords and bigrams
* Identifying frequently asked questions
* Clustering student concerns (academic vs personal)
* Temporal sentiment shifts around exam periods

---

## ⚠️ Ethical Considerations

This dataset contains potentially sensitive and emotionally charged content. Researchers should treat it with confidentiality and respect, especially when publishing findings. Always anonymize outputs and never attempt to deanonymize posts or users.

---

## 📬 Citation

If you use this dataset in your work, please cite:

```
Sanjid Hasan. (2025). KUET_whispers_Dataset [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DS/7822294
```

