-- Databricks notebook source
-- MAGIC %md
-- MAGIC ## Ingest companies data into bronze layer
-- MAGIC 1. Create the bronze schema if doesn't already exists
-- MAGIC 1. Create the bronze companies table with the data from landing folder. 

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS demo.bronze
     MANAGED LOCATION 's3://databricks-catalog-sans/demoDAG/';  

-- COMMAND ----------

DROP TABLE IF EXISTS demo.bronze.companies;

CREATE TABLE demo.bronze.companies
AS
SELECT company_name, founded_date, country
  FROM read_files('s3://databricks-catalog-sans/demoDAG/landing/top_tech_companies*',
                  format => 'csv',
                  header => true);

-- COMMAND ----------

SELECT * FROM demo.bronze.companies;

-- COMMAND ----------


