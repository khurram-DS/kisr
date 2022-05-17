import streamlit as st
# Eda packages

import pandas as pd
import numpy as np

#Data viz packages

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

#function

def main():
    
    activites = ["validation"]
    choice =st.sidebar.selectbox("Select Activity",activites)
    
    @st.cache(allow_output_mutation=True)
    def get_df(file):
      # get extension and read file
      extension = file.name.split('.')[1]
      if extension.upper() == 'CSV':
        df = pd.read_csv(file)
      elif extension.upper() == 'XLSX':
        df = pd.read_excel(file)
      
      return df
    file = st.file_uploader("Upload file", type=['csv' 
                                             ,'xlsx'])
    if not file:
        st.write("Upload a .csv or .xlsx file to get started")
        return
      
    df = get_df(file)
    st.write("**Data has been loaded Successfully**")
    if st.checkbox('Show Raw Data'):
        st.subheader('Raw Data')
        st.write(df)
    if choice == 'validation':
        def highlight_greater(df):
            r = 'tomato'
            
        
            first_number=df['The total Kuwaiti workers 2019']
            second_number=df['The total Kuwaiti workers 2020']
            percent_diff = ((second_number - first_number)/first_number) * 100
            a1= percent_diff <= -70 
            a2= percent_diff >= 70
            
            first_number=df['The total Kuwaiti workers 2020']
            second_number=df['Total Kuwaiti employment 2021']
            percent_diff = ((second_number - first_number)/first_number) * 100
            a11= percent_diff <= -70 
            a21= percent_diff >= 70
         # non
            first_number=df['Total non- Kuwaiti employment 2019']
            second_number=df['Total non Kuwaiti employment 2020']
            percent_diff = ((second_number - first_number)/first_number) * 100
            b1= percent_diff <= -70 
            b2= percent_diff >= 70
            
            first_number=df['Total non Kuwaiti employment 2020']
            second_number=df['The total non -Kuwaiti employment 2021']
            percent_diff = ((second_number - first_number)/first_number) * 100
            b11= percent_diff <= -70 
            b21= percent_diff >= 70
        
        
        
        
        
        
        
            df1 = pd.DataFrame(' ', index=df.index, columns=df.columns)
            
            df1['The total Kuwaiti workers 2020'] = np.where(a1, 'background-color: {}'.format(r), df1['The total Kuwaiti workers 2020'])
            df1['The total Kuwaiti workers 2020'] = np.where(a2, 'background-color: {}'.format(r), df1['The total Kuwaiti workers 2020'])
            
            df1['Total Kuwaiti employment 2021'] = np.where(a11, 'background-color: {}'.format(r), df1['Total Kuwaiti employment 2021'])
            df1['Total Kuwaiti employment 2021'] = np.where(a21, 'background-color: {}'.format(r), df1['Total Kuwaiti employment 2021'])
            
            
            df1['Total non Kuwaiti employment 2020'] = np.where(a1, 'background-color: {}'.format(r), df1['Total non Kuwaiti employment 2020'])
            df1['Total non Kuwaiti employment 2020'] = np.where(a2, 'background-color: {}'.format(r), df1['Total non Kuwaiti employment 2020'])
            
            df1['The total non -Kuwaiti employment 2021'] = np.where(a11, 'background-color: {}'.format(r), df1['The total non -Kuwaiti employment 2021'])
            df1['The total non -Kuwaiti employment 2021'] = np.where(a21, 'background-color: {}'.format(r), df1['The total non -Kuwaiti employment 2021'])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            return df1
        da=df.style.apply(highlight_greater, axis =None)
        st.dataframe(da)
        
    
        
        import base64
        import io
        towrite = io.BytesIO()
        downloaded_file = da.to_excel(towrite, encoding='utf-8', index=False, header=True) # write to BytesIO buffer
        towrite.seek(0)  # reset pointer
        b64 = base64.b64encode(towrite.read()).decode() 
        linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="validation_result.xlsx">Download excel file</a>'
        st.markdown(linko, unsafe_allow_html=True)
            




if __name__=='__main__':
    main()
