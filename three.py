import streamlit as st
import pandas as pd
import create_heatmap, h_h_map
import datetime
import hydralit_components as hc


def graph_user():
    st.subheader("Roomwise Hourly Non-Compliances.")
    c = st.columns(3)
    with c[0]:
        val1 = st.number_input("Mention a Value for Room-1", value=2)
    with c[1]:
        val2 = st.number_input("Mention a Value for Room-2", value=2)
    with c[2]:
        data_value = st.date_input("Mention a Date",datetime.date(2022, 4, 18))
    #st.write(data_value)

    heat_map_data= create_heatmap.heat_map_func(data_value,int(val1),int(val2))
    save_path = "dynamic_images"
    image = h_h_map.create_dashboard_occ_heatmap(heat_map_data,save_path,cmap='Reds')
    st.write(image)


    occ_today_df = create_heatmap.func_1(str(data_value),int(val1))
    M1_occ = str(occ_today_df["M1 Separation Room"].values[0]) ## to do - values of total non-compliances
    occ_today = create_heatmap.func_1(str(data_value),int(val2))
    M2_occ = str(occ_today["M2 Purification Room"].values[0])
    col = st.columns(2)
    with col[0]:
        hc.info_card(title='Room-1 Total Count', content=M1_occ, bar_value=M1_occ, sentiment='neutral')
    with col[1]:
        hc.info_card(title='Room-2 Total Count', content=M2_occ, bar_value=M2_occ, sentiment='neutral')

