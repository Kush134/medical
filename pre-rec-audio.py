from unicodedata import category
import streamlit as st
import requests
import pandas as pd
from get_results import *

upload_file = st.file_uploader('Upload Medical Data Audio')

if upload_file is not None:
    st.audio(upload_file, start_time=0)
    polling_endpoint = upload_to_AssemblyAI(upload_file)

    status='submitted'
    while status != 'completed':
        polling_response = requests.get(polling_endpoint, headers=headers)
        status = polling_response.json()['status']

        if status == 'completed':
            st.subheader('Medical Data')
            with st.expander('Entity'):
                categories = polling_response.json()['iab_categories_result']['summary']
                for cat in categories:
                    st.markdown("*" + cat)



            st.subheader('Breakdown of Medical Data')
            chapters = polling_response.json()['Endities']
            chapter_df = pd.DataFrame(chapters)   
            chapter_df['start_str'] = chapter_df['start'].apply(convertMillis)
            chapter_df['end_str'] = chapter_df['end'].apply(convertMillis)

            for index, row in chapter_df.iterrows():
                with st.write(row['body system']):
                    st.write(row['summary'])
                    st.button(row['start_str'])
