import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load cleaned dataset
df = pd.read_csv("metadata_clean.csv", parse_dates=['publish_time'])
# Setting up Streamlit app
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Filter by publication year

min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select publication year range", 
                       min_value=min_year, max_value=max_year, 
                       value=(2015, max_year))

filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications over time plot
st.subheader("Publications Over Time")
year_counts = filtered_df['year'].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color="skyblue", edgecolor="black")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
ax.set_title("COVID-19 Publications by Year")
st.pyplot(fig)

# Top journals plot
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)

fig, ax = plt.subplots()
top_journals.plot(kind='barh', ax=ax, color="lightgreen", edgecolor="black")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
ax.set_title("Top 10 Journals")
st.pyplot(fig)

# Word Cloud of Abstracts
st.subheader("Word Cloud of Paper Titles")
all_titles = " ".join(filtered_df['title'].dropna().astype(str))
wc = WordCloud(width=800, height=400, background_color="white", max_words=100).generate(all_titles)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Distribution by source plot
st.subheader("Distribution of Papers by Source")
source_counts = filtered_df['source_x'].value_counts()

fig, ax = plt.subplots()
source_counts.plot(kind='bar', ax=ax, color="lightcoral", edgecolor="black")
ax.set_xlabel("Source")
ax.set_ylabel("Number of Papers")
ax.set_title("Paper Distribution by Source")
st.pyplot(fig)
