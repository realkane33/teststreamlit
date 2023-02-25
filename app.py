import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from io import BytesIO
import pip
pip.main(['install', 'streamlit'])

st.set_page_config(page_title='paiement releveurs')
st.header('Paiement releveur')
st.subheader("test test")

### --- LOAD DATAFRAME
a=st.file_uploader("charger le paiement des releveurs")
releveur=pd.read_excel(a.read())
b=st.file_uploader("charger les compteurs", type="xlsx")
compteurs=pd.read_excel(b) 
forage=compteurs["forage"]
nombre=compteurs["nombre"]
a=releveur["FORAGE"] 
b=[]
erreur=[]
print(a)
for i in range (len(a)):
	c=str(a[i]).split(",")
	b.insert(i,c)
	n=[]
i=0
for objet in b:
	k=0
	
	for site in objet:
		try:
			j=compteurs.loc[compteurs['forage'] ==site.lstrip().lower()]
			
			k+=j.iloc[0,1]
         
		except:
			k="NA"
			erreur.append(site.lstrip().lower())

	n.insert(i,k)
	 
	i+=1
releveur["Nombre de compteurs"]=n
erreurs=pd.DataFrame()
erreurs["sites"]=erreur
c=releveur.to_excel("ncompteur.xlsx")
erreurs.to_excel("sites mal orthographié.xlsx")


def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output)
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data
df_xlsx = to_excel(releveur)
st.download_button(label='📥 Download les  Resultats',
                                data=df_xlsx ,
                                file_name= 'df_test.xlsx')
		






