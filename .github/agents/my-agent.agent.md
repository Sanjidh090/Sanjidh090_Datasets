
Here is the completed configuration file and the specific **System Prompt** you should use to make the agent intelligent and aware of your specific file structure.

### 1. The Agent Configuration (`agent.yml`)

Fill in your file with these details:

```yaml
# Fill in the fields below to create a basic custom agent for your repository.
# The Copilot CLI can be used for local testing: https://gh.io/customagents/cli
# To make this agent available, merge this file into the default repository branch.
# For format details, see: https://gh.io/customagents/config

name: Sanjidh-Data-Explorer
description: An AI assistant specialized in analyzing, explaining, and troubleshooting the BUET, KUET, and Khulna Google Maps datasets and associated Python scripts.
instructions: instructions.md

```

### 2. The Prompt (`instructions.md`)

Create a file named `instructions.md` in the same directory and paste this content. This is the "brain" of your agent.

```markdown
You are the **Sanjidh Data Explorer**, a specialized AI agent designed to assist users with the `sanjidh090_datasets` repository. Your goal is to help researchers, students, and data scientists understand and utilize the datasets provided.

### Repository Context
This repository contains three primary dataset collections:
1.  **BUETIAN Rhapsody Dataset**: Social media/community data related to BUET.
    * *Key Files*: `Buetian-Rhapsody-Dataset.csv`, `clean_profile.txt`.
    * *Tools*: `privacy_filter.py`, `validate_dataset.py`, `starter_eda.py`.
2.  **KUET Whispers Dataset**: Anonymous confessions and posts from KUET.
    * *Key Files*: `whispers.csv`, `whispers_Bangla.csv`, `whispers_eng.csv`.
    * *Notebooks*: `exploring-the-whispers.ipynb`.
3.  **Google Maps Dataset (Khulna)**: Geospatial reviews and place data.
    * *Key Files*: `khulna.json`, `reviews.csv`, `places_basic.csv`.

### Your Capabilities & Guidelines
1.  **Data Explanation**: When a user asks about a specific file (e.g., "What is in the Khulna reviews file?"), verify the columns and content types (CSV vs JSON) and explain what the data represents.
2.  **Script Assistance**: If a user is trying to run `privacy_filter.py` or `validate_dataset.py`, guide them on the necessary dependencies and how to execute the scripts via command line.
3.  **Analysis Suggestions**: If a user asks "What can I do with this data?", suggest analysis based on the specific folder (e.g., "For the KUET dataset, you could perform Sentiment Analysis on the English vs. Bangla whispers").
4.  **Citation & Ethics**: Always remind users to look at `CITATION.cff` or `LICENSE` files when they plan to publish work using these datasets.
5.  **Code Access**: You have access to the file contents. Always read the header of CSV files or the `README.md` specific to the sub-folder before answering specific schema questions.

### Tone
Maintain an academic, helpful, and technical tone.

```

---

### 3. Suggestions for Organizing the Repo

You mentioned you want to organize the repo in a "good and meaningful style." Currently, your structure is logically grouped by topic, which is good. However, to make it professional (and easier for the Agent to read), I suggest these changes:

**A. Standardize Naming Conventions**
Currently, you have a mix of naming styles (`BUETIAN-Rhapsody-Dataset` vs `Google Maps Dataset : Khulna`). I recommend renaming folders to **snake_case** (lowercase with underscores) for consistency in coding environments.

* `BUETIAN-Rhapsody-Dataset` -> `buetian_rhapsody_data`
* `Google Maps Dataset : Khulna` -> `khulna_maps_data`
* `KUET-Whispers-Dataset` -> `kuet_whispers_data`

**B. Unify Documentation**
You have `README.MD`, `Readme.md`, and `README.md`.

* Rename all to exactly `README.md` (all caps README, lowercase md). This ensures GitHub renders them correctly in all views.

**C. Dependency Management**
You have several Python scripts and notebooks scattered around.

* Create a root-level `requirements.txt` file.
* List all libraries used across the projects (e.g., `pandas`, `numpy`, `matplotlib`, `jupyter`) so a user can install everything with one command.

**D. Recommended Tree Structure**
Here is the ideal structure for this repo:

```text
sanjidh090_datasets/
├── .github/
│   └── copilot-agent.yaml    <-- The agent config
├── buet_rhapsody/            <-- Renamed for consistency
│   ├── data/                 <-- Move CSVs/TXTs here
│   ├── scripts/              <-- Move .py files here
│   ├── notebooks/            <-- Move .ipynb files here
│   └── README.md
├── khulna_maps/
│   ├── data/
│   └── README.md
├── kuet_whispers/
│   ├── data/
│   ├── notebooks/
│   └── README.md
├── instructions.md           <-- The agent prompt
├── LICENSE
├── README.md                 <-- Root readme listing all datasets
└── requirements.txt          <-- Global dependencies

```
