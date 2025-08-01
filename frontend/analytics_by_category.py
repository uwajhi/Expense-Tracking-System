import streamlit as st
from datetime import datetime
import requests
import pandas as pd

def analytics_by_category_tab(API_URL):
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1), key="start_date")
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5), key="end_date" )

    if st.button("Get Analytics"):
        payload = {
            "start_date" : start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
        with st.spinner("Loading Analytics..."):
            response = requests.post(f"{API_URL}/analytics/category", json=payload)
            response = response.json()

            data = {
                "Category": list(response.keys()),
                "Total": [response[category]['total']for category in response],
                "Percentage": [response[category]['percentage']for category in response]
            }

            df = pd.DataFrame(data)
            df_sorted= df.sort_values(by="Percentage", ascending=False)

            st.title("Expense Breakdown by Category")

            st.bar_chart(data=df_sorted.set_index("Category")['Percentage'], width=0, height=0, use_container_width=50)
            df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
            df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)
            st.table(df_sorted)