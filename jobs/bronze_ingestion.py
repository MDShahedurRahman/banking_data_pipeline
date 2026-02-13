# jobs/bronze_ingestion.py

from utils.schema_definitions import transaction_schema


def ingest_transactions(spark, input_file, bronze_path):
    """
    Bronze Layer Job:
    - Reads raw CSV transactions
    - Writes raw Parquet output
    """

    df = spark.read.csv(
        input_file,
        header=True,
        schema=transaction_schema()
    )

    df.write.mode("overwrite").parquet(bronze_path)

    print("✅ Bronze Layer Completed: Raw Parquet Stored")
    return df
