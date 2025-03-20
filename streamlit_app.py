import streamlit as st
from Python.visualization import load_data, plot_sales_trend, plot_category_sales, plot_interactive_sales

# Title of the Streamlit app
st.title("Sales Data Dashboard")

# Load dataset
df = load_data()

# Show dataset preview
st.write("### Data Preview")
st.dataframe(df.head())

# Monthly Sales Trend
st.write("### Monthly Sales Trend")
fig1 = plot_sales_trend(df)
st.pyplot(fig1)

# Sales by Category
st.write("### Sales by Category")
fig2 = plot_category_sales(df)
st.pyplot(fig2)

# Interactive Sales Distribution
st.write("### Interactive Sales Visualization")
fig3 = plot_interactive_sales(df)
st.plotly_chart(fig3)

# Footer
st.write("### Insights")
st.write("This dashboard provides insights into monthly sales trends, category-wise sales distribution, and an interactive view of sales performance.")

