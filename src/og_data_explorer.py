import pandas as pd
import json
import os
import kagglehub


def generate_data_dictionary():
    """Generate a summary dictionary for all columns in each table"""
    # Download the data
    path = kagglehub.dataset_download("shalakagangurde/hospital-hmis-dataset-for-healthcare-analytics")

    # Kaggle downloads your file in a hidden cache folder on your laptop. THe code below is drilling down from the root and extracting all the files than end with a .csv
    csv_files = []

    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('csv'):
                csv_files.append(os.path.join(root,f))


    #We want to to get the dtype, null percentage, cardinality, and the date range (if applicable for each column)
    # I decided to use a loop to extract each of these details, store them in a dictionary, then dump them in a json and a csv

    details = {}

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        table_name = os.path.splitext(os.path.basename(csv_file))[0]

        columns = df.columns.to_list()

        details[table_name] = {}


        for column in columns:

            # Add types
            dtype_val = str(df.dtypes[column])
            null_pct = float(df[column].isnull().mean() * 100)
            cardinality = df[column].nunique()

            # check if the columns have a date columns
            # can first check the type, and then check if a column has the word date
            date_range = None
            if 'date' in column.lower() or dtype_val == 'datetime':
                column_to_datetime = pd.to_datetime(df[column])
                min_date = column_to_datetime.min()
                max_date = column_to_datetime.max()
                date_range = (str(min_date), str(max_date))
            details[table_name][column]= {
                "dtype": dtype_val,
                "null_pct": null_pct,
                "cardinality": cardinality,
                "date_range": date_range
            }


    # Save dictionary as a csv
    rows = []
    for table_name, columns in details.items():
        for column_name, column_info in columns.items():
            rows.append({
                'table': table_name,
                'column': column_name,
                'dtype': column_info['dtype'],
                'null_pct': column_info['null_pct'],
                'cardinality': column_info['cardinality'],
                'date_range': column_info['date_range']
            })

    df_summary = pd.DataFrame(rows)
    df_summary.to_csv('../data/raw/data_dictionary_summary.csv', index=False)

    # Saved to json
    with open('../data/raw/data_dictionary_summary.json', 'w') as f:
        json.dump(details, f, indent=2, default=str)