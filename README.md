# SDA Assignment 3 — Citi Bike Streaming Analytics

## Pipeline
Python Dummy Data → Kafka Producer → `citibike-trips` → Kafka Consumer → MySQL → Grafana

## Files
- `dummy_data.py` — generates dummy Citi Bike records
- `producer.py` — publishes records to Kafka
- `consumer.py` — consumes Kafka records and inserts them into MySQL
- `dashboard.py` — retained for reference; Grafana is the dashboard
- `requirements.txt` — Python dependencies

## Database
MySQL database: `citibike_db`
Table: `trips`

## Dashboard
Grafana connected directly to MySQL.
