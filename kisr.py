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

    if choice == 'validation':
        
        def highlight_greater(df):
            r = 'tomato'
            df1 = pd.DataFrame(' ', index=df.index, columns=df.columns)
        
            diff1=df["The total value of the company's investments in 2020"]-df["The total value of the company's investments in 2019"]
            b1= diff1 < -2 
            b2= diff1 > 2
            b4= diff1 == 3
            df1["The total value of the company's investments in 2019"]= np.where(b1, 'background-color: {}'.format(r), df1["The total value of the company's investments in 2019"])
            df["The total value of the company's investments in 2019"]=np.where(b4, df["The total value of the company's investments in 2019"]+1 , df["The total value of the company's investments in 2019"])
            df1["The total value of the company's investments in 2019"]= np.where(b2, 'background-color: {}'.format(r), df1["The total value of the company's investments in 2019"])
    
    
    
           
    
            
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
