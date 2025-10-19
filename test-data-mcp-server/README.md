# Synthetic Test Data Generation MCP Server

Model Context Protocol server that generates realistic synthetic test data for any domain. Supports JSON, CSV, and SQL formats with automatic local storage.

## Features

- **Universal Domain Support**: Generate data for any domain (employee, customer, business, IoT, or custom)
- **Multiple Formats**: Output in JSON, CSV, or SQL format
- **Realistic Data**: Uses Faker library for authentic-looking test data
- **Automatic Storage**: Saves all generated datasets locally with timestamped filenames
- **Deterministic**: Uses fixed seeds for reproducible results
- **Claude Desktop Integration**: Works seamlessly with Claude Desktop via MCP
- **Extensible**: Easy to add new domain templates

## Prerequisites

- Python 3.10 or higher
- `uv` package manager (recommended) or `pip`
- Claude Desktop (for integration)

### Supported Domains

#### Predefined Domains (with rich schemas):

- **employee**: ID, name, email, department, position, salary, hire_date
- **customer**: ID, name, email, phone, country, registration_date, status
- **business**: ID, name, address, city, country, revenue, sector, founded_year, employees
- **product**: ID, name, category, price, stock, supplier, rating
- **transaction**: ID, customer_ID, amount, currency, timestamp, status, payment_method
- **iot**: device_ID, type, location, temperature, humidity, battery_level, last_update

#### Custom Domains:

The server automatically generates appropriate schemas for any domain you specify:

```
Generate 100 hospital records in CSV
Generate 50 school records in JSON
Generate 25 restaurant records in SQL
```

### Output Formats

**JSON** - Structured data with proper indentation
```json
[
  {
    "employee_id": "EMP00001",
    "name": "John Smith",
    "email": "john.smith@example.com",
    "department": "Engineering",
    "position": "Software Developer",
    "salary": 85000,
    "hire_date": "2021-03-15"
  }
]
```

**CSV** - Tabular format with headers
```csv
employee_id,name,email,department,position,salary,hire_date
EMP00001,John Smith,john.smith@example.com,Engineering,Software Developer,85000,2021-03-15
```

**SQL** - INSERT statements ready for database import
```sql
INSERT INTO employee (employee_id, name, email, department, position, salary, hire_date) 
VALUES ('EMP00001', 'John Smith', 'john.smith@example.com', 'Engineering', 'Software Developer', 85000, '2021-03-15');
```

## File Storage

All generated datasets are automatically saved in the `data/` directory with timestamped filenames:

```
data/
├── employee_data_2025-10-18_1045.csv
├── customer_data_2025-10-18_1047.json
├── business_data_2025-10-18_1050.sql
└── iot_data_2025-10-18_1052.json
```
