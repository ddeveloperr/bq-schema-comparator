# bq-schema-comparator
Compare the schemas between many BigQuery tables

## Description (The problem)
We have multiple datasets in BigQuery that receive data from various sources, such as AWS and GCP. These datasets have identical table names. How can we efficiently check the schemas of these tables in a short period of time without manual intervention?

This script retrieves the schemas of many tables using the get_table_schema() function and then compares the schemas using a simple equality check. 
You can copy, modify, fork the comparison logic based on your specific requirements!

By running this Python script, you can check and compare the schema of three BigQuery SQL tables and identify any differences or similarities.

## Solution
To check and compare the schema of many BigQuery SQL tables using a Python script, we can utilize the BigQuery Python client library. 

Here's an example of how we can achieve this using one simple script.

## Usage 
### Here's an example of how you can achieve this:

1. Install the `google-cloud-bigquery` library by running the following command:
```
pip install google-cloud-bigquery
```
2. Import the necessary modules in your Python script:
```
from google.cloud import bigquery
```
3. Set up the BigQuery client:
```
# Create a client instance
client = bigquery.Client()
```
4. Define a function to retrieve the schema of a table:
```
def get_table_schema(project_id, dataset_id, table_id):
    table_ref = client.dataset(dataset_id, project=project_id).table(table_id)
    table = client.get_table(table_ref)
    return table.schema
```
5. Compare the schemas of the three tables:
```
# Define the table names
table1_name = 'table1'
table2_name = 'table2'
table3_name = 'table3'

# Retrieve the schemas of the tables
table1_schema = get_table_schema('project_id', 'dataset_id', table1_name)
table2_schema = get_table_schema('project_id', 'dataset_id', table2_name)
tableN_schema = get_table_schema('project_id', 'dataset_id', tableN_name)

# Compare the schemas field by field
# You can write your own comparison logic here based on your requirements
if table1_schema == table2_schema and table2_schema == tableN_schema:
    print("All table schemas are identical.")
    print(table1_schema) # To see the schema in details!
else:
    print("Table schemas have differences.")
```

## Double Check!
* Make sure to replace 'project_id' and 'dataset_id' with your actual project and dataset IDs.
* Adjust the table names (table1_name, table2_name, tableN_name) as per your table names.

## The MIT License (MIT)

Copyright (c) <2023> Kemal Cholovic
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


