import argparse
import pandas as pd
import glob
import json
from sqlalchemy import create_engine



# parse argumentation
def parse():                          
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--source_dir', action='store', type=str, required=True)
    my_parser.add_argument('--mysql_info', action='store', type=str,required=True)
    my_parser.add_argument('--destination_table', action='store', type=str,required=True)


    args1= my_parser.parse_args()
    args2=my_parser.parse_args()
    args3=my_parser.parse_args()
    

    path1=args1.source_dir
    path2=args2.mysql_info
    path3=args3.destination_table
    
    return path1,path2,path3

path=parse()

# Mysql part
def mysql_connection(path):
    file=open(path)
    data = json.load(file)

    MYSQL_USER = data['user']
    MYSQL_PASSWORD= data['password']
    MYSQL_HOST_IP= data['ip']
    MYSQL_PORT= data['port']
    MYSQL_DATABASE= data['database']
    engine = create_engine('mysql+mysqlconnector://'+MYSQL_USER+':'+MYSQL_PASSWORD+'@'+MYSQL_HOST_IP+':'+MYSQL_PORT+'/'+MYSQL_DATABASE, echo=False)
    
    return engine

engine=mysql_connection(path[1]) #mysql_info path[1]

# Data
def data(path):
    all_files = glob.glob(path + "/*.json")
    li = list()
    for filename in all_files:
        df = pd.read_json(filename,orient='index')
        li.append(df)

    df= pd.concat(li,axis=1).T
    
    return df

df=data(path[0])  #source dir path[0]

# Create dataframe
df.to_sql(name=path[2], con=engine, if_exists='append', index=False)  #table_name path[2]





