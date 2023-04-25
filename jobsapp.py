import streamlit as st
import pandas as pd
import numpy as np


def search_jobs():
    # Get user input for keywords
    junior = st.checkbox("Filter by junior jobs?")
    senior = st.checkbox("Filter by senior jobs?")
    remote = st.checkbox("Filter by remote jobs?")
    contract = st.checkbox("Filter by contract jobs?")
    
    # Load the job DataFrame
    df_jobs = pd.read_csv('streamlit.csv')
    
    # Filter the DataFrame based on the input keywords
    if contract:
        df_jobs = df_jobs[df_jobs['status1'] == 'Contract']
    if remote:
        df_jobs = df_jobs[df_jobs['remote'] == 'yes']
    if junior:
        df_jobs = df_jobs[df_jobs['title'].str.lower().str.contains("junior|graduate|apprentice|entry level")]
    if senior:
        df_jobs = df_jobs[df_jobs['title'].str.lower().str.contains("senior|lead|head|vp")]
    
    # format salary and link
    df_jobs['annual_salary(£)'] = df_jobs['annual_salary'].fillna('negotiable').apply(lambda x: '{:.0f}'.format(x) if isinstance(x, float) else x)
    df_jobs['link'] = df_jobs['link'].apply(lambda x:f'<a href="{x}" target="_blank">link</a>')
    df_jobs = df_jobs.reset_index(drop=True)
    df_jobs = df_jobs.rename(columns={'status1': 'job type'})
    df_jobs = df_jobs.rename(columns={'link': 'link to posting'})

    
    # Return the filtered jobs
    st.write(f"{len(df_jobs)} job(s) found.")
    st.write(df_jobs[['title', 'region', 'job type', 'remote','annual_salary(£)', 'link to posting']].to_html(escape=False), unsafe_allow_html=True)

st.title("Data Jobs Search!")
search_jobs()
