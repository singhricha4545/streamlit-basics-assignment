import streamlit as st
import pandas as pd

# Title and description
st.title("📊 Sales Summary Dashboard")
st.subheader("Filter sales data by category and view trends")

#dataset
data = {
    "Product": ["Laptop", "Shirt", "Mobile", "Jeans", "Tablet"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "Sales": [50000, 2000, 30000, 2500, 15000]
}

df = pd.DataFrame(data)

# Sidebar for filter
st.sidebar.header("Filter Options")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filtering the data
filtered_df = df[df["Category"] == category]

# Display the table
st.write(f"### Showing data for: {category}")
st.dataframe(filtered_df)

# Line chart here
st.write("### Sales Trend")
st.line_chart(filtered_df["Sales"])