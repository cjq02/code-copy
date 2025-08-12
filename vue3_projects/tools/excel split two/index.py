import pandas as pd
import os
from datetime import datetime
import uuid

# Function to generate UUID without hyphens
def generate_uuid():
    return uuid.uuid4().hex

# Function to pad codes
def pad_code(code, length):
    return str(code).zfill(length)

# Define the input file path
input_file = os.path.abspath('excel.xlsx')

# Check if the file exists
if not os.path.exists(input_file):
    print(f"File not found: {input_file}")
else:
    # Read the Excel file using the openpyxl engine
    df = pd.read_excel(input_file, engine='openpyxl')

    # Pad the country_code and city_code
    df['country_code'] = df['country_code'].apply(pad_code, length=3)
    df['city_code'] = df['city_code'].apply(pad_code, length=6)

    # Create the country DataFrame and remove duplicates
    country_df = df[['country_code', 'country_name']].drop_duplicates().reset_index(drop=True)
    country_df.insert(0, 'id', [generate_uuid() for _ in range(len(country_df))])

    # Create the city DataFrame
    city_df = df[['country_code', 'city_code', 'city_name']].reset_index(drop=True)
    city_df.insert(0, 'id', [generate_uuid() for _ in range(len(city_df))])

    # Generate the output file names with the current timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    country_output_file = f"country_{timestamp}.xlsx"
    city_output_file = f"city_{timestamp}.xlsx"

    # Save the DataFrames to Excel files
    with pd.ExcelWriter(country_output_file, engine='openpyxl') as writer:
        country_df.to_excel(writer, index=False, sheet_name='Country')

    with pd.ExcelWriter(city_output_file, engine='openpyxl') as writer:
        city_df.to_excel(writer, index=False, sheet_name='City')

    print(f"Country data has been written to {country_output_file}")
    print(f"City data has been written to {city_output_file}")
