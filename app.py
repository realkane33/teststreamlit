import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='paiement releveurs')
st.header('Paiement releveur')
st.subheader("bestie bb lem je t'aime de srx")

### --- LOAD DATAFRAME
a=st.file_uploader("charger le paiement des releveurs", type="xlsx")
releveur=pd.read_excel(a)
b=st.file_uploader("charger les compteurs", type="xlsx")
compteurs=pd.read_excel(b) 
forage=compteurs["forage"]
nombre=compteurs["nombre"]
a=releveur["FORAGE"] 
b=[]
erreur=[]

for i in range (len(a)):
	c=a[i].split(",")
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
			print(site.lstrip().lower()+" n existe pas sur la plateforme")
			k="NA"
			erreur.append(site.lstrip().lower())

	n.insert(i,k)
	 
	i+=1
releveur["nombreC"]=n
erreurs=pd.DataFrame()
erreurs["sites"]=erreur
releveur.to_excel("ncompteur.xlsx")
erreurs.to_excel("sites mal orthographié.xlsx")
			
		






