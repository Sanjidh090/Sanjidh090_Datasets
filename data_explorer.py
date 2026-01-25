#!/usr/bin/env python3
"""
Sanjidh Data Explorer - Interactive Dataset Assistant

A specialized AI agent designed to assist users with the sanjidh090_datasets repository.
Helps researchers, students, and data scientists understand and utilize the datasets provided.
"""

import os
import sys
import json
import argparse
from pathlib import Path
import pandas as pd


class SanjidhDataExplorer:
    """
    The Sanjidh Data Explorer - Your guide to understanding and working with datasets.
    """
    
    def __init__(self, repo_root=None):
        self.repo_root = Path(repo_root) if repo_root else Path(__file__).parent
        self.datasets = {
            'buetian': {
                'name': 'BUETIAN Rhapsody Dataset',
                'path': 'BUETIAN-Rhapsody-Dataset',
                'description': 'Social media/community data related to BUET',
                'key_files': ['Buetian-Rhapsody-Dataset.csv', 'clean_profile.txt'],
                'tools': ['privacy_filter.py', 'validate_dataset.py', 'starter_eda.py'],
                'citation_file': 'CITATION.cff'
            },
            'kuet': {
                'name': 'KUET Whispers Dataset',
                'path': 'KUET-Whispers-Dataset',
                'description': 'Anonymous confessions and posts from KUET',
                'key_files': ['whispers.csv', 'whispers_Bangla.csv', 'whispers_eng.csv'],
                'notebooks': ['exploring-the-whispers.ipynb'],
                'citation_file': 'Readme.md'
            },
            'google_maps': {
                'name': 'Google Maps Dataset (Khulna)',
                'path': 'Google Maps Dataset : Khulna',
                'description': 'Geospatial reviews and place data',
                'key_files': ['khulna.json', 'reviews.csv', 'places_basic.csv'],
                'citation_file': 'Readme.md'
            }
        }
    
    def explain_file(self, file_path):
        """
        Explain the contents and structure of a dataset file.
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            # Try to find the file in dataset directories
            for dataset_key, dataset_info in self.datasets.items():
                potential_path = self.repo_root / dataset_info['path'] / file_path.name
                if potential_path.exists():
                    file_path = potential_path
                    break
        
        if not file_path.exists():
            return f"❌ File not found: {file_path}"
        
        result = [f"\n📊 **File Analysis: {file_path.name}**\n"]
        result.append(f"Full path: {file_path}\n")
        
        # Determine file type and process accordingly
        if file_path.suffix == '.csv':
            return self._explain_csv(file_path, result)
        elif file_path.suffix == '.json':
            return self._explain_json(file_path, result)
        elif file_path.suffix == '.txt':
            return self._explain_txt(file_path, result)
        else:
            result.append(f"File type: {file_path.suffix}")
            result.append(f"Size: {file_path.stat().st_size:,} bytes")
            return '\n'.join(result)
    
    def _explain_csv(self, file_path, result):
        """Explain CSV file structure."""
        try:
            # Read CSV with error handling
            df = pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip', nrows=1000)
            
            result.append(f"**File Type:** CSV (Comma-Separated Values)")
            result.append(f"**Rows:** {len(df):,}")
            result.append(f"**Columns:** {len(df.columns)}\n")
            
            result.append("**Column Information:**")
            for col in df.columns:
                dtype = df[col].dtype
                non_null = df[col].notna().sum()
                null_count = df[col].isna().sum()
                result.append(f"  • {col}: {dtype} ({non_null} non-null, {null_count} null)")
            
            result.append(f"\n**Preview (first 3 rows):**")
            result.append(df.head(3).to_string(index=False))
            
            # Add context based on filename
            context = self._get_file_context(file_path.name)
            if context:
                result.append(f"\n**What this data represents:**\n{context}")
            
        except Exception as e:
            result.append(f"⚠️ Error reading CSV: {e}")
        
        return '\n'.join(result)
    
    def _explain_json(self, file_path, result):
        """Explain JSON file structure."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            result.append(f"**File Type:** JSON (JavaScript Object Notation)")
            
            if isinstance(data, list):
                result.append(f"**Structure:** Array with {len(data)} items")
                if len(data) > 0:
                    result.append(f"**Sample item keys:** {list(data[0].keys())}")
            elif isinstance(data, dict):
                result.append(f"**Structure:** Object with {len(data)} top-level keys")
                result.append(f"**Keys:** {list(data.keys())}")
            
            # Add context
            context = self._get_file_context(file_path.name)
            if context:
                result.append(f"\n**What this data represents:**\n{context}")
            
        except Exception as e:
            result.append(f"⚠️ Error reading JSON: {e}")
        
        return '\n'.join(result)
    
    def _explain_txt(self, file_path, result):
        """Explain TXT file content."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            result.append(f"**File Type:** Text file")
            result.append(f"**Lines:** {len(lines)}")
            result.append(f"\n**Preview (first 10 lines):**")
            result.append(''.join(lines[:10]))
            
        except Exception as e:
            result.append(f"⚠️ Error reading TXT: {e}")
        
        return '\n'.join(result)
    
    def _get_file_context(self, filename):
        """Get contextual information about a file."""
        contexts = {
            'Buetian-Rhapsody-Dataset.csv': 
                'Anonymous student posts from BUET campus, including text content, engagement metrics (likes, comments), timestamps, and URLs.',
            'whispers.csv': 
                'Complete KUET Whispers dataset with post_id, text, date_posted, length, and is_question fields.',
            'whispers_Bangla.csv': 
                'KUET Whispers posts filtered to contain Bangla language content.',
            'whispers_eng.csv': 
                'KUET Whispers posts filtered to contain English language content.',
            'reviews.csv': 
                'Google Maps reviews for locations in Khulna, Bangladesh.',
            'places_basic.csv': 
                'Basic information about places in Khulna from Google Maps.',
            'khulna.json': 
                'Comprehensive geospatial data for Khulna including places, reviews, and metadata in JSON format.',
        }
        return contexts.get(filename, '')
    
    def guide_script_usage(self, script_name):
        """
        Provide guidance on running dataset processing scripts.
        """
        guides = {
            'privacy_filter.py': {
                'description': 'Redacts personally identifiable information (PII) from the dataset',
                'dependencies': ['pandas', 're (built-in)'],
                'usage': [
                    'python privacy_filter.py [input_file] [output_file]',
                    'python privacy_filter.py Buetian-Rhapsody-Dataset.csv redacted.csv',
                    'python privacy_filter.py  # Uses default files'
                ],
                'what_it_does': [
                    '• Redacts email addresses → [EMAIL]',
                    '• Redacts phone numbers → [PHONE]',
                    '• Redacts URLs → [URL]',
                    '• Redacts social media handles → @[HANDLE]'
                ],
                'location': 'BUETIAN-Rhapsody-Dataset/privacy_filter.py'
            },
            'validate_dataset.py': {
                'description': 'Validates the BUETIAN Rhapsody dataset structure and integrity',
                'dependencies': ['pandas', 'python-dateutil'],
                'usage': [
                    'python validate_dataset.py [dataset_file]',
                    'python validate_dataset.py Buetian-Rhapsody-Dataset.csv',
                    'python validate_dataset.py  # Uses default file'
                ],
                'what_it_does': [
                    '• Checks for required columns: text, likes, comments, time, url',
                    '• Validates that likes and comments are >= 0',
                    '• Checks time field parsability (allows ≤1% failures)',
                    '• Reports duplicate text entries'
                ],
                'location': 'BUETIAN-Rhapsody-Dataset/validate_dataset.py'
            },
            'starter_eda.py': {
                'description': 'Performs exploratory data analysis and baseline modeling',
                'dependencies': ['pandas', 'numpy', 'scikit-learn'],
                'usage': [
                    'python starter_eda.py'
                ],
                'what_it_does': [
                    '• Loads and preprocesses the dataset',
                    '• Creates engagement buckets based on likes',
                    '• Builds a baseline TF-IDF + Ridge regression model',
                    '• Predicts post engagement (likes) from text',
                    '• Reports R² and MAE metrics'
                ],
                'location': 'BUETIAN-Rhapsody-Dataset/starter_eda.py'
            }
        }
        
        if script_name not in guides:
            return f"❌ Unknown script: {script_name}\nAvailable scripts: {', '.join(guides.keys())}"
        
        guide = guides[script_name]
        
        output = [f"\n📜 **Script Guide: {script_name}**\n"]
        output.append(f"**Description:** {guide['description']}\n")
        output.append(f"**Location:** {guide['location']}\n")
        
        output.append("**Required Dependencies:**")
        for dep in guide['dependencies']:
            output.append(f"  • {dep}")
        
        output.append("\n**Installation:**")
        output.append(f"  pip install pandas python-dateutil scikit-learn numpy")
        
        output.append("\n**Usage Examples:**")
        for usage in guide['usage']:
            output.append(f"  {usage}")
        
        output.append("\n**What it does:**")
        for item in guide['what_it_does']:
            output.append(f"  {item}")
        
        return '\n'.join(output)
    
    def suggest_analysis(self, dataset_name):
        """
        Suggest analysis approaches for a specific dataset.
        """
        suggestions = {
            'buetian': {
                'dataset': 'BUETIAN Rhapsody',
                'analyses': [
                    {
                        'name': 'Topic Modeling',
                        'description': 'Discover recurring themes in student posts using LDA or BERTopic',
                        'tools': ['gensim', 'BERTopic', 'sklearn']
                    },
                    {
                        'name': 'Sentiment Analysis',
                        'description': 'Analyze emotional tone and affect in campus discourse',
                        'tools': ['VADER', 'TextBlob', 'transformers (BERT-based models)']
                    },
                    {
                        'name': 'Engagement Prediction',
                        'description': 'Predict post popularity based on content (see starter_eda.py)',
                        'tools': ['scikit-learn', 'XGBoost', 'neural networks']
                    },
                    {
                        'name': 'Time Series Analysis',
                        'description': 'Track posting patterns and topic evolution over time',
                        'tools': ['pandas', 'matplotlib', 'seaborn']
                    },
                    {
                        'name': 'Code-Mixing Analysis',
                        'description': 'Study English-Bangla language mixing patterns',
                        'tools': ['polyglot', 'langdetect', 'custom NLP models']
                    }
                ]
            },
            'kuet': {
                'dataset': 'KUET Whispers',
                'analyses': [
                    {
                        'name': 'Sentiment Analysis (Cross-Lingual)',
                        'description': 'Compare sentiment between English and Bangla whispers',
                        'tools': ['transformers', 'BanglaBERT', 'mBERT']
                    },
                    {
                        'name': 'Question Detection & Clustering',
                        'description': 'Analyze the is_question field and cluster common concerns',
                        'tools': ['sklearn', 'DBSCAN', 'Topic Modeling']
                    },
                    {
                        'name': 'Mental Health Indicators',
                        'description': 'Identify patterns related to stress, anxiety, or wellbeing',
                        'tools': ['Custom lexicons', 'supervised ML', 'LIWC']
                    },
                    {
                        'name': 'Temporal Trends',
                        'description': 'Track sentiment shifts around exam periods or semester breaks',
                        'tools': ['pandas', 'time series visualization']
                    },
                    {
                        'name': 'Text Summarization',
                        'description': 'Automatically summarize long confessions',
                        'tools': ['transformers (BART, T5)', 'extractive summarization']
                    }
                ]
            },
            'google_maps': {
                'dataset': 'Google Maps Khulna',
                'analyses': [
                    {
                        'name': 'Geospatial Visualization',
                        'description': 'Map places and reviews across Khulna',
                        'tools': ['folium', 'geopandas', 'plotly']
                    },
                    {
                        'name': 'Review Sentiment Analysis',
                        'description': 'Analyze review sentiment and rating correlations',
                        'tools': ['VADER', 'TextBlob', 'correlation analysis']
                    },
                    {
                        'name': 'Place Categorization',
                        'description': 'Cluster places by type, reviews, and ratings',
                        'tools': ['sklearn', 'K-means', 'hierarchical clustering']
                    },
                    {
                        'name': 'Rating Distribution Analysis',
                        'description': 'Study rating patterns across different place types',
                        'tools': ['pandas', 'matplotlib', 'statistical tests']
                    },
                    {
                        'name': 'Recommendation System',
                        'description': 'Build a place recommendation engine based on reviews',
                        'tools': ['collaborative filtering', 'content-based filtering']
                    }
                ]
            }
        }
        
        if dataset_name not in suggestions:
            return f"❌ Unknown dataset: {dataset_name}\nAvailable: {', '.join(suggestions.keys())}"
        
        info = suggestions[dataset_name]
        output = [f"\n💡 **Analysis Suggestions for {info['dataset']}**\n"]
        
        for i, analysis in enumerate(info['analyses'], 1):
            output.append(f"{i}. **{analysis['name']}**")
            output.append(f"   {analysis['description']}")
            output.append(f"   Suggested tools: {', '.join(analysis['tools'])}\n")
        
        return '\n'.join(output)
    
    def citation_reminder(self, dataset_name=None):
        """
        Provide citation and ethical use information.
        """
        output = ["\n📚 **Citation & Ethics Guidelines**\n"]
        
        if dataset_name:
            citation_files = {
                'buetian': 'BUETIAN-Rhapsody-Dataset/CITATION.cff',
                'kuet': 'KUET-Whispers-Dataset/Readme.md (Citation section)',
                'google_maps': 'Google Maps Dataset : Khulna/Readme.md'
            }
            
            if dataset_name in citation_files:
                output.append(f"**For {self.datasets[dataset_name]['name']}:**")
                output.append(f"📄 See: {citation_files[dataset_name]}\n")
        
        output.append("**General Guidelines:**\n")
        output.append("✓ **Always cite the dataset** when publishing research")
        output.append("✓ Review the LICENSE file for usage terms")
        output.append("✓ Check dataset-specific CITATION.cff or README files")
        output.append("✓ **Do NOT** use for surveillance, deanonymization, or punitive profiling")
        output.append("✓ Treat sensitive content with confidentiality and respect")
        output.append("✓ Anonymize outputs in publications")
        output.append("✓ Consider cultural context and nuance in analysis\n")
        
        output.append("**License Information:**")
        output.append("  • BUETIAN Rhapsody: CC BY-NC 4.0 (recommended)")
        output.append("  • KUET Whispers: Academic/Research use only")
        output.append("  • See individual README files for specific terms")
        
        return '\n'.join(output)
    
    def list_datasets(self):
        """List all available datasets."""
        output = ["\n📂 **Available Datasets**\n"]
        
        for key, info in self.datasets.items():
            output.append(f"**{info['name']}** ({key})")
            output.append(f"  {info['description']}")
            output.append(f"  Location: {info['path']}")
            output.append(f"  Key files: {', '.join(info['key_files'])}")
            if 'tools' in info:
                output.append(f"  Tools: {', '.join(info['tools'])}")
            output.append("")
        
        return '\n'.join(output)
    
    def interactive_help(self):
        """Display interactive help menu."""
        help_text = """
