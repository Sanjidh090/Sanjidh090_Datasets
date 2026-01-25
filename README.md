# Sanjidh090_Datasets
Datasets I am author to

## 🤖 Sanjidh Data Explorer

A specialized interactive tool designed to help researchers, students, and data scientists understand and utilize the datasets in this repository.

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Get help
python data_explorer.py --help

# List all datasets
python data_explorer.py --list

# Explain a specific file
python data_explorer.py --explain whispers.csv

# Get analysis suggestions
python data_explorer.py --suggest kuet

# Script usage guidance
python data_explorer.py --script privacy_filter.py

# Citation information
python data_explorer.py --cite buetian
```

### Available Datasets

1. **BUETIAN Rhapsody Dataset** - Social media/community data related to BUET
   - Location: `BUETIAN-Rhapsody-Dataset/`
   - Key files: `Buetian-Rhapsody-Dataset.csv`, `clean_profile.txt`
   - Tools: `privacy_filter.py`, `validate_dataset.py`, `starter_eda.py`

2. **KUET Whispers Dataset** - Anonymous confessions and posts from KUET
   - Location: `KUET-Whispers-Dataset/`
   - Key files: `whispers.csv`, `whispers_Bangla.csv`, `whispers_eng.csv`
   - Notebooks: `exploring-the-whispers.ipynb`

3. **Google Maps Dataset (Khulna)** - Geospatial reviews and place data
   - Location: `Google Maps Dataset : Khulna/`
   - Key files: `khulna.json`, `reviews.csv`, `places_basic.csv`

### Features

- 📊 **Data Explanation**: Inspect CSV/JSON files and understand their structure
- 🔧 **Script Assistance**: Learn how to use processing scripts
- 💡 **Analysis Suggestions**: Get ideas for data analysis based on dataset type
- 📚 **Citation & Ethics**: Important reminders about proper dataset usage
- 🔍 **File Access**: Direct content inspection and schema exploration

### Citation & License

Always review the `LICENSE` file and dataset-specific `CITATION.cff` or README files before using these datasets in publications. Respect ethical guidelines and privacy considerations.

For detailed information about each dataset, navigate to the respective directories and read their README files.
