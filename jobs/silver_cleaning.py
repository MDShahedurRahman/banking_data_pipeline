# jobs/silver_cleaning.py

from pyspark.sql.functions import col, to_date


def clean_transaction_data(df, silver_path):
    """
    Silver Layer Job:
    - Removes duplicates
    - Drops null values
    - Converts txn_date to DateType
    - Renames amount column
    """

    cleaned_df = df.dropDuplicates() \
        .dropna() \
        .withColumn("txn_date", to_date(col("txn_date"))) \
        .withColumnRenamed("amount", "txn_amount")

    cleaned_df.write.mode("overwrite").parquet(silver_path)

    print("✅ Silver Layer Completed: Cleaned Data Stored")
    return cleaned_df
