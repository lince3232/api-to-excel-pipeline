# Project Roadmap – API to Excel Pipeline

This roadmap outlines the current state of the project, planned improvements, and future enhancements.  
The goal is to evolve this pipeline into a robust, extensible, and production-ready data automation system.

---

##Completed

- REST API data extraction
- Error handling for API requests
- Data normalization and cleaning
- Transformation of raw API data into Pandas DataFrames
- KPI calculation module
- Excel report generation
- PDF report generation
- Modular project architecture
- Automated testing with Pytest
- API mocking for reliable and isolated tests
- Bug tracking and documentation (`ERRORS.md`)

---

## In Progress

- Improving data validation and edge-case handling
- Refactoring KPI logic for better flexibility
- Enhancing logging and error reporting

---

## Planned Features

- Email delivery of generated reports
- Interactive dashboard for KPI visualization
- Support for multiple API providers
- Environment-based configuration using `.env` files
- Additional data cleaning strategies for different data schemas
- Improved database integration (MySQL)

---

## Future Improvements

- Scheduling and automation (cron jobs, Airflow)
- Cloud storage integration (AWS S3, GCP, Azure)
- CI/CD pipeline for automated testing and deployment
- Dockerization for easier deployment
- Authentication support for protected APIs
- Performance optimization for large datasets

---

## Long-Term Vision

- Turn the project into a reusable data pipeline template
- Support plug-and-play data sources
- Enable scalable analytics workflows
- Make the pipeline suitable for enterprise-grade data engineering use cases
