# Import required libraries

import streamlit as st
import pandas as pd

# Configure Streamlit page
st.set_page_config(
    page_title="IMDb Movie Dashboard",
    page_icon="🎬",
    layout="wide"
)

# Dashboard title
st.title("🎬 IMDb Top 250 Movies Dashboard")

# Read movie data from CSV file
df = pd.read_csv("movie_data.csv")

# Create metrics section
col1, col2 = st.columns(2)

# Total number of movies
with col1:
    st.metric(
        "Total Movies",
        len(df)
    )

# Display top ranked movie
with col2:
    st.metric(
        "Top Ranked Movie",
        df.iloc[0]["Movie"]
    )

# Search box for movie filtering
search = st.text_input(
    "🔍 Search Movie"
)

# Filter data based on search input
if search:
    filtered_df = df[
        df["Movie"].str.contains(
            search,
            case=False,
            na=False
        )
    ]
else:
    filtered_df = df

# Display movie table
st.subheader("🎥 Movie List")

st.dataframe(
    filtered_df,
    width="stretch"
)

# Top 10 movies section
st.subheader("⭐ Top 10 Movies")

top10 = df.head(10)

st.table(top10)

# Download CSV button
csv = df.to_csv(index=False)

st.download_button(
    label="⬇ Download CSV",
    data=csv,
    file_name="movie_data.csv",
    mime="text/csv"
)