import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Titanic Data Visualizations")

# Load dataset
df = sns.load_dataset("titanic")

# Bar chart: Survivors by gender
st.subheader("Survivors by Gender")
survivors = df[df['survived'] == 1]['sex'].value_counts()
st.bar_chart(survivors)

# Histogram: Age distribution
st.subheader("Age Distribution")
fig1, ax1 = plt.subplots()
ax1.hist(df['age'].dropna(), bins=20, color='skyblue', edgecolor='black')
st.pyplot(fig1)

# Pie chart: Class distribution
st.subheader("Passenger Class Distribution")
class_counts = df['class'].value_counts()
fig2 = px.pie(names=class_counts.index, values=class_counts.values, title="Class Distribution")
st.plotly_chart(fig2)
