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

    return fact_transactions
