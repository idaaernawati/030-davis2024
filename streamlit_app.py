import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.subheader("Diagram Batang")
# reading the database
data = pd.read_csv("D:\\Ida Ernawati\\Documents\\e-book college\\6\\DAVIS (P. Irwan)\\Datasets\\tips.csv")

# Bar chart with day against tip
fig, ax = plt.subplots()
ax.bar(data['day'], data['tip'])
ax.set_title("Bar Chart")
ax.set_xlabel('Day')
ax.set_ylabel('Tip')

# Display the plot using st.pyplot() with the figure object
st.pyplot(fig)

############################################################
st.subheader("Histogram")
# Create the figure and axis objects
fig, ax = plt.subplots()

# Create the histogram using seaborn
sns.histplot(x='total_bill', data=data, kde=True, hue='sex', ax=ax)

# Display the plot using st.pyplot() with the figure object
st.pyplot(fig)

############################################################
st.subheader("Sliders and Selectors")
# This section cannot be directly converted as is to Streamlit because it involves Plotly, which requires a different approach
# Streamlit does support Plotly charts, but we need to use the streamlit.plotly_chart() function

# Instead of directly converting this section, I'll show you how to create an interactive Plotly chart using Streamlit:

import plotly.express as px

# Create the Plotly figure
fig = px.scatter(data, x='day', y='tip', color='size', size='total_bill')

# Update layout
fig.update_layout(
    title="Scatter Plot",
    xaxis_title="Day",
    yaxis_title="Tip"
)

# Display the Plotly chart using st.plotly_chart()
st.plotly_chart(fig)
