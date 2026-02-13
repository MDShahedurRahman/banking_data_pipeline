# jobs/bronze_ingestion.py

from utils.schema_definitions import transaction_schema


def ingest_transactions(spark, input_file, bronze_path):
    """
    Bronze Layer Job:
    - Reads raw CSV transactions
    - Writes raw Parquet output
    """
