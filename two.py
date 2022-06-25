import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def fun_graph(df):
    st.subheader("User defiened functions for graph")
    # df will be the csv file from where we are selecting data in tru false format.
    data_new = pd.DataFrame({'True':[sum(df.gloves == True),sum(df.bottle == True),sum(df.sop == True)],
            'False':[sum(df.gloves == False),sum(df.bottle == False),sum(df.sop == False)],
                })
    print(data_new)
    # create stacked bar chart for data_new DataFrame
    data_new.plot.barh(stacked=True, color=['green', 'red'])
    # Add Title and Labels
    # plt.title('Activity Chart')
    plt.yticks([0, 1, 2], ['Gloves', 'Bottle', 'SOP'],rotation=45, fontsize=15)
    plt.xlabel('Current State', fontsize=15)
    plt.legend(bbox_to_anchor=(0.9, 1))
    plt.savefig("graph_new.png")

# make_graph(new_df)