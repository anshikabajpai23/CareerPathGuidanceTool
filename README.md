# CareerPathGuidanceTool
# Job Skill Mapping and Recommender System
Using LinkedIn job data to map technical skills, cluster job roles, mine frequent skill sets, 
and build a personalized skill recommendation tool.

## 🔍 Project Summary
This project analyzes technical skills required in data-related roles using the 
LinkedIn Data Jobs Dataset (Kaggle). It performs:
- Skill extraction and cleaning  
- One-hot encoding of skills  
- K-Means clustering to group similar roles  
- Apriori association rule mining for frequent skill sets  
- Skill recommender system using cluster similarity  
- Job role prediction model based on skills  

## 📁 Repository Structure

## Project Structure
```
job-skill-mapping-recommender/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   └── linkedin_jobs.csv
│   ├── processed/
│   │   └── skills_matrix.csv
│   └── external/  
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_skill_matrix_encoding.ipynb
│   ├── 03_clustering_kmeans.ipynb
│   ├── 04_apriori_association_rules.ipynb
│   ├── 05_skill_recommender.ipynb
│   └── 06_role_prediction_model.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── apriori_mining.py
│   ├── recommender.py
│   └── role_classifier.py
│
├── models/
│   ├── kmeans_model.pkl
│   ├── role_classifier.pkl
│   └── vectorizer.pkl
│
├── visuals/
│   ├── clusters_pca.png
│   ├── apriori_network_graph.png
│   ├── skills_heatmap.png
│   └── recommender_sample.png
│
├── requirements.txt
│
└── LICENSE
```

## Directory Overview

### `/data`
- **raw/**: Contains original, unprocessed data files
  - `linkedin_jobs.csv`: Raw job postings data from LinkedIn
- **processed/**: Cleaned and transformed datasets
  - `skills_matrix.csv`: Binary/encoded matrix of skills by job
- **external/**: Additional external data sources

### `/notebooks`
Jupyter notebooks for exploratory data analysis and model development:
1. `01_data_cleaning.ipynb`: Data preprocessing and cleaning
2. `02_skill_matrix_encoding.ipynb`: Feature engineering and encoding
3. `03_clustering_kmeans.ipynb`: K-means clustering analysis
4. `04_apriori_association_rules.ipynb`: Association rule mining
5. `05_skill_recommender.ipynb`: Skill recommendation system
6. `06_role_prediction_model.ipynb`: Job role prediction model

### `/src`
Python modules containing reusable code:
- `preprocessing.py`: Data cleaning and transformation functions
- `clustering.py`: Clustering algorithms and utilities
- `apriori_mining.py`: Association rule mining implementation
- `recommender.py`: Skill recommendation engine
- `role_classifier.py`: Job role classification model

### `/models`
Trained machine learning models:
- `kmeans_model.pkl`: Serialized K-means clustering model
- `role_classifier.pkl`: Trained role prediction classifier
- `vectorizer.pkl`: Text vectorizer for feature extraction

### `/visuals`
Generated visualizations and figures:
- `clusters_pca.png`: PCA visualization of skill clusters
- `apriori_network_graph.png`: Network graph of skill associations
- `skills_heatmap.png`: Heatmap of skill co-occurrences
- `recommender_sample.png`: Sample output from recommender system

## Getting Started

### Installation
```bash
pip install -r requirements.txt
```

### Usage
Navigate through the notebooks in order for a complete walkthrough of the project pipeline.
