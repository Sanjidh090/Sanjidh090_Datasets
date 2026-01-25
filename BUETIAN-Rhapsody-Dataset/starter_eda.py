# Starter EDA and Baselines for BUETIAN Rhapsody
import pandas as pd
import numpy as np

# Path for Kaggle: replace with the actual input path after upload
CSV_PATH = 'Buetian-Rhapsody-Dataset.csv'

df = pd.read_csv(CSV_PATH)
df['time'] = pd.to_datetime(df['time'], errors='coerce')
df['text'] = df['text'].astype(str).str.strip()
df['text_len'] = df['text'].str.len()

print('Rows:', len(df))
print(df.head())

# Simple engagement buckets
df['eng_bucket'] = pd.qcut(df['likes'].rank(method='first'), q=4, labels=['low','mid','high','viral'])

# Baseline text regression for likes (no labels needed)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

mask = df['likes'].notna()
X_train, X_test, y_train, y_test = train_test_split(df.loc[mask,'text'], df.loc[mask,'likes'], test_size=0.2, random_state=42)

vec = TfidfVectorizer(min_df=3, ngram_range=(1,2), max_features=50000)
Xtr = vec.fit_transform(X_train); Xte = vec.transform(X_test)

model = Ridge(alpha=1.0)
model.fit(Xtr, y_train)
pred = model.predict(Xte)

print('Baseline Likes Regression')
print('R^2:', round(r2_score(y_test, pred), 4))
print('MAE:', round(mean_absolute_error(y_test, pred), 2))
