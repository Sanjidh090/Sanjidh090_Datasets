#!/usr/bin/env python3
import sys, pandas as pd
from dateutil import parser

path = sys.argv[1] if len(sys.argv) > 1 else 'Buetian-Rhapsody-Dataset.csv'
df = pd.read_csv(path, encoding='utf-8', engine='python', on_bad_lines='skip')

required = ['text','likes','comments','time','url']
missing = [c for c in required if c not in df.columns]
assert not missing, f'Missing required columns: {missing}'

# Types/constraints
assert (df['likes']>=0).all(), 'likes must be >= 0'
assert (df['comments']>=0).all(), 'comments must be >= 0'

# Time parsable check (allow NaT <= 1% rows)
parsed = pd.to_datetime(df['time'], errors='coerce')
fail_rate = parsed.isna().mean()
assert fail_rate <= 0.01, f'Time parse failures too high: {fail_rate:.2%}'

# Duplicate text report (warn only)
dups = df.duplicated(subset=['text']).sum()
print(f'OK. Rows={len(df)}, duplicate_text_rows={dups}, time_parse_fail_rate={fail_rate:.2%}')
