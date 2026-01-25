#!/usr/bin/env python3
import re, sys, pandas as pd

IN_PATH = sys.argv[1] if len(sys.argv) > 1 else 'Buetian-Rhapsody-Dataset.csv'
OUT_PATH = sys.argv[2] if len(sys.argv) > 2 else 'Buetian-Rhapsody-REDacted.csv'

df = pd.read_csv(IN_PATH, encoding='utf-8', engine='python', on_bad_lines='skip')

def redact(text):
    s = str(text)
    # emails
    s = re.sub(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', '[EMAIL]', s)
    # phone numbers (BD patterns, simple)
    s = re.sub(r'(\+?8801|\b01)[0-9-]{8,}\b', '[PHONE]', s)
    # urls
    s = re.sub(r'https?://\S+|www\.\S+', '[URL]', s)
    # social @mentions and IDs
    s = re.sub(r'@\w+', '@[HANDLE]', s)
    return s

df['text'] = df['text'].apply(redact)
df.to_csv(OUT_PATH, index=False, encoding='utf-8')
print(f'Wrote redacted CSV -> {OUT_PATH}')