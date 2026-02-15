# jobs/business_queries.py

from pyspark.sql.functions import sum, count, desc


def top_spending_customers(df):
    """
    Returns top customers by total spending.
    """
    return df.groupBy("customer_name") \
        .agg(sum("txn_amount").alias("total_spent")) \
        .orderBy(desc("total_spent"))


def fraud_transaction_percentage(df):
    """
    Returns fraud vs normal transaction counts.
    """
    return df.groupBy("fraud_flag") \
        .agg(count("*").alias("transaction_count")) \
        .orderBy(desc("transaction_count"))


def revenue_by_merchant(df):
    """
    Returns merchants generating highest revenue.
    """
    return df.groupBy("merchant") \
        .agg(sum("txn_amount").alias("merchant_revenue")) \
        .orderBy(desc("merchant_revenue"))


def spending_by_city(df):
    """
    Returns spending breakdown by city.
    """
    return df.groupBy("city") \
        .agg(sum("txn_amount").alias("city_spending")) \
        .orderBy(desc("city_spending"))
