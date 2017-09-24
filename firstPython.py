import json

def jsonOutput(data):

  # solution can be seen on: https://github.com/kelaiya/JsonFormat
  
  # obj is python object storing the data 
  obj = {}
  f = open(data, "r")

  # arr is the array of strings
  arr = f.read().split('\n')
  
  # obj will have 2 key-value pairs. One will be "entries" and other will be "errors"
  # checkData is a function which will check data and return the data in two groups
  # if the data is valid, it will go to entries section of obj and if it is invalid, it will go to errors section of obj 
  [obj["entries"], obj["errors"]] = checkData(arr)
  f.close()

  # stored_obj is an object stored by lastname
  sorted_obj = dict(obj) 
  sorted_obj["entries"] = sorted(obj['entries'], key=lambda x: x['lastname'], reverse=False) 

  # jsonAns is the Json format of sorted_obj 
  jsonAns = json.dumps(sorted_obj, sort_keys=True, indent=2)
  return jsonAns


def checkData(arr):

  # entry array is for entries list in Json format 
  # mistake array is for errors list in Json format
  entry = []
  mistake = []

  # there are 3 types of format which are valid so there are 3 if conditions to check the string and if the string length is less than 4 then consider it as invalid string in the loop
  for i in range(len(arr)):
    dataInfo = arr[i].split(', ')
    
    if len(dataInfo) < 4:
      mistake.append(i)

    elif dataInfo[2].find('(') != -1 and len(dataInfo[2]) == 14 and len(dataInfo[4]) == 5:

      # if we don't want brackets("()") and dashes("-") in the phonenumber than execute the below command:
      # dataInfo[2] = dataInfo[2].replace("(","").replace(")","").replace("-"," ")
      entry.append({'firstname': dataInfo[1], 'lastname': dataInfo[0], 'color': dataInfo[3], 'phonenumber': dataInfo[2], 'zipcode': dataInfo[4] })
    
    elif len(dataInfo) == 4 and len(dataInfo[2]) == 5 and len(dataInfo[3]) == 12 :
      nameInfo = dataInfo[0].split(' ')
      entry.append({'firstname': nameInfo[0], 'lastname': nameInfo[1], 'color': dataInfo[1], 'phonenumber': dataInfo[3], 'zipcode': dataInfo[2] })
    
    elif ord(dataInfo[2][0]) < 58 and ord(dataInfo[2][0]) > 47 and len(dataInfo[2]) == 5 and len(dataInfo[3]) == 12 :
      entry.append({'firstname': dataInfo[0], 'lastname': dataInfo[1], 'color': dataInfo[4], 'phonenumber': dataInfo[3], 'zipcode': dataInfo[2] })
    
    else:
      mistake.append(i)

  return [entry, mistake] 


print(jsonOutput('data.in'))
  