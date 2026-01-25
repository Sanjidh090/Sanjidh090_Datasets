# Khulna Places: Multimodal Google Maps Dataset 🇧🇩

This dataset contains structured and raw information about places and businesses
in Khulna, Bangladesh, collected from Google Maps.  
It is designed to support exploratory data analysis, machine learning, NLP,
computer vision, and multimodal research.

---

## 📂 Dataset Contents

The dataset includes **five files**, each serving a different purpose:

### 1. `khulna.json`
Raw, unprocessed Google Maps place data.
Includes full nested information such as images, reviews, opening hours,
geolocation, and additional metadata.  
Recommended for advanced users who want complete data fidelity.

---

### 2. `khulna_all_in_one.csv`
A flattened, single-table version of the dataset where each row represents
one place.  
Complex fields (images, reviews, opening hours, attributes) are stored as
JSON-formatted strings.

---

### 3. `places_core.csv`
Clean, place-level structured data containing:
- Place name and category
- Description (when available)
- Address and city
- Latitude and longitude
- Ratings and review counts
- Business metadata

Suitable for EDA, ML modeling, and geospatial analysis.

---

### 4. `place_images.csv`
Image metadata associated with places, including:
- Image URLs
- Author names
- Upload timestamps

This file enables multimodal learning and computer vision experiments.
Note: Only image URLs are provided; images are not hosted in this dataset.

---

### 5. `reviews.csv`
User-generated reviews linked to places, containing:
- Star ratings
- Review text
- Language
- Publication timestamps

Useful for NLP tasks such as sentiment analysis and opinion mining.

---

## 🔍 Key Features

- Multi-category urban place data
- Geolocation (latitude & longitude)
- Ratings and popularity metrics
- User reviews for NLP
- Image URLs for multimodal research
- Real-world, imperfect data for practical ML work

---

## 🧠 Possible Use Cases

- Exploratory data analysis (EDA)
- Business category classification
- Sentiment analysis on reviews
- Multimodal learning (text + image)
- Geospatial analysis and mapping
- Recommendation systems
- Weakly supervised learning

---

## ⚠️ Notes

- Some fields may contain missing values, reflecting real-world data.
- Image descriptions are not provided; users may generate captions using
computer vision models.
- JSON-like columns in CSV files can be parsed back into Python objects if needed.

---

## 📜 Disclaimer

This dataset is shared strictly for educational and research purposes.
All data originates from publicly accessible sources.

---

## 🙌 Acknowledgement

If you use this dataset in a project or publication, please consider
crediting the dataset source.

