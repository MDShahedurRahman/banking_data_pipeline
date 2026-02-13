# utils/spark_session.py

from pyspark.sql import SparkSession


def get_spark_session(app_name="BankingPipeline"):
    """
    Creates and returns a Spark session.
    """
    return SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .getOrCreate()
