# jobs/business_queries.py

from pyspark.sql.functions import sum, count, desc


def top_spending_customers(df):
    """
    Returns top customers by total spending.
    """
    return df.groupBy("customer_name") \
        .agg(sum("txn_amount").alias("total_spent")) \
        .orderBy(desc("total_spent"))
