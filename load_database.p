import sqlite3
import pandas as pd

# 1. Connect to SQLite database (this creates 'ecommerce.db' in the root folder)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# 2. Execute the schema setup script from the sql folder
with open('sql/01_schema_setup.sql', 'r') as f:
    schema_script = f.read()
cursor.executescript(schema_script)
print("Database schema created successfully from 01_schema_setup.sql!")

# 3. Load cleaned CSV files into the SQLite tables
df_regions = pd.read_csv('data/cleaned_regions.csv')
df_customers = pd.read_csv('data/cleaned_customers.csv')
df_products = pd.read_csv('data/cleaned_products.csv')
df_orders = pd.read_csv('data/cleaned_orders.csv')
df_order_items = pd.read_csv('data/cleaned_order_items.csv')

df_regions.to_sql('regions', conn, if_exists='append', index=False)
df_customers.to_sql('customers', conn, if_exists='append', index=False)
df_products.to_sql('products', conn, if_exists='append', index=False)
df_orders.to_sql('orders', conn, if_exists='append', index=False)
df_order_items.to_sql('order_items', conn, if_exists='append', index=False)

conn.commit()
print("All cleaned data successfully loaded into SQLite tables!")

# 4. Verify row counts
for table in ['regions', 'customers', 'products', 'orders', 'order_items']:
    cursor.execute(f"SELECT COUNT(*) FROM {table};")
    count = cursor.fetchone()[0]
    print(f"Table '{table}': {count} rows")

conn.close()