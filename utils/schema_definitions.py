# utils/schema_definitions.py

from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType, DoubleType


def transaction_schema():
    """
    Defines schema for banking transactions CSV.
    """
    return StructType([
        StructField("txn_id", IntegerType(), True),
        StructField("customer_id", StringType(), True),
        StructField("customer_name", StringType(), True),
        StructField("account_type", StringType(), True),
        StructField("merchant", StringType(), True),
        StructField("category", StringType(), True),
        StructField("amount", DoubleType(), True),
        StructField("txn_date", StringType(), True),
        StructField("city", StringType(), True)
    ])
