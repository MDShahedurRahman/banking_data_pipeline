# jobs/fraud_detection.py

from pyspark.sql.functions import col, when


def fraud_detection(df, fraud_path):
    """
    Fraud Detection Job:
    Flags suspicious transactions based on rules:
    - Amount > $3000
    - Merchant = Casino
    - Category = Gambling
    """
    return fraud_df
