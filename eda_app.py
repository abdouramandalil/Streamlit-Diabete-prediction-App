import streamlit as st 
import pandas as pd 

import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px

@st.cache
def load_data(data):
	df=pd.read_csv(data)
	return df



def run_eda_app():
	st.subheader("Exploratory Data Analysis")
	#df=pd.read_csv("datas/diabetes_data_upload.csv")
	df=load_data("datas/diabetes_data_upload.csv")
	df_encoded=load_data("datas/diabetes_data_upload_clean.csv")
	freq_df=load_data("datas/freqdist_of_age_data.csv")
	

	submenu=st.sidebar.selectbox("Submenu",["Descriptive","Plots"])
	if submenu=="Descriptive":
		st.dataframe(df)

		with st.expander("Describe Summary"):
			st.dataframe(df_encoded.describe())

		with st.expander("Class Distribution"):
			st.dataframe(df_encoded["class"].value_counts())

		with st.expander("Gender Distribution"):
			st.dataframe(df["Gender"].value_counts())

	elif submenu=="Plots":
		st.subheader("Plots")

		col1,col2=st.columns([2,1])

		with col1:
			with st.expander("Dist plots of Gender"):
				# fig=plt.figure()
				# sns.countplot(df['Gender'])
				# st.pyplot(fig)

				data=df['Gender'].value_counts().to_frame()
				data=data.reset_index()
				data.columns=["Gender Type","Counts"]
				#st.dataframe(data)

				p1=px.pie(data,names="Gender Type",values="Counts")
				st.plotly_chart(p1,use_container_width=True)

			with st.expander("Dist plots of Classes"):
				fig=plt.figure()
				sns.countplot(df['class'])
				st.pyplot(fig)

		with col2:
			with st.expander("Gender Distribution"):
				st.dataframe(data)
			
			with st.expander("Gender Distribution"):
				st.dataframe(df['class'].value_counts())

		with st.expander("Frequency Dist of age"):
			st.dataframe(freq_df)
			p2=px.bar(freq_df,x="Age",y="count")
			st.plotly_chart(p2)

		with st.expander("Outlier Detection Plot"):
			fig=plt.figure()
			sns.boxplot(df["Age"])
			st.pyplot(fig)

			p3=px.box(df,x="Age",color="Gender")
			st.plotly_chart(p3)

		with st.expander("Correlation Plot"):
			corr_matrix=df_encoded.corr()
			fig=plt.figure(figsize=(20,10))
			sns.heatmap(corr_matrix,annot=True)
			st.pyplot(fig)
 
