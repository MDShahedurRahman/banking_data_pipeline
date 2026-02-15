# main.py

from config import RAW_FILE, BRONZE_PATH, SILVER_PATH, FRAUD_PATH, GOLD_PATH
from utils.spark_session import get_spark_session

from jobs.bronze_ingestion import ingest_transactions
from jobs.silver_cleaning import clean_transaction_data
from jobs.fraud_detection import fraud_detection
from jobs.gold_star_schema import build_star_schema

from jobs.business_queries import (
    top_spending_customers,
    fraud_transaction_percentage,
    revenue_by_merchant,
    spending_by_city
)


def main():
    spark = get_spark_session()

    print("\n--- Running Banking Data Pipeline ---\n")

    # Bronze Layer
    bronze_df = ingest_transactions(spark, RAW_FILE, BRONZE_PATH)

    # Silver Layer
    silver_df = clean_transaction_data(bronze_df, SILVER_PATH)

    # Fraud Detection
    fraud_df = fraud_detection(silver_df, FRAUD_PATH)

    # Gold Layer
    build_star_schema(fraud_df, GOLD_PATH)

    # Business Queries
    print("\n📊 Top Spending Customers:")
    top_spending_customers(fraud_df).show()

    print("\n🚨 Fraud Transaction Breakdown:")
    fraud_transaction_percentage(fraud_df).show()

    print("\n🏦 Revenue by Merchant:")
    revenue_by_merchant(fraud_df).show()


if __name__ == "__main__":
    main()
