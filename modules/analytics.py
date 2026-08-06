import pandas as pd

def load_data():
    return pd.read_csv("data/sales_data.csv")


def total_revenue(df):
    return df["Revenue"].sum()


def total_orders(df):
    return len(df)


def total_customers(df):
    return df["Customer_Name"].nunique()


def total_companies(df):
    return df["Company_Name"].nunique()

# Revenue by Service
def revenue_by_service(df):
    return (
        df.groupby("Service")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )


# Revenue by City
def revenue_by_city(df):
    return (
        df.groupby("City")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )


# Top Customers
def top_customers(df):

    return (
        df.groupby("Company_Name")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

# Dataset Preview
def preview_data(df):
    return df.head(10)
# Revenue by City
def revenue_by_city(df):
    return (
        df.groupby("City")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )


# Top 10 Customers
def top_customers(df):
    return (
        df.groupby("Company_Name")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )