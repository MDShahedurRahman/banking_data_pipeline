# Smart Banking Transactions Data Engineering Pipeline (PySpark)

A complete **Data Engineering portfolio project** built using **PySpark** and the **Medallion Architecture (Bronze → Silver → Gold)**.

This project simulates how banks process millions of transactions daily by ingesting raw CSV transaction records, cleaning and enriching them, applying fraud detection rules, building a Star Schema, and generating business analytics KPIs.

---

## 🚀 Project Overview

Banks generate large volumes of financial transaction data every day.  
To support fraud analytics, customer insights, and reporting, raw transaction records must be transformed into clean, structured datasets.

This pipeline performs:

- Raw ingestion into a Data Lake (Bronze)
- Data cleaning and enrichment (Silver)
- Fraud rule flagging and anomaly detection
- Star Schema modeling for analytics (Gold)
- Business KPI queries for insights

---

## 🏗 Pipeline Architecture (Medallion Design)

Raw CSV Transactions  
→ Bronze Layer (Raw Parquet)  
→ Silver Layer (Clean + Fraud Flagged Parquet)  
→ Gold Layer (Star Schema Tables)  
→ Business Queries + KPI Reports

---

## 📂 Project Structure

banking_data_pipeline/

- main.py  
- config.py  
- requirements.txt  

data/  
- transactions.csv  

jobs/  
- bronze_ingestion.py  
- silver_cleaning.py  
- fraud_detection.py  
- gold_star_schema.py  
- business_queries.py  

utils/  
- spark_session.py  
- schema_definitions.py  
- helpers.py  

output/  
- bronze/  
- silver/  
- gold/  
- reports/  

---
