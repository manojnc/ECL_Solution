import heapq as heap
import os.path
import os
import sys
import json
from json.decoder import JSONDecodeError
import re

class solution():

    def __init__(self,filename,num_records):
        self.filename=filename
        self.num_records=int(num_records)
        self.counter=0
        self.heaparray=[]

    def parse_file(self):
        res={}
        line_count=0

        with open(self.filename,"r") as infile:
            for row in infile:
                if row.rstrip():                                            # skipping the empty lines 
                    try:
                        line_count+=1
                        match=re.match(r'^(\d+):?(\s+)?(.*)?',row)          # matching the pattern NUM : VAL
                        if match == None:
                            print("Unexpected content in the file")
                            os._exit(1)
                        score=int(match.group(1))
                        exp_json=json.loads(match.group(3))

                        if not(isinstance(exp_json,dict)):
                            os._exit(1)
                        if exp_json.get('id',None) is None:                 # validate for id key
                            os._exit(1)

                        uid=exp_json.get('id')

                        if self.counter < self.num_records:                 # set up the heap array initially with N number of records requested
                            heap.heappush(self.heaparray,score)
                            res[score]=uid                                  # set up the result json onbject with score and associated id
                            self.counter+=1
                            continue

                        if score > self.heaparray[0]:                       # if any subsequent elements are having higer score, replace the smallest element from heap with the new element
                            popped_ele=heap.heappushpop(self.heaparray,score)
                            res.pop(popped_ele)                             # remove the smaller scores and replace it with higher score key vale pair
                            res[score]=uid
                           
                    except JSONDecodeError:                                 # validate if the value is not a valid json object 
                        print("bad json input in the file")
                        os._exit(1)

                    except Exception as e:
                        print(str(e))
                        continue
        if self.num_records > line_count:                                   # number of records requested cannot exeed number of lines in the file
            sys.exit("Number of records requested is greater than total number of valid lines in the file")
        return res

def validate(args):
    if len(args) != 3:
        sys.exit("Required number of arguments not matching")

    if(not(os.path.isfile(args[1]))):
        print("file not found")
        os._exit(2)

    try:
        int(args[2])
    except ValueError:
        sys.exit("invalid input for number of records")



def main():
    validate(sys.argv)
    s = solution(sys.argv[1],sys.argv[2])
    res=s.parse_file()
    arr=[]
    for i in sorted(res,reverse=True):
        arr.append({"score":i,"id":res[i]})

    print(arr)
    

if __name__ == "__main__":
    main()


