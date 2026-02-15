# jobs/gold_star_schema.py

def build_star_schema(df, gold_path):
    """
    Gold Layer Job:
    Builds Star Schema tables:
    - dim_customer
    - dim_merchant
    - fact_transactions
    """

    # Dimension: Customer
    dim_customer = df.select(
        "customer_id",
        "customer_name",
        "account_type",
        "city"
    ).distinct()

    # Dimension: Merchant
    dim_merchant = df.select(
        "merchant",
        "category"
    ).distinct()

    # Fact Table: Transactions
    fact_transactions = df.select(
        "txn_id",
        "customer_id",
        "merchant",
        "txn_date",
        "txn_amount",
        "fraud_flag"
    )

    # Save tables
    dim_customer.write.mode("overwrite").parquet(gold_path + "/dim_customer")
    dim_merchant.write.mode("overwrite").parquet(gold_path + "/dim_merchant")

    return fact_transactions