╔════════════════════════════════════════════════════════════════╗
║          Sanjidh Data Explorer - Interactive Guide             ║
╚════════════════════════════════════════════════════════════════╝

🎯 **Purpose:**
Help researchers, students, and data scientists understand and utilize
the datasets in the sanjidh090_datasets repository.

📋 **Available Commands:**

  --list                  List all available datasets
  --explain FILE          Explain structure and content of a data file
  --script SCRIPT_NAME    Get usage guide for a processing script
  --suggest DATASET       Get analysis suggestions for a dataset
  --cite [DATASET]        Show citation and ethics information
  --help                  Show this help message

📊 **Dataset Identifiers:**
  • buetian      - BUETIAN Rhapsody Dataset
  • kuet         - KUET Whispers Dataset
  • google_maps  - Google Maps Khulna Dataset

🔧 **Available Scripts:**
  • privacy_filter.py   - Redact PII from datasets
  • validate_dataset.py - Validate dataset integrity
  • starter_eda.py      - Exploratory data analysis

💡 **Example Usage:**

  python data_explorer.py --list
  python data_explorer.py --explain whispers.csv
  python data_explorer.py --script privacy_filter.py
  python data_explorer.py --suggest kuet
  python data_explorer.py --cite buetian

📚 **Quick Start:**
  1. Explore datasets: --list
  2. Understand a file: --explain <filename>
  3. Get analysis ideas: --suggest <dataset>
  4. Check citation: --cite

