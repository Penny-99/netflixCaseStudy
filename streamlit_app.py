import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('/kaggle/input/netflix-userbase-dataset/Netflix Userbase.csv')

# Streamlit App
st.title("Netflix Userbase Analysis")

# Choropleth Map: Number of Netflix Users by Country
country_data = data.groupby('Country').agg({'User ID': 'count', 'Monthly Revenue': 'sum'}).reset_index()
fig1 = px.choropleth(country_data, locations='Country', locationmode='country names',
                     color='User ID', title='Number of Netflix Users by Country',
                     hover_name='Country', color_continuous_scale='Plasma')
st.plotly_chart(fig1)

# Choropleth Map: Total Netflix Revenue by Country
fig2 = px.choropleth(country_data, locations='Country', locationmode='country names',
                     color='Monthly Revenue', title='Total Netflix Revenue by Country',
                     hover_name='Country', color_continuous_scale='Plasma')
st.plotly_chart(fig2)

# Plots using Matplotlib and Seaborn
st.subheader("Demographic Analysis")

# Age Distribution
fig_age = plt.figure(figsize=(10, 6))
sns.histplot(data=data, x="Age", binwidth=10, color='skyblue')
plt.title('Age Distribution')
st.pyplot(fig_age)

# Gender Distribution
fig_gender = plt.figure(figsize=(10, 6))
sns.countplot(data=data, x="Gender", palette='pastel')
plt.title('Gender Distribution')
st.pyplot(fig_gender)

# Country Distribution
fig_country = plt.figure(figsize=(10, 6))
sns.countplot(y="Country", data=data, palette='pastel')
plt.title('Country Distribution')
st.pyplot(fig_country)

# Device Usage Distribution
fig_device = plt.figure(figsize=(10, 6))
sns.countplot(y="Device", data=data, palette='pastel')
plt.title('Device Usage Distribution')
st.pyplot(fig_device)

# Subscription and Plan Distribution
st.subheader("Subscription and Plan Analysis")

# Subscription Type Distribution
fig_subscription = plt.figure(figsize=(10, 6))
sns.countplot(data=data, x="Subscription Type", palette='pastel')
plt.title('Subscription Type Distribution')
st.pyplot(fig_subscription)

# Plan Duration Distribution
fig_plan_duration = plt.figure(figsize=(10, 6))
sns.countplot(data=data, x="Plan Duration", palette='pastel')
plt.title('Plan Duration Distribution')
st.pyplot(fig_plan_duration)

# Revenue Distribution Analysis
st.subheader("Revenue Distribution Analysis")

# Revenue Distribution by Subscription Type
fig_rev_sub = plt.figure(figsize=(10, 6))
sns.boxplot(x="Subscription Type", y="Monthly Revenue", data=data, palette='pastel')
plt.title('Revenue Distribution by Subscription Type')
st.pyplot(fig_rev_sub)

# Revenue Distribution by Country
fig_rev_country = plt.figure(figsize=(10, 6))
sns.boxplot(y="Country", x="Monthly Revenue", data=data, palette='pastel')
plt.title('Revenue Distribution by Country')
st.pyplot(fig_rev_country)

# Revenue Distribution by Device
fig_rev_device = plt.figure(figsize=(10, 6))
sns.boxplot(x="Device", y="Monthly Revenue", data=data, palette='pastel')
plt.title('Revenue Distribution by Device')
st.pyplot(fig_rev_device)

# Churn Rate Calculation
st.subheader("Churn Rate Calculation")

# Convert the 'Join Date' and 'Last Payment Date' columns to datetime objects
data['Join Date'] = pd.to_datetime(data['Join Date'], format='%d-%m-%y')
data['Last Payment Date'] = pd.to_datetime(data['Last Payment Date'], format='%d-%m-%y')

# Calculate the number of days between the join date and the last payment date
data['Days Active'] = (data['Last Payment Date'] - data['Join Date']).dt.days

# Calculate the churn rate
churn_rate = (data['Days Active'] < 30).mean()

st.write(f"Churn Rate: {churn_rate:.2%}")
