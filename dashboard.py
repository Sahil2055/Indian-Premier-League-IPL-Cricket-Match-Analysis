# --- Import necessary libraries ---

import streamlit as st
import pandas as pd
import plotly.express as px # Plotly is great for interactive charts



# --- Page Configuration ---

# 'st.set_page_config' should be the first Streamlit command in your script.
st.set_page_config(
    page_title="IPL Dashboard",
    page_icon="🏏",
    layout="wide" # Use the full page width
)


# --- Load Data ---

# We use a caching decorator to load data only once, which improves performance.
@st.cache_data
def load_data():
    matches_df = pd.read_csv('sample_datasets/matches_cleaned.csv')
    deliveries_df = pd.read_csv('sample_datasets/deliveries.csv')
    return matches_df, deliveries_df

matches_df, deliveries_df = load_data()


# --- Dashboard Title ---

st.title("🏏 Indian Premier League (IPL) Analysis")
st.markdown("This dashboard presents an in-depth analysis of IPL matches from 2008 to 2024.")


# --- Sidebar Filters ---

st.sidebar.header("Filter Options")
selected_season = st.sidebar.selectbox("Select a Season", options=sorted(matches_df['season'].unique(), reverse=True))

# Filter data based on the selected season
season_df = matches_df[matches_df['season'] == selected_season]





# --- Main Page Content ---

# --- Row 1: Key Metrics ---
st.header(f"Season Overview: {selected_season}")

# Get the list of match IDs for the selected season
season_match_ids = season_df['id'].unique()

# Calculate metrics for the selected season
total_matches = len(season_df)
toss_decisions = season_df['toss_decision'].value_counts()

# Filter deliveries data for the selected season's matches and sum the total runs
total_runs = deliveries_df[deliveries_df['match_id'].isin(season_match_ids)]['total_runs'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Matches", f"{total_matches}")
col2.metric("Teams Chose to Bat", f"{toss_decisions.get('bat', 0)}")
col3.metric("Teams Chose to Field", f"{toss_decisions.get('field', 0)}")


# --- Row 2: Visualizations ---
st.header("Visual Analysis")

# Visualization 1: Toss Decision Impact for the Season
fig_toss = px.pie(
    season_df,
    names='toss_decision',
    title=f'Toss Decisions in {selected_season}',
    hole=0.4
)
st.plotly_chart(fig_toss, use_container_width=True)

# Visualization 2: Top 5 Run Scorers of All Time
st.header("All-Time Player Rankings")
top_n = st.slider("Select Number of Top Players", 5, 20, 10) # Interactive slider

batsman_runs = deliveries_df.groupby('batter')['batsman_runs'].sum().nlargest(top_n)
fig_top_scorers = px.bar(
    x=batsman_runs.index,
    y=batsman_runs.values,
    title=f'Top {top_n} Run Scorers in IPL History',
    labels={'x': 'Batsman', 'y': 'Total Runs'},
    color=batsman_runs.index
)
st.plotly_chart(fig_top_scorers, use_container_width=True)