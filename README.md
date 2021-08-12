# ECL_Solution
**Introduction** :
This tool is designed to parse a given input file and aggregate the records based on the associated score in descending order. The job accepts two arguments, a filename and number of top N records to be displayed. 

**Using the Tool** :
python3 Solution.py filename num_of_records
Expected output is an array of json objects with id and associated score.


**Validations Performed by the tool**:
1) Number of command line arguments should be exactly two. Else the job exits with appropriate error message.
2) Filename passed should exist and be accessible to the job. Otherwise, the job exits with status code 2.
3) Number of records should be a valid number.
4) Number of records cannot be greater than total number of valid lines in the file. 
5) Blank lined will be ignored.
6) if there are any data that does not confirm to the structure of key value pair, then the job exits.
7) if a line does not start with a number, then the tool assumes that the data in the file is not in the right format and exits. (It can be changed to skip the erroneous lines only )
8) If the value in each line is not a proper json object then the job exits with status code 1.
9) If the value is valid json but it does not have a key named "id" then the job exits with status code 1.

**DESIGN DECISIONS** :
1) The underlying script is written in python3.
2) It is assumed that the score value is unique (as no logic is provided on how to sort two records with same score. This can be changed if necessary)
3) Priority Queue algorithm is used to reduce the memory footprint. Only N number of records that are required in the output are stored in the memory at any given point of time.
4) File is parsed line by line so that only one line of file resides in the memory. 
