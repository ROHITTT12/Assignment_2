# Assignment_2
Python Assignment

Install a Python IDE (Anyone will do)
Visual Studio Code
PyCharm
Note: If you’re used to some other IDE that’s also fine just make sure you have all the best practices set as per the next section.

Go through python best practices.
https://data-flair.training/blogs/python-best-practices/ 
pep8 is python standard: https://www.python.org/dev/peps/pep-0008/
Any editor you choose will have a pep8 checker search on how to enable that for your editor. Eg: for visual studio: https://code.visualstudio.com/docs/python/linting#:~:text=Enable%20linters%23,name%20of%20the%20chosen%20linter.
 
Post going through best practices, we ask them to perform the following assignment with best practices followed.
 
Implement a file upload utility with the functionality expected below,
Prerequisites,
Install MySQL
Get an understanding of how to handle JSON in python.
Get an understanding of Pandas in python.
Get an understanding of MySQL connection in python.
Use 'argparse' for argument parsing.

Name of utility : file_upload.py

What is it supposed to do?

Whenever the above utility is executed with necessary arguments it will take a directory as an argument, and read all files from the directory, and upload them to the corresponding MySQL table specified in config.

Arguments

--source_dir <Source directory from which we need to read all files to upload to mysql>
  
--mysql_details <Path of a JSON file which contains all details of MySQL to which to connect to>
  
JSON file contents,
{
"mysql_ip": "127.0.0.1",
"port" : "3306",
"username" : "<appropriate username>",
"password" : "<password",
< any other field required for connection >
}
  
--destination_table <Name of table to upload this data to>
Processing,
  
Create MySQL connection

Read JSON file and create MySQL conn object.

List files from <source_dir>
  
Iterate through these files one by one.
  
Read each csv file into pandas dataframe.
  
Load pandas dataframe to mysql.

