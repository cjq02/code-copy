import pandas as pd
import os
import uuid
from datetime import datetime

# Define the input file path
input_file = os.path.abspath('input.xlsx')

# Check if the file exists
if not os.path.exists(input_file):
    print(f"File not found: {input_file}")
else:
    # Read the Excel file using the openpyxl engine
    df = pd.read_excel(input_file, engine='openpyxl')

    # Replace empty city_name cells with "所有城市"
    df['city_name'].fillna('所有城市', inplace=True)

    # Ensure country_code is a string of length 3, padding with zeros if necessary
    df['country_code'] = df['country_code'].apply(lambda x: str(x).zfill(3))

    # Generate city_code based on the conditions
    def generate_city_code(row):
        if row['city_name'] == "其他城市":
            return f"{row['country_code']}999"
        else:
            count = row['city_count']
            return f"{row['country_code']}{str(count).zfill(3)}"

    # Group by country_code and generate city_code
    df['city_count'] = df.groupby('country_code').cumcount() + 1
    df['city_code'] = df.apply(generate_city_code, axis=1)

    # Drop the temporary city_count column
    df.drop(columns=['city_count'], inplace=True)

    # Generate UUIDs without hyphens and add as the first column
    df.insert(0, 'id', df.apply(lambda _: str(uuid.uuid4()).replace('-', ''), axis=1))

    # Delete the second column
    df.drop(df.columns[1], axis=1, inplace=True)

    # Generate the output file name with the current timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_file = f"output{timestamp}.xlsx"

    # Write the modified data to a new Excel file
    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Modified data has been written to {output_file}")
