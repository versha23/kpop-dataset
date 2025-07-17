
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="K-pop Comeback Dashboard", layout="wide")

# Load data
df = pd.read_csv("kpop_comeback_day_by_day.csv")

st.title("🎵 K-pop Comeback Dashboard")
st.markdown("Analyze daily YouTube views and Spotify streams of 50+ simulated JYP artist comebacks.")

# Sidebar filters
artists = st.sidebar.multiselect("Select Artist(s)", options=df["Artist"].unique(), default=df["Artist"].unique())
countries = st.sidebar.multiselect("Select Country/Countries", options=df["Country"].unique(), default=df["Country"].unique())

# Filtered data
filtered_df = df[df["Artist"].isin(artists) & df["Country"].isin(countries)]

# Line chart - Day-by-Day YouTube Views
st.subheader("📈 Daily YouTube Views by Artist")
line_fig = px.line(filtered_df, x="Day", y="YouTube Views", color="Artist", markers=True,
                   title="YouTube Views Over 7 Days", template="plotly_white")
st.plotly_chart(line_fig, use_container_width=True)

# Line chart - Day-by-Day Spotify Streams
st.subheader("📈 Daily Spotify Streams by Artist")
stream_fig = px.line(filtered_df, x="Day", y="Spotify Streams", color="Artist", markers=True,
                     title="Spotify Streams Over 7 Days", template="plotly_white")
st.plotly_chart(stream_fig, use_container_width=True)

# Bar chart - Total Streams per Artist
st.subheader("🎤 Total Streams per Artist")
total_streams = filtered_df.groupby("Artist")[["YouTube Views", "Spotify Streams"]].sum().reset_index()
bar_fig = px.bar(total_streams, x="Artist", y=["YouTube Views", "Spotify Streams"],
                 barmode="group", title="Total Views & Streams per Artist", template="plotly_white")
st.plotly_chart(bar_fig, use_container_width=True)

# Pie chart - Country Distribution
st.subheader("🌍 Fanbase Distribution by Country (YouTube Views)")
country_dist = filtered_df.groupby("Country")["YouTube Views"].sum().reset_index()
pie_fig = px.pie(country_dist, names="Country", values="YouTube Views", title="YouTube Views by Country")
st.plotly_chart(pie_fig, use_container_width=True)
