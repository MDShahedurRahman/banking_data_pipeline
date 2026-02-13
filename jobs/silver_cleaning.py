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
    return cleaned_df
