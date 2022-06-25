import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_sample.csv")

def line_graph():
    # st.line_chart(df)
    col = st.columns(3)
    with col[1]:
        st.subheader("Line graph")
    line_df = df[['Fname','Age']]
    # line_df['average_age'] = line_df['Age'].mean(axis=0)
    # st.write(line_df)
    line_df = line_df.set_index('Fname')
    st.line_chart(line_df)

    st.subheader('Stacked chart')
    stack_df = df[['Fname','Children','Pets']]
    # plot bars in stack manner
    plt.bar(stack_df.Fname, stack_df.Children, color='r')
    plt.bar(stack_df.Fname, stack_df.Pets, bottom=stack_df.Children, color='b')
    plt.xlabel("Names")
    plt.ylabel("Count")
    plt.legend(["Children", "Pets"])
    plt.title("No. of Childrens & Pets")
    plt.savefig("stack_graph.png")

