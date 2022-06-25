import streamlit as st
import pandas as pd
st.set_page_config(layout = 'wide', page_title='KT Session',page_icon="chart_with_upwards_trend")
from one import line_graph
from two import fun_graph
from three import graph_user

st.header("Graphs and User-defined Functions.")
sel = st.sidebar.radio("Select a Page to Visit",('Basic','Functions','User-def'))

data = pd.read_csv("data.csv")
new_df = data.tail(1)

if sel=='Basic':
    line_graph()
    st.image('stack_graph.png')
elif sel=='Functions':
    fun_graph(new_df)
    st.image('graph_new.png')
elif sel=='User-def':
    graph_user()



# plac = st.empty()

# dat - > to_csv 
# sleep(0.1)