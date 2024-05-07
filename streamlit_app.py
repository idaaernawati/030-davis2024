import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Visualisasi Data Tips")
    
    # Baca dataset (gunakan path relatif jika file berada dalam folder yang sama dengan script)
    data = pd.read_csv("tips.csv")
    
    # Pilihan visualisasi
    chart_type = st.sidebar.selectbox("Pilih Jenis Visualisasi", ["Scatter Plot", "Line Plot", "Bar Plot", "Histogram"])
    
    if chart_type == "Scatter Plot":
        scatter_plot(data)
    elif chart_type == "Line Plot":
        line_plot(data)
    elif chart_type == "Bar Plot":
        bar_plot(data)
    elif chart_type == "Histogram":
        histogram(data)

def scatter_plot(data):
    st.subheader("Scatter Plot")
    # Scatter plot with day against tip
    fig, ax = plt.subplots()
    scatter = ax.scatter(data['day'], data['tip'], c=data['size'], s=data['total_bill'])
    # Adding Title to the Plot
    ax.set_title("Scatter Plot")
    # Setting the X and Y labels
    ax.set_xlabel('Day')
    ax.set_ylabel('Tip')
    fig.colorbar(scatter, ax=ax)
    st.pyplot(fig)

def line_plot(data):
    st.subheader("Line Plot")
    fig, ax = plt.subplots()
    ax.plot(data['tip'])
    ax.plot(data['size'])
    # Adding Title to the Plot
    ax.set_title("Line Plot")
    # Setting the X and Y labels
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    st.pyplot(fig)

def bar_plot(data):
    st.subheader("Bar Plot")
    fig, ax = plt.subplots()
    sns.barplot(x='day',y='tip', data=data, hue='sex', ax=ax)
    st.pyplot(fig)

def histogram(data):
    st.subheader("Histogram")
    fig, ax = plt.subplots()
    sns.histplot(x='total_bill', data=data, kde=True, hue='sex', ax=ax)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
