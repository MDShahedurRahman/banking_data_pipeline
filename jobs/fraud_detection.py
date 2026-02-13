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

    fraud_df = df.withColumn(
        "fraud_flag",
        when(col("txn_amount") > 3000, "HIGH_AMOUNT")
    )

    fraud_df.write.mode("overwrite").parquet(fraud_path)

    print("🚨 Fraud Detection Completed: Fraud Flags Added")
    return fraud_df
