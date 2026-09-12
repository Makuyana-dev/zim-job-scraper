import streamlit as st
import pandas as pd

st.set_page_config(page_title="ZIM JOB SCRAPER", layout="wide")

st.title("🇿🇼 ZIM JOB SCRAPER")
st.markdown("**100+ Latest Jobs in Zimbabwe. Updated Daily.**")

@st.cache_data
def load_data():
    df = pd.read_csv("jobs.csv", encoding="utf-8")
    return df

df = load_data()

# FILTERS
col1, col2, col3 = st.columns(3)
with col1:
    search = st.text_input("🔍 Search Job Title, Company")
with col2:
    cities = ["All"] + sorted(df['Location'].dropna().unique().tolist())
    location = st.selectbox("📍 Filter by City", cities)
with col3:
    job_types = ["All"] + sorted(df['Title'].dropna().unique().tolist())[:20]
    job_type = st.selectbox("💼 Filter by Job", job_types)

# FILTER DATA
filtered_df = df.copy()
if search:
    filtered_df = filtered_df[filtered_df.apply(lambda row: search.lower() in str(row).lower(), axis=1)]
if location != "All":
    filtered_df = filtered_df[filtered_df['Location'] == location]
if job_type != "All":
    filtered_df = filtered_df[filtered_df['Title'] == job_type]

st.write(f"**Showing {len(filtered_df)} Jobs**")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.markdown("💰 **PREMIUM: $3/month for WhatsApp Job Alerts**")
st.markdown("Send EcoCash to 078 580 5135")
st.markdown("Then WhatsApp `JOIN` to get jobs daily")
