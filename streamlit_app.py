import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Visualisasi Data Tips")
    
    # Baca dataset
    data = pd.read_csv("D:\\Ida Ernawati\\Documents\\e-book college\\6\\DAVIS (P. Irwan)\\Datasets\\tips.csv")
    
    # Pilihan visualisasi
    chart_type = st.sidebar.selectbox("Pilih Jenis Visualisasi", ["Scatter Plot", "Line Plot", "Bar Plot", "Histogram"])
    
    if chart_type == "Scatter Plot":
        st.subheader("Scatter Plot")
        scatter_plot(data)
    elif chart_type == "Line Plot":
        st.subheader("Line Plot")
        line_plot(data)
    elif chart_type == "Bar Plot":
        st.subheader("Bar Plot")
        bar_plot(data)
    elif chart_type == "Histogram":
        st.subheader("Histogram")
        histogram(data)

def scatter_plot(data):
    # Scatter plot with day against tip
    plt.scatter(data['day'], data['tip'], c=data['size'], s=data['total_bill'])
    # Adding Title to the Plot
    plt.title("Scatter Plot")
    # Setting the X and Y labels
    plt.xlabel('Day')
    plt.ylabel('Tip')
    plt.colorbar()
    st.pyplot()

def line_plot(data):
    plt.plot(data['tip'])
    plt.plot(data['size'])
    # Adding Title to the Plot
    plt.title("Line Plot")
    # Setting the X and Y labels
    plt.xlabel('Index')
    plt.ylabel('Value')
    st.pyplot()

def bar_plot(data):
    sns.barplot(x='day',y='tip', data=data, hue='sex')
    st.pyplot()

def histogram(data):
    sns.histplot(x='total_bill', data=data, kde=True, hue='sex')
    st.pyplot()

if __name__ == "__main__":
    main()
