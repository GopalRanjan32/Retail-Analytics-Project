import pandas as pd
from sqlalchemy import create_engine

# CSV load (updated path)
df = pd.read_csv("C:/Users/ranja/OneDrive/Desktop/Retail-Analytics-Project/excel/cleaned_superstore.csv")

# MySQL connection (password replace karna)
engine = create_engine("mysql+pymysql://root:Gopal%40123@localhost/retail_project")

# Upload to SQL
df.to_sql("sales_data", con=engine, if_exists="replace", index=False)

print("Data imported successfully!")