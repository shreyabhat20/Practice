"""
Synthetic Test Data Generation MCP Server
Generates realistic test data for any domain with support for JSON, CSV, and SQL formats.
"""

import json
from datetime import datetime
from typing import Any
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from faker import Faker

# Initialize Faker with a seed for deterministic output
fake = Faker()
Faker.seed(42)

# Ensure data directory exists
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# Domain schemas - predefined templates for common domains
DOMAIN_SCHEMAS = {
    "employee": {
        "fields": ["employee_id", "name", "email", "department", "position", "salary", "hire_date"],
        "generators": {
            "employee_id": lambda i: f"EMP{str(i+1).zfill(5)}",
            "name": lambda i: fake.name(),
            "email": lambda i: fake.email(),
            "department": lambda i: fake.random_element(["Engineering", "Sales", "Marketing", "HR", "Finance", "Operations"]),
            "position": lambda i: fake.job(),
            "salary": lambda i: fake.random_int(min=40000, max=150000),
            "hire_date": lambda i: fake.date_between(start_date="-5y", end_date="today").isoformat()
        }
    },
    "customer": {
        "fields": ["customer_id", "name", "email", "phone", "country", "registration_date", "status"],
        "generators": {
            "customer_id": lambda i: f"CUST{str(i+1).zfill(6)}",
            "name": lambda i: fake.name(),
            "email": lambda i: fake.email(),
            "phone": lambda i: fake.phone_number(),
            "country": lambda i: fake.country(),
            "registration_date": lambda i: fake.date_between(start_date="-2y", end_date="today").isoformat(),
            "status": lambda i: fake.random_element(["Active", "Inactive", "Pending"])
        }
    },
    "business": {
        "fields": ["business_id", "name", "address", "city", "country", "revenue", "sector", "founded_year", "employees"],
        "generators": {
            "business_id": lambda i: f"BIZ{str(i+1).zfill(5)}",
            "name": lambda i: fake.company(),
            "address": lambda i: fake.street_address(),
            "city": lambda i: fake.city(),
            "country": lambda i: fake.country(),
            "revenue": lambda i: fake.random_int(min=100000, max=10000000),
            "sector": lambda i: fake.random_element(["Technology", "Healthcare", "Finance", "Retail", "Manufacturing", "Services"]),
            "founded_year": lambda i: fake.random_int(min=1950, max=2024),
            "employees": lambda i: fake.random_int(min=10, max=5000)
        }
    },
    "product": {
        "fields": ["product_id", "name", "category", "price", "stock", "supplier", "rating"],
        "generators": {
            "product_id": lambda i: f"PRD{str(i+1).zfill(6)}",
            "name": lambda i: fake.catch_phrase(),
            "category": lambda i: fake.random_element(["Electronics", "Clothing", "Food", "Books", "Home", "Sports"]),
            "price": lambda i: round(fake.random.uniform(10, 1000), 2),
            "stock": lambda i: fake.random_int(min=0, max=1000),
            "supplier": lambda i: fake.company(),
            "rating": lambda i: round(fake.random.uniform(1, 5), 1)
        }
    },
    "transaction": {
        "fields": ["transaction_id", "customer_id", "amount", "currency", "timestamp", "status", "payment_method"],
        "generators": {
            "transaction_id": lambda i: f"TXN{str(i+1).zfill(8)}",
            "customer_id": lambda i: f"CUST{fake.random_int(min=1, max=10000):06d}",
            "amount": lambda i: round(fake.random.uniform(5, 5000), 2),
            "currency": lambda i: fake.currency_code(),
            "timestamp": lambda i: fake.date_time_between(start_date="-1y", end_date="now").isoformat(),
            "status": lambda i: fake.random_element(["Completed", "Pending", "Failed", "Refunded"]),
            "payment_method": lambda i: fake.random_element(["Credit Card", "Debit Card", "PayPal", "Bank Transfer"])
        }
    },
    "iot": {
        "fields": ["device_id", "device_type", "location", "temperature", "humidity", "battery_level", "last_update"],
        "generators": {
            "device_id": lambda i: f"IOT{str(i+1).zfill(6)}",
            "device_type": lambda i: fake.random_element(["Sensor", "Camera", "Thermostat", "Smart Lock", "Light"]),
            "location": lambda i: f"{fake.city()}, {fake.country()}",
            "temperature": lambda i: round(fake.random.uniform(15, 35), 1),
            "humidity": lambda i: round(fake.random.uniform(30, 90), 1),
            "battery_level": lambda i: fake.random_int(min=0, max=100),
            "last_update": lambda i: fake.date_time_between(start_date="-7d", end_date="now").isoformat()
        }
    }
}


def generate_generic_schema(domain: str) -> dict:
    """Generate a generic schema for unknown domains."""
    fields = [f"{domain}_id", "name", "description", "created_at", "status"]
    
    generators = {
        f"{domain}_id": lambda i: f"{domain.upper()[:3]}{str(i+1).zfill(5)}",
        "name": lambda i: fake.name() if domain.lower() in ["user", "person", "staff"] else fake.company(),
        "description": lambda i: fake.text(max_nb_chars=100),
        "created_at": lambda i: fake.date_time_between(start_date="-1y", end_date="now").isoformat(),
        "status": lambda i: fake.random_element(["Active", "Inactive", "Pending"])
    }
    
    return {"fields": fields, "generators": generators}


def generate_data(domain: str, count: int) -> list[dict[str, Any]]:
    """Generate synthetic data for a given domain."""
    domain_lower = domain.lower()
    
    # Get schema (predefined or generic)
    if domain_lower in DOMAIN_SCHEMAS:
        schema = DOMAIN_SCHEMAS[domain_lower]
    else:
        schema = generate_generic_schema(domain_lower)
    
    data = []
    for i in range(count):
        record = {}
        for field in schema["fields"]:
            generator = schema["generators"][field]
            record[field] = generator(i)
        data.append(record)
    
    return data


def format_as_json(data: list[dict[str, Any]]) -> str:
    """Format data as JSON."""
    return json.dumps(data, indent=2)


def format_as_csv(data: list[dict[str, Any]]) -> str:
    """Format data as CSV."""
    if not data:
        return ""
    
    output = []
    fields = list(data[0].keys())
    
    # Header
    output.append(",".join(fields))
    
    # Rows
    for record in data:
        row = []
        for field in fields:
            value = str(record[field])
            # Escape commas and quotes
            if "," in value or '"' in value:
                value = f'"{value.replace('"', '""')}"'
            row.append(value)
        output.append(",".join(row))
    
    return "\n".join(output)


def format_as_sql(data: list[dict[str, Any]], domain: str) -> str:
    """Format data as SQL INSERT statements."""
    if not data:
        return ""
    
    table_name = domain.lower()
    fields = list(data[0].keys())
    
    output = [f"-- SQL INSERT statements for {table_name}\n"]
    
    for record in data:
        values = []
        for field in fields:
            value = record[field]
            if isinstance(value, str):
                # Escape single quotes
                value = value.replace("'", "''")
                values.append(f"'{value}'")
            elif value is None:
                values.append("NULL")
            else:
                values.append(str(value))
        
        sql = f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({', '.join(values)});"
        output.append(sql)
    
    return "\n".join(output)


def save_data(data: list[dict[str, Any]], domain: str, format_type: str) -> str:
    """Save generated data to a file and return the file path."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = f"{domain}_data_{timestamp}.{format_type}"
    filepath = DATA_DIR / filename
    
    # Format data
    if format_type == "json":
        content = format_as_json(data)
    elif format_type == "csv":
        content = format_as_csv(data)
    elif format_type == "sql":
        content = format_as_sql(data, domain)
    else:
        raise ValueError(f"Unsupported format: {format_type}")
    
    # Write to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    return str(filepath)


# Initialize FastMCP server
mcp = FastMCP("test-data-generator")


@mcp.tool()
def generate_test_data(
    domain: str,
    count: int = 100,
    format: str = "json"
) -> str:
    """Generate synthetic test data for any domain with support for JSON, CSV, and SQL formats.
    
    Automatically saves the generated data locally and returns the file path.
    Supports common domains (employee, customer, business, product, transaction, iot)
    and can generate data for any custom domain.
    
    Args:
        domain: The domain/type of data to generate (e.g., 'employee', 'customer', 'business', or any custom domain)
        count: Number of records to generate (1-1000), defaults to 100
        format: Output format for the generated data: 'json', 'csv', or 'sql', defaults to 'json'
    
    Returns:
        A message with the file path and preview of the generated data
    """
    # Validate parameters
    if not domain or not domain.strip():
        return "Error: Domain parameter is required."
    
    domain = domain.strip()
    
    if count < 1 or count > 1000:
        return "Error: Count must be between 1 and 1000."
    
    format_type = format.lower()
    if format_type not in ["json", "csv", "sql"]:
        return f"Error: Unsupported format '{format}'. Use 'json', 'csv', or 'sql'."
    
    try:
        # Generate data
        data = generate_data(domain, count)
        
        # Save to file
        filepath = save_data(data, domain, format_type)
        
        # Create preview (first 3 records)
        preview_data = data[:3]
        preview = ""
        
        if format_type == "json":
            preview = json.dumps(preview_data, indent=2)
        elif format_type == "csv":
            preview = format_as_csv(preview_data)
        elif format_type == "sql":
            preview = format_as_sql(preview_data, domain)
        
        # Prepare response
        response = f"""Generated {count} {domain} records in {format_type.upper()} format!

File saved to: {filepath}

Preview:
{preview}

Dataset has been saved locally and is ready for use in your testing workflows."""
        
        return response
    
    except Exception as e:
        return f"Error generating test data: {str(e)}"


if __name__ == "__main__":
    mcp.run()