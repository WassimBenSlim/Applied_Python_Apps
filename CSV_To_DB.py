import sqlite3
import pandas as pd

#SQLite database connection 
new_connection = sqlite3.connect(r'PythonApps\demo5.db')

#Loading data into Dataframe
demo_data = pd.read_csv(r'PythonApps\demo5.csv')

#write the data to a sqlite table
demo_data.to_sql('demo5', new_connection, if_exists = 'replace', index= False)


#close connection to sqlite database
new_connection.close()