# Batch Data Processing for Music Streaming

This project implements a batch data processing pipeline for a music streaming service. The goal is to analyze user listening behaviors and song popularity to generate actionable Key Performance Indicators (KPIs).

## 🏗️ Architecture

The project follows a standard batch processing architecture:

1.  **Data Lake (Input)**: Raw data is stored in CSV format, representing the core entities of the streaming platform (Users, Songs, and Stream logs).
2.  **Processing Layer**: Python and Pandas are used (via Jupyter Notebooks) to ingest, clean, and transform the raw data.
3.  **Orchestration**: (Planned) Apache Airflow will schedule and manage the dependency between processing tasks.
4.  **Analytics (Output)**: The pipeline produces aggregated metrics (KPIs) such as hourly listening trends and genre popularity.

## 📂 Project Structure

```
Batch_Data_Processing_MusicStreams/
├── airflow-dag/          # (Planned) Airflow DAGs for orchestrating the pipeline
├── data/                 # Raw input data (CSV files)
│   ├── songs.csv         # Metadata for all available tracks
│   ├── users.csv         # Registered user demographics
│   ├── streams1.csv      # Log of songs played by users (Part 1)
│   ├── streams2.csv      # Log of songs played by users (Part 2)
│   └── streams3.csv      # Log of songs played by users (Part 3)
├── main/                 # Processing Logic (Jupyter Notebooks)
│   ├── genre_level_KPIs.ipynb  # Analyzes streams by genre
│   └── hourly_KPIs.ipynb       # Analyzes streams by time of day
└── requirements.txt      # Python dependencies
```

## 📊 Data Schema

The analysis relies on three primary datasets:

### 1. Songs (`songs.csv`)
Contains metadata for the music catalog.
*   **track_id**: Unique identifier for the song.
*   **artists**: Artist name(s).
*   **track_name**: Title of the song.
*   **album_name**: Album title.
*   **track_genre**: Genre of the track (Critical for Genre KPIs).
*   **popularity**: Popularity score.
*   **duration_ms**: Length of the track in milliseconds.
*   *Other audio features*: `danceability`, `energy`, `key`, `loudness`, `tempo`, etc.

### 2. Users (`users.csv`)
Contains demographic information about the listeners.
*   **user_id**: Unique identifier for the user.
*   **user_name**: Name of the user.
*   **user_age**: Age of the user.
*   **user_country**: Country of residence.
*   **created_at**: Account creation date.

### 3. Streams (`streams*.csv`)
Transactional logs recording every time a user listens to a song.
*   **user_id**: The user who listened.
*   **track_id**: The track that was played.
*   **listen_time**: Timestamp of when the stream occurred (Critical for Hourly KPIs).

## 📈 Key Performance Indicators (KPIs)

The project focuses on calculating the following metrics:

### Hourly KPIs (`hourly_KPIs.ipynb`)
**Goal:** Identify peak listening times to optimize server scaling and ad placement.
*   **Streams per Hour**: Aggregation of stream counts grouped by the hour of the day.
*   **Daily Active Users (DAU)**: Unique users active within each 24-hour period.

### Genre Level KPIs (`genre_level_KPIs.ipynb`)
**Goal:** Understand user preferences to improve recommendation algorithms.
*   **Top Genres**: Ranking of genres based on total stream counts.
*   **Genre Trends**: Analyzing how specific genres perform across different user demographics (e.g., age groups or countries).

## 🚀 Getting Started

### Prerequisites
*   Python 3.8+
*   Pandas (`pip install pandas`)
*   Jupyter Lab or Notebook

### Running the Analysis
1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Navigate to the `main/` directory.
4.  Open `hourly_KPIs.ipynb` or `genre_level_KPIs.ipynb` in Jupyter to run the analysis cells.

## 🔜 Future Improvements
*   **Airflow Integration**: Populate `airflow-dag/` with DAG files to automate the daily execution of these notebooks.
*   **Data Validation**: Add checks for null values or duplicate transaction logs (streams).
*   **Dashboarding**: Export the calculated KPIs to a visualization tool or a SQL database for dashboarding.
