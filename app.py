import pandas as pd
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="ZIM JOB SCRAPER", page_icon="🇿🇼")
st.title("🇿🇼 ZIM JOB SCRAPER")

df = pd.read_csv('jobs.csv')

search = st.text_input("🔍 Search Job Title")
location = st.text_input("📍 Filter by Location e.g. Harare")

if search:
    df = df[df['Title'].str.contains(search, case=False, na=False)]
if location:
    df = df[df['Location'].str.contains(location, case=False, na=False)]

st.success(f"Found {len(df)} jobs")

df['Link'] = df['Link'].apply(lambda x: f'<a href="{x}" target="_blank">Apply Here</a>')
st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 🚀 PREMIUM: $3/month for WhatsApp Job Alerts")
st.markdown("**Send EcoCash to 0785 805 135**")
st.markdown("Then WhatsApp 'JOIN' to get jobs daily")