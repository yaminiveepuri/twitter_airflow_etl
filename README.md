# Twitter Data Extraction and ETL Pipeline with Snscrape and Airflow

This project demonstrates the extraction of tweets containing specific keywords, such as "cocacola" and "pepsi," using the Snscrape library. The extracted data is then processed and loaded into a database using an ETL (Extract, Transform, Load) pipeline constructed with Apache Airflow.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Twitter is a popular social media platform that contains a vast amount of valuable user-generated data. Extracting relevant tweets based on specific keywords can provide insights into user opinions, sentiment analysis, marketing research, and much more. This project demonstrates how to extract tweets related to "cocacola" and "pepsi" using the Snscrape library and process them using an ETL pipeline built with Apache Airflow.

## Installation

To use this project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yaminiveepuri/twitter_airflow_etl.git

2. Install the SNSCRAPE Library:
    ```bash
    pip install snscrape
3. Install Apache Airflow
   I have installed following this [Medium Article](https://medium.com/@jacksonbull1987/how-to-install-apache-airflow-6b8a2ae60050)

## Usage

1. Modify the Airflow configuration file (`airflow.cfg`) to match your environment. Set the `dags_folder` parameter to the location of the project's DAG file.
2. Start the Airflow webserver and scheduler:

   ```bash
   airflow webserver --port 8080
   airflow scheduler
3. Access the Airflow web interface by visiting http://localhost:8080 in your web browser.
4. Enable the twitter_dag in the Airflow UI and trigger the DAG to start the data extraction and ETL pipeline.

