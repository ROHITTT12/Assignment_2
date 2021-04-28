import argparse
import pandas as pd
import glob
import json
from sqlalchemy import create_engine

# Data
def get_data(sorce_dir):

    all_files = glob.glob(sorce_dir + "/*.json")
    li = list()
    for filename in all_files:
        df = pd.read_json(filename,orient='index')
        li.append(df)
    df= pd.concat(li,axis=1).T
    return df
    
    
# Mysql part
def mysql_connection(mysql_info_path,table_name,df):

    file_path=open(mysql_info_path)
    data = json.load(file_path)
    MYSQL_USER = data['user']
    MYSQL_PASSWORD= data['password']
    MYSQL_HOST_IP= data['ip']
    MYSQL_PORT= data['port']
    MYSQL_DATABASE= data['database']
    engine = create_engine('mysql+mysqlconnector://'+MYSQL_USER+':'+MYSQL_PASSWORD+'@'+MYSQL_HOST_IP+':'+MYSQL_PORT+'/'+MYSQL_DATABASE, echo=False)

    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)  #table_name path[2]


if __name__ == "__main__":
    pass