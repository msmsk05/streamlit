

import streamlit as st
import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as plt




html_temp = """
<div style="background-color:white;padding:10px">
<h1 style="color:black;text-align:center;"><b> ML Models Performance Dashboard </b></h1>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)



html_temp = """
<div style="background-color:red;padding:10px">
<h2 style="color:white;text-align:center;">Metrics </h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

  
@st.cache(allow_output_mutation=True)
def get_table():
  bigquery_client = bigquery.Client()

  QUERY = """
  SELECT * FROM `coo-risk-ews-237113.ews.topic_model_feedback `
   """
  Query_Results = bigquery_client.query(QUERY)
  df = Query_Results.to_dataframe()
  #View top few rows of result
  TP=df[(df.model_threshold==True) & (df.feedback==True)].feedback.count()
  FP=df[(df.model_threshold==True) & (df.feedback==False)].feedback.count()
  FN=df[(df.model_threshold==False) & (df.feedback==True)].feedback.count()
  TN=df[(df.model_threshold==False) & (df.feedback==False)].drop_duplicates(subset=['article_id', 'topic_model']).feedback.count()
  accuracy=(TN+TP)/(TP+TN+FP+FN)
  precision=TP/(TP+FP)
  recall=TP/(TP+FN)
  return df, accuracy, precision, recall
  
     
def write():
    """ Writes content to the app """
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox('', ("Choose a metric",'All Metrics', "Accuracy", 'Precision', "Recall"))

    st.write('You selected:', page)
    st.title("Get Data from BigQuery")

    
    if page == 'All Metrics':
        st.success(get_table[0]).
        st.info('Accuracy score is:')
        st.success(get_table[1])
        st.info('Precision score is:')
        st.success(get_table[2])
        st.info('Recall score is:')
        st.success(get_table[3])
        
    if page=='Accuracy':
        st.info('Accuracy score is:')
        st.success(get_table[1])
        
    if page== 'Precision':
        st.info('Precision score is:')
        st.success(get_table[2])
        
    if page == 'Recall':
        st.info('Recall score is:')
        st.success(get_table[3])
      

      
if __name__ == "__main__":
    write()   
 


  




 