⚠️ **Remember:**
  • Always cite datasets in publications
  • Respect privacy and ethical guidelines
  • Review LICENSE before commercial use
"""
        return help_text


def main():
    parser = argparse.ArgumentParser(
        description='Sanjidh Data Explorer - Your guide to the sanjidh090_datasets repository',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--list', action='store_true',
                       help='List all available datasets')
    parser.add_argument('--explain', metavar='FILE',
                       help='Explain the structure and content of a data file')
    parser.add_argument('--script', metavar='SCRIPT_NAME',
                       help='Get usage guide for a processing script')
    parser.add_argument('--suggest', metavar='DATASET',
                       help='Get analysis suggestions for a dataset (buetian/kuet/google_maps)')
    parser.add_argument('--cite', metavar='DATASET', nargs='?', const='all',
                       help='Show citation and ethics information')
    
    args = parser.parse_args()
    
    explorer = SanjidhDataExplorer()
    
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        print(explorer.interactive_help())
        return
    
    # Process commands
    if args.list:
        print(explorer.list_datasets())
    
    if args.explain:
        print(explorer.explain_file(args.explain))
    
    if args.script:
        print(explorer.guide_script_usage(args.script))
    
    if args.suggest:
        print(explorer.suggest_analysis(args.suggest))
    
    if args.cite:
        dataset = None if args.cite == 'all' else args.cite
        print(explorer.citation_reminder(dataset))


if __name__ == '__main__':
    main()
