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


if __name__ == "__main__":
    main()
