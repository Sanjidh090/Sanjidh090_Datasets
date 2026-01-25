# Sanjidh Data Explorer - Usage Guide

## Overview

The **Sanjidh Data Explorer** is a specialized interactive tool designed to help researchers, students, and data scientists understand and utilize the datasets in the `sanjidh090_datasets` repository.

## Installation

```bash
# Clone the repository
git clone https://github.com/Sanjidh090/Sanjidh090_Datasets.git
cd Sanjidh090_Datasets

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### 1. View Help Menu

```bash
python data_explorer.py
```

This displays the interactive help menu with all available commands.

### 2. List All Datasets

```bash
python data_explorer.py --list
```

Output:
```
📂 **Available Datasets**

**BUETIAN Rhapsody Dataset** (buetian)
  Social media/community data related to BUET
  Location: BUETIAN-Rhapsody-Dataset
  Key files: Buetian-Rhapsody-Dataset.csv, clean_profile.txt
  Tools: privacy_filter.py, validate_dataset.py, starter_eda.py
...
```

### 3. Understand a Data File

```bash
python data_explorer.py --explain whispers.csv
```

This will:
- Show file type (CSV, JSON, etc.)
- Display column names and data types
- Show preview of the data
- Explain what the data represents

### 4. Get Analysis Suggestions

```bash
python data_explorer.py --suggest kuet
```

Provides tailored analysis suggestions for the KUET Whispers dataset, including:
- Sentiment Analysis (Cross-Lingual)
- Question Detection & Clustering
- Mental Health Indicators
- Temporal Trends
- Text Summarization

### 5. Learn How to Use Scripts

```bash
python data_explorer.py --script privacy_filter.py
```

Shows:
- Script description
- Required dependencies
- Usage examples
- What the script does

### 6. Citation Information

```bash
python data_explorer.py --cite buetian
```

Displays:
- Citation file location
- Ethical guidelines
- License information

## Complete Examples

### Example 1: Working with BUETIAN Rhapsody Dataset

```bash
# 1. Understand the dataset structure
python data_explorer.py --explain Buetian-Rhapsody-Dataset.csv

# 2. Learn about privacy filtering
python data_explorer.py --script privacy_filter.py

# 3. Get analysis ideas
python data_explorer.py --suggest buetian

# 4. Check citation requirements
python data_explorer.py --cite buetian
```

### Example 2: Working with KUET Whispers Dataset

```bash
# 1. List available datasets
python data_explorer.py --list

# 2. Examine the English whispers file
python data_explorer.py --explain whispers_eng.csv

# 3. Get analysis suggestions
python data_explorer.py --suggest kuet

# 4. Check ethical guidelines
python data_explorer.py --cite
```

### Example 3: Working with Google Maps Dataset

```bash
# 1. Understand the JSON structure
python data_explorer.py --explain khulna.json

# 2. Check the reviews CSV
python data_explorer.py --explain reviews.csv

# 3. Get analysis ideas
python data_explorer.py --suggest google_maps
```

## Available Datasets

### 1. BUETIAN Rhapsody Dataset
- **Identifier:** `buetian`
- **Description:** Anonymous student posts from BUET campus
- **Key Files:**
  - `Buetian-Rhapsody-Dataset.csv` - Main dataset
  - `clean_profile.txt` - Cleaned profiles
- **Tools:**
  - `privacy_filter.py` - Redact PII
  - `validate_dataset.py` - Validate integrity
  - `starter_eda.py` - Exploratory analysis

### 2. KUET Whispers Dataset
- **Identifier:** `kuet`
- **Description:** Anonymous confessions from KUET
- **Key Files:**
  - `whispers.csv` - Complete dataset
  - `whispers_Bangla.csv` - Bangla posts only
  - `whispers_eng.csv` - English posts only

### 3. Google Maps Khulna Dataset
- **Identifier:** `google_maps`
- **Description:** Geospatial data and reviews
- **Key Files:**
  - `khulna.json` - Complete data in JSON
  - `reviews.csv` - Reviews only
  - `places_basic.csv` - Place information

## Features

### 1. Data Explanation
The explorer automatically detects file types and provides:
- Column schema for CSVs
- Structure analysis for JSON
- Data previews
- Contextual information

### 2. Script Assistance
Comprehensive guides for running processing scripts:
- Dependencies required
- Installation commands
- Usage examples
- Expected behavior

### 3. Analysis Suggestions
Tailored suggestions based on dataset:
- Specific analysis techniques
- Recommended tools and libraries
- Use case examples

### 4. Citation & Ethics
Reminders about:
- Proper citation practices
- License terms
- Ethical considerations
- Privacy guidelines

## Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `--list` | List all datasets | `python data_explorer.py --list` |
| `--explain FILE` | Explain file structure | `python data_explorer.py --explain whispers.csv` |
| `--script NAME` | Script usage guide | `python data_explorer.py --script privacy_filter.py` |
| `--suggest DATASET` | Analysis suggestions | `python data_explorer.py --suggest kuet` |
| `--cite [DATASET]` | Citation info | `python data_explorer.py --cite buetian` |
| `--help` | Show help menu | `python data_explorer.py --help` |

## Tips

1. **File Names:** You can provide just the filename (e.g., `whispers.csv`) - the explorer will find it in the appropriate dataset directory.

2. **Multiple Commands:** You can run multiple operations:
   ```bash
   python data_explorer.py --list --cite
   ```

3. **Citation:** Always run `--cite` before publishing research using these datasets.

4. **Validation:** Run validation scripts before starting analysis to ensure data integrity.

## Ethical Guidelines

⚠️ **Important Reminders:**

- ✓ Always cite datasets in publications
- ✓ Review LICENSE files before use
- ✓ Do NOT use for surveillance or deanonymization
- ✓ Respect privacy and anonymize outputs
- ✓ Consider cultural context in analysis
- ✓ Treat sensitive content with care

## Support

For issues or questions:
- Check individual dataset README files
- Review CITATION.cff files
- Contact dataset authors (see README files)

## License

Refer to the LICENSE file and dataset-specific licenses in their respective directories.
