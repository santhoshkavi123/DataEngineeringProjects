FROM apache/airflow:3.1.6-python3.13

USER root

# ---- system dependencies (example: Java for Spark) ----
RUN apt-get update && apt-get install -y openjdk-17-jdk && apt-get clean

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
ENV PATH=$JAVA_HOME/bin:$PATH

USER airflow

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt