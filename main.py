import file_upload as task
import argparse
import pandas as pd




def Driver(source_dir,mysql_info,table_name):

   df=task.get_data(source_dir)
   task.mysql_connection(mysql_info,table_name,df)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_dir', type=str, required=True)
    parser.add_argument('--mysql_info',type=str,required=True)
    parser.add_argument('--destination_table',type=str,required=True)
    
    args=parser.parse_args()
     
    Driver(args.source_dir,args.mysql_info,args.destination_table)