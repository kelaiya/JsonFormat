# # def data(arr):
# #   d = {}
# #   brr = []
# #   obj = {}
# #   for x in arr:
# #     d["First_name"] = x[0]
# #     d["Last_name"] = x[1]
# #     d["Zip-Code"] = x[2]
# #     brr.append(d)
# #   obj["entries"] = brr
# #   return obj
  
# # print(data([["kel","pr",123],["vis","pr",1234]]))
# def kelFirst():
#   d = {}
#   drr = []
#   ans = []
#   obj = {}
#   f = open('data.in', "r")
#   message = f.read()
#   arr = message.split('\n');
#   # print(arr)
#   for i in range(len(arr)):
#     print("hey")
#     crr = arr[i].split(', ')
#     print(len(crr))
#     if len(crr) < 4:
#       ans.append(i)
#     elif crr[2].find('(') != -1 and len(crr[2]) == 12 and len(crr[4]) == 5:
#         # d["firstName"] = crr[1]
#         # d["lastName"] = crr[0]
#         # d["zipCode"] = crr[4]
#         # d["phone"] = crr[2]
#         # d["color"] = crr[3]
#         # print(d)
#         print('inside')
#         drr.append({'firstName': crr[1], 'color': crr[3], 'lastName': crr[0], 'phone': crr[2], 'zipcode': crr[4] })
#         print(drr)
#     elif len(crr) == 4 and ord(crr[2][0]) < 58 and ord(crr[2][0]) > 47 and len(crr[2]) == 5 and len(crr[3]) == 12 :
#       spl = crr[0].split(' ')
#       drr.append({'firstName': spl[0], 'color': crr[1], 'lastName': spl[1], 'phone': crr[3], 'zipcode': crr[2] })
#     elif ord(crr[2][0]) < 58 and ord(crr[2][0]) > 47 and len(crr[2]) == 5 and len(crr[3]) == 12 :
#       print("I am still here")
#       # d["firstName"] = crr[0]
#       # d["lastName"] = crr[1]
#       # d["zipCode"] = crr[2]
#       # d["phone"] = crr[3]
#       # d["color"] = crr[4]
#       # print(d)
#       print('inside')
#       drr.append({'firstName': crr[0], 'color': crr[4], 'lastName': crr[1], 'phone': crr[3], 'zipcode': crr[2] })
#       print(drr)
#     elif len(crr[3]) == 5 and len(crr[4]) == 12:
#       print("I am still here")  
#       # d["firstName"] = crr[0]
#       # d["lastName"] = crr[1]
#       # d["zipCode"] = crr[3]
#       # d["phone"] = crr[4]
#       # d["color"] = crr[2]
#       # print(d)
#       print('inside')
#       drr.append({'firstName': crr[0], 'color': crr[2], 'lastName': crr[1], 'phone': crr[4], 'zipcode': crr[3] })
#       print(drr)
#     else:
#       ans.append(i)
#   obj["entries"] = drr
#   obj["errors"] = ans
#   # print(obj)
#   f.close()
#   return (obj) 

# print(kelFirst())
  


  def kelFirst(data):
  entry = []
  mistake = []
  obj = {}
  f = open(data, "r")
  message = f.read()
  arr = message.split('\n');
  for i in range(len(arr)):
    crr = arr[i].split(', ')
    if len(crr) < 4:
      mistake.append(i)
    elif crr[2].find('(') != -1 and len(crr[2]) == 12 and len(crr[4]) == 5:
      entry.append({'firstName': crr[1], 'color': crr[3], 'lastName': crr[0], 'phone': crr[2], 'zipcode': crr[4] })
    elif len(crr) == 4 and ord(crr[2][0]) < 58 and ord(crr[2][0]) > 47 and len(crr[2]) == 5 and len(crr[3]) == 12 :
      spl = crr[0].split(' ')
      entry.append({'firstName': spl[0], 'color': crr[1], 'lastName': spl[1], 'phone': crr[3], 'zipcode': crr[2] })
    elif ord(crr[2][0]) < 58 and ord(crr[2][0]) > 47 and len(crr[2]) == 5 and len(crr[3]) == 12 :
      entry.append({'firstName': crr[0], 'color': crr[4], 'lastName': crr[1], 'phone': crr[3], 'zipcode': crr[2] })
    elif len(crr[3]) == 5 and len(crr[4]) == 12:
      entry.append({'firstName': crr[0], 'color': crr[2], 'lastName': crr[1], 'phone': crr[4], 'zipcode': crr[3] })
    else:
      mistake.append(i)
  obj["entries"] = entry
  obj["errors"] = mistake
  f.close()
  # print(type(obj))
  # correctAns = json.dumps(obj, sort_keys=True, skipkeys=False, indent=2)
  # print(type(correctAns))
  # newObj = json.loads(correctAns)
  sorted_obj = dict(obj) 
  sorted_obj["entries"] = sorted(obj['entries'], key=lambda x: x['lastName'], reverse=False) 
  # print(sorted_obj)
  print(json.dumps(sorted_obj, sort_keys=True, skipkeys=False, indent=2))
  # print(correctAns)
  # return correctAns
print(kelFirst('data.in'))
  