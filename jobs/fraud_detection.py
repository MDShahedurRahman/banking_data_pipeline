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
        .when(col("merchant") == "Casino", "SUSPICIOUS_MERCHANT")
        .when(col("category") == "Gambling", "GAMBLING_CATEGORY")
    )

    return fraud_df
