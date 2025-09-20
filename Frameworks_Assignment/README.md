# 📊 CORD-19 Research Data Explorer

This project is part of Assignment 8, focusing on analyzing [the CORD-19 research dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
and building a Streamlit app to explore insights from COVID-19 related research papers.

## 📌 Project Overview

The project walks through the end-to-end data science workflow:

1. Data Cleaning & Preparation (handling missing values, creating derived columns).

2. Data Analysis & Visualization (publication trends, top journals, word frequency, source distribution).

3. Streamlit Application (interactive web app for exploring results).

## 🛠️ Tools & Libraries

Python 3.7+

- pandas → data manipulation

- matplotlib → visualizations

- wordcloud → word cloud generation

- streamlit → interactive web app

- collection  → the counter to tally hashable objects 

- nltk → for importing stopwords

## 🚀 Installation & Usage

Follow these steps to set up the project on your local machine:

## 1. Clone the Repository

First, clone this repository from GitHub to your local computer:

`git clone https://github.com/Mmainajames/Python-Assignments-at-PLP/Frameworks_Assignment.git
cd Frameworks_Assignmwnt`

## 2. Create a Virtual Environment (Recommended)

It’s best to use a virtual environment so dependencies don’t conflict with your system Python.

### On Windows:

`python -m venv venv
venv\Scripts\activate`


### On Mac/Linux:

`python3 -m venv venv
source venv/bin/activate`

## 3. Install Dependencies

Install all required Python libraries using requirements.txt:

`pip install -r requirements.txt`

## 4. Download the Dataset

This project uses the CORD-19 metadata.csv dataset.

Download it from Kaggle: [CORD-19 Research Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)


Place `metadata.csv` in the root folder of this project.

Alternatively, use the cleaned version (`metadata_clean.csv`) provided in the repo.

## 5. Run the Jupyter Notebook (Optional)

To explore the analysis step by step in Jupyter Notebook:

`jupyter notebook`


Open the notebook inside your browser and run the cells to see the analysis & visualizations.

## 6. Run the Streamlit App

To launch the interactive web app:

`streamlit run app.py`

This will open the app in your browser at:

`http://localhost:8501`

Inside the app, you can:

1. Select a year range

2. View publication trends

3. See top journals

4. Generate a word cloud of titles

5. Explore paper counts by source

6. Preview a sample of the dataset

## 7. Deactivate Virtual Environment (when done)

When you’re finished, deactivate your virtual environment:

`deactivate`


✅ That’s it! You now have the full analysis + interactive Streamlit dashboard running on your machine.

## 📂 Dataset

We used the *metadata.csv* file from the CORD-19 dataset.

Key columns used in analysis:

- title → research paper titles

- abstract → abstracts of papers

- publish_time → publication dates

- journal → journal names

- source_x → data source (e.g., PMC, bioRxiv)

- cord_uid → unique identifier


For data integrity and completeness other columns included the dataset are:
- doi/url → only needed if you want to link back to the papers
- license→ not critical for analysis, but good for metadata context.
- authors → could be used for “most prolific authors” if you want to extend analysis.

## 🔧 Data Cleaning

1. Handled missing values

- Filled missing text fields with placeholders (e.g., "No Title", "Unknown", "No Abstract Available").

- Dropped rows with invalid or missing publish_time.

2. Created derived columns

- year → extracted from publish_time.

- abstract_word_count → number of words in each abstract.

3. Filtered dataset

- Kept only publications from 2015 onward.

## 📊 Analysis & Visualizations

1. Publications Over Time → trend of research output by year.

2. Top Journals → journals with the highest number of COVID-19 papers.

3. Word Frequency in Titles → most common words in research titles.

4. Word Cloud → visual representation of frequent terms in titles.

5. Source Distribution → number of papers by source.

## 🌐 Streamlit Application

An interactive web app was developed with Streamlit:

- Filter by publication year range.

- Explore publication trends.

- View top journals.

- Generate a word cloud of paper titles.

- Visualize paper distribution by source.

- Preview a sample of the dataset.

### Run the app locally:
` streamlit run app.py `

## 📸 Example Outputs

📈 Line chart of publications by year
<img width="989" height="490" alt="line graph" src="https://github.com/user-attachments/assets/c63407ba-af19-405e-83bf-c26e05dbf51b" />

🏛️ Top 20 journals
<img width="1189" height="590" alt="top journals" src="https://github.com/user-attachments/assets/5057e190-38f2-48f1-abe0-87bab8db11ae" />


☁️ Word cloud of research titles

<img width="944" height="504" alt="word cloud" src="https://github.com/user-attachments/assets/4e521916-e451-4c3b-9fce-02cf2cebaf55" />

📊 Source distribution (bar & pie charts)

<img width="989" height="590" alt="distribution by source" src="https://github.com/user-attachments/assets/dcc0f956-121e-42b3-9473-d7d81d3549a7" />

## 📌 Project Structure
├── app.py                # Streamlit app
├── metadata_clean.csv    # Cleaned dataset
├── pubs_by_year.csv      # Aggregated publication counts
├── README.md             # Project documentation
└── notebooks/            # (Optional) Jupyter notebooks for analysis

✨ Key Learnings

- How to clean and preprocess real-world research metadata.

- Techniques for text analysis (word frequency, word clouds).

- Building interactive dashboards with Streamlit.

- Importance of filtering out irrelevant data for clearer insights.

📬 Author

Assignment completed by MAINA M JAMES as part of the PLP Software Engineering Program.


