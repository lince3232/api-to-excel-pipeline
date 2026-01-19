

```markdown
# API to Excel Pipeline

A Python-based data automation pipeline that extracts data from external APIs, cleans and transforms it, calculates business KPIs, and exports the results to Excel and PDF formats for analysis and reporting.

This project is built with a modular, scalable, and test-driven approach, suitable for real-world data engineering and automation use cases.

---

## Overview

This pipeline automates the following workflow:

-   Fetches raw data from a REST API
-   Cleans and normalizes incoming data
-   Transforms API responses into structured Pandas DataFrames
-   Calculates business KPIs
-   Exports processed data to Excel and PDF reports
-   Optionally stores data in a MySQL database

---

## Features

-   REST API data extraction
-   Data cleaning and normalization
-   KPI calculation (price averages, ratings, inventory metrics)
-   Excel report generation
-   PDF report generation
-   Modular and scalable architecture
-   Automated tests using Pytest
-   API request mocking for reliable testing

---

## Project Structure

```text
api-to-excel-pipeline/
│
├── src/
│   ├── api/
│   │   └── api_provider.py
│   ├── processing/
│   │   ├── data_processing.py
│   │   └── kpis.py
│   ├── export/
│   │   ├── excel_export.py
│   │   └── pdf_export.py
│   └── main.py
│
├── tests/
│   ├── test_api_provider.py
│   ├── test_data_processing.py
│   └── test_kpis.py
│
├── .env.example
├── ERRORS.md
├── README.md
├── requirements.txt
└── pytest.ini

```

---

## Tech Stack

---

## Prerequisites

Before you begin, ensure you have met the following requirements:

* **Python 3.12+** installed on your system.
* (Optional) Access to a MySQL database instance if you plan to use the database storage feature.

---

## Installation

Follow these steps to get your development environment set up:

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/api-to-excel-pipeline.git](https://github.com/your-username/api-to-excel-pipeline.git)
cd api-to-excel-pipeline

```


2. **Set up the virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows use: .venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Configure Environment Variables:**
Create a `.env` file in the root directory of the project, based on the `.env.example` file. This file will hold your API keys, database credentials, or any other sensitive configuration.
```ini
# .env example
API_BASE_URL=[https://api.example.com/v1/](https://api.example.com/v1/)
API_KEY=your_api_key_here
DB_HOST=localhost
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_database_name

```



---

## Usage

### Running the Pipeline

To execute the data pipeline and generate reports:

```bash
python src/main.py

```

This will fetch data, process it, calculate KPIs, and save the Excel and PDF reports in a designated output folder (e.g., `reports/`).

### Running Tests

To run the automated tests using Pytest:

```bash
pytest

```

---

## Test Coverage

The project includes comprehensive tests for:

* API data fetching logic
* Data processing and normalization
* KPI calculation logic

---

## Work in Progress

This project is still under active development. Planned improvements include:

* Email delivery of generated reports
* Interactive dashboard for KPI visualization
* Additional data cleaning strategies for different API schemas
* Support for multiple API providers (e.g., a configurable `api_provider.py`)
* Environment-based configuration management (beyond basic `.env`)

---

## Known Issues

All bugs, edge cases, and development issues discovered during implementation are documented in:

[ERRORS.md](ERRORS.md)

---

## Design Goals

* Clean separation of concerns for maintainability
* Extensible and adaptable architecture
* Test-driven development (TDD) principles applied
* Implementation of real-world data pipeline practices

---

## Status

* Core pipeline implemented
* All tests passing
* Advanced features in progress
