"""
##################################################################################
Script Name: bq-schema-comparator
Author: Kemal Cholovich
Date: 2023-05-30
License information: MIT
##################################################################################
"""

from google.cloud import bigquery
# Create a client instance
client = bigquery.Client()

# Get the table schema fn
def get_table_schema(project_id, dataset_id, table_id):
    table_ref = client.dataset(dataset_id, project=project_id).table(table_id)
    table = client.get_table(table_ref)
    return table.schema

# Define the table names
table1_name = 'events'
table2_name = 'events'
table3_name = 'events'

# Retrieve the schemas of the tables
table1_schema = get_table_schema('project-saas', 'dw1_pubsub', table1_name)
table2_schema = get_table_schema('project-saas', 'dw2_pubsub', table2_name)
table3_schema = get_table_schema('project-saas', 'dw1_pubsub', table3_name)

# Compare the schemas field by field
# You can write your own comparison logic here based on your requirements
if table1_schema == table2_schema and table2_schema == table3_schema:
    print("All table schemas are identical.")
    #print the scema content
    print(table1_schema)
else:
    print("Table schemas have differences.")

