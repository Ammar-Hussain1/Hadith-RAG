import pandas as pd
import os

df = pd.read_csv('../data/raw/all_hadiths_clean.csv')

df['source'] = df['source'].str.strip()
df['chapter'] = df['chapter'].str.strip()

df = df.dropna(subset=['text_en', 'text_ar'])
df = df[df['text_en'].str.strip() != ""]
df = df[df['text_ar'].str.strip() != ""]

cleaned_data = []

for _, row in df.iterrows():
    reference = f"{row['source']}, Chapter {row['chapter_no']}, Hadith {row['hadith_no']}"
    cleaned_data.append({
        "reference": reference,
        "book": row['source'].strip(),
        "chapter": row['chapter'].strip(),
        "text_en": row['text_en'].strip(),
        "text_ar": row['text_ar'].strip(),
        "hadith_no": row['hadith_no'],
        "chapter_no": row['chapter_no']
    })

# Ensure output folder exists
import json

OUTPUT_PATH = '../data/processed/cleaned_hadiths.json'
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Save JSON
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

print(f"Saved {len(cleaned_data)} cleaned hadiths to {OUTPUT_PATH}")