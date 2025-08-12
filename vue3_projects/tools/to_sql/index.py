import pandas as pd
import os

# Function to generate UUID without hyphens
import uuid
def generate_uuid():
    return uuid.uuid4().hex

# Function to pad codes
def pad_code(code, length):
    return str(code).zfill(length)

# Define the input file paths
city_file = os.path.abspath('city.xlsx')
country_file = os.path.abspath('country.xlsx')

# Check if the files exist
if not os.path.exists(city_file):
    print(f"File not found: {city_file}")
if not os.path.exists(country_file):
    print(f"File not found: {country_file}")

if os.path.exists(city_file) and os.path.exists(country_file):
    # Read the Excel files using the openpyxl engine
    city_df = pd.read_excel(city_file, engine='openpyxl')
    country_df = pd.read_excel(country_file, engine='openpyxl')

    # Pad the country_code and city_code
    city_df['country_code'] = city_df['country_code'].apply(pad_code, length=3)
    city_df['city_code'] = city_df['city_code'].apply(pad_code, length=6)
    country_df['country_code'] = country_df['country_code'].apply(pad_code, length=3)

    # Generate PostgreSQL INSERT statements for country
    country_inserts = []
    for _, row in country_df.iterrows():
        country_inserts.append(
            f"INSERT INTO t_jj_sys_country (id, country_code, country_name) VALUES ('{row['id']}', '{row['country_code']}', '{row['country_name']}');"
        )

    # Generate PostgreSQL INSERT statements for city
    city_inserts = []
    for _, row in city_df.iterrows():
        city_inserts.append(
            f"INSERT INTO t_jj_sys_city (id, country_code, city_code, city_name) VALUES ('{row['id']}', '{row['country_code']}', '{row['city_code']}', '{row['city_name']}');"
        )

    # Print the generated SQL statements
    print("\n".join(country_inserts))
    print("\n".join(city_inserts))
