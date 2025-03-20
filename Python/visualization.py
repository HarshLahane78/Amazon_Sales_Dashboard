import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import matplotlib

matplotlib.use("Agg")  # Use non-GUI backend before importing pyplot


# Load dataset
def load_data(file_path="datasets/amazon_sales_data.csv"):
    df = pd.read_csv(file_path)

    # Debugging: Print available columns
    print("Loaded Data Columns:", df.columns)

    # Ensure 'Date' is in datetime format
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    return df


# Monthly sales trend visualization
def plot_sales_trend(df):
    """Plot the monthly sales trend."""

    # Ensure required columns exist
    if 'Sales' not in df.columns or 'Date' not in df.columns:
        print("Error: Missing 'Sales' or 'Date' column in dataset.")
        return None

    # Resample sales data monthly
    monthly_sales = df.resample('M', on='Date')['Sales'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='Date', y='Sales', data=monthly_sales, marker='o', ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Sales')
    ax.set_title('Monthly Sales Trend')
    ax.tick_params(axis='x', rotation=45)
    ax.grid()
    return fig


# Sales by category visualization
def plot_category_sales(df):
    """Plot sales distribution by category."""

    # Ensure required column exists
    if 'Sales' not in df.columns or 'Category' not in df.columns:
        print("Error: Missing 'Sales' or 'Category' column in dataset.")
        return None

    category_sales = df.groupby('Category')['Sales'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='Sales', y='Category', data=category_sales, palette='viridis', ax=ax)
    ax.set_xlabel('Total Sales')
    ax.set_ylabel('Category')
    ax.set_title('Sales by Category')
    return fig


# Interactive visualization using Plotly
def plot_interactive_sales(df):
    """Generate an interactive sales distribution plot using Plotly."""

    if 'Sales' not in df.columns or 'Category' not in df.columns:
        print("Error: Missing 'Sales' or 'Category' column in dataset.")
        return None

    category_sales = df.groupby('Category')['Sales'].sum().reset_index()
    fig = px.bar(category_sales, x='Category', y='Sales', color='Category',
                 title="Sales by Category (Interactive)")
    return fig


def save_plots():
    """Generate and save all visualizations."""
    df = load_data("datasets/amazon_sales_data.csv")

    # Save Monthly Sales Trend
    fig = plot_sales_trend(df)
    if fig:
        fig.savefig("static/images/sales_trend.png")
        print("✔️ Monthly sales trend saved.")

    # Save Sales by Category
    fig = plot_category_sales(df)
    if fig:
        fig.savefig("static/images/category_sales.png")
        print("✔️ Sales by category saved.")
