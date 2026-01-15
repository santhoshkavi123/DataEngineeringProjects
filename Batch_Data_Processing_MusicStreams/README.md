# Batch Data Processing for Music Streaming

This project implements a robust batch data processing pipeline for a music streaming service. It orchestrates the validation, transformation, and loading (ETL) of data from an S3 Data Lake into an AWS Redshift Data Warehouse using Apache Airflow.

## 🏗️ Architecture

The pipeline is designed to handle daily batch processing with the following stages:

1.  **Data Lake (Extraction)**: Raw CSV data (`songs`, `users`, `streams`) is ingested from an S3 bucket (`de-airflow-sansdags`).
2.  **Validation**: A custom Airflow task validates that all incoming datasets possess the required schema before processing begins.
3.  **Transformation**: Python (Pandas) is used to aggregate data and calculate business-critical KPIs (Hourly & Genre-based).
4.  **Loading**: Processed KPIs are upserted into AWS Redshift to ensure idempotency and data consistency.
5.  **Archival**: Successfully processed raw files are moved to an archive prefix in S3 to prevent re-processing.
6.  **Orchestration**: The entire workflow is managed by the `data_validation_and_kpi_calculations` Airflow DAG.

### Tech Stack
*   **Orchestration**: Apache Airflow
*   **Processing**: Python, Pandas
*   **Storage**: AWS S3
*   **Data Warehouse**: AWS Redshift
*   **Infrastructure**: Docker (Airflow running in containers)

## 📂 Project Structure

```
Batch_Data_Processing_MusicStreams/
├── airflow-dag/
│   └── dag_song_kpi_calculations.py  # Main Airflow DAG definition
├── data/                             # Local sample data
├── main/                             # Jupyter notebooks for prototyping logic
├── sql/
│   └── redshift_tables.sql           # DDL for Redshift tables
└── requirements.txt                  # Python dependencies
```

## � The Pipeline

The Airflow DAG (`dag_song_kpi_calculations.py`) executes the following tasks:

1.  **`validate_datasets`**: Checks `songs.csv`, `users.csv`, and all files in `streams/` prefix for required columns.
2.  **`check_validation`**: A `BranchPythonOperator` that acts as a circuit breaker. If validation fails, the pipeline skips processing and ends.
3.  **`calculate_genre_level_kpis`**:
    *   Reads data from S3.
    *   Aggregates streams by genre.
    *   Calculates popularity indices and average duration.
    *   Upserts results to `reporting_schema.genre_level_kpis` in Redshift.
4.  **`calculate_hourly_kpis`**:
    *   Aggregates streams by hour.
    *   Calculates unique listeners, sessions per user, and top artists.
    *   Upserts results to `reporting_schema.hourly_kpis` in Redshift.
5.  **`move_processed_files`**: Moves processed stream files from `streams/` to `streams/archived/` in S3.

## 📊 Data Schema

### Input Schema (S3 CSVs)
*   **Songs**: Metadata including `track_id`, `artists`, `track_genre`, `duration_ms`, etc.
*   **Users**: Demographics including `user_id`, `user_age`, `user_country`.
*   **Streams**: Transaction logs with `user_id`, `track_id`, `listen_time`.

### Output Schema (Redshift)

#### `reporting_schema.hourly_kpis`
Tracks platform usage patterns throughout the day.
```sql
CREATE TABLE reporting_schema.hourly_kpis (
    listen_date DATE NOT NULL,
    listen_hour INT NOT NULL,
    unique_listeners INT,
    listen_counts INT,
    top_artist VARCHAR(255),
    avg_sessions_per_user FLOAT,
    diversity_index FLOAT,
    most_engaged_age_group VARCHAR(255)
);
```

#### `reporting_schema.genre_level_kpis`
Analyzes popularity trends across different music genres.
```sql
CREATE TABLE reporting_schema.genre_level_kpis(
    listen_date DATE NOT NULL,
    track_genre VARCHAR(255) NOT NULL,
    listen_count INT,
    popularity_index FLOAT,
    average_duration FLOAT,
    most_popular_track_id VARCHAR(255)
);
```

## 🚀 Getting Started

### Prerequisites
*   Docker Desktop (for running Airflow)
*   AWS Account with S3 and Redshift access
*   configured `~/.aws/credentials` or Airflow Connections

### Configuration
1.  **Airflow Connection**: Create a Postgres connection in Airflow named `sansAirflowRedshiftConn` pointing to your Redshift cluster.
2.  **S3 Bucket**: Ensure the bucket `de-airflow-sansdags` exists and contains the `spotify_data/` folder structure.

### Running the Pipeline
1.  Place the DAG file in your Airflow DAGs folder.
2.  Trigger the `data_validation_and_kpi_computation` DAG from the Airflow UI.
3.  Monitor the `Graph View` to watch the execution flow.
