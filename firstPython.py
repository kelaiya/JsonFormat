import json

def jsonOutput(data):
  entry = []
  mistake = []
  obj = {}
  f = open(data, "r")
  arr = f.read().split('\n')

  for i in range(len(arr)):
    crr = arr[i].split(', ')
    if len(crr) < 4:
      mistake.append(i)
    elif crr[2].find('(') != -1 and len(crr[2]) == 14 and len(crr[4]) == 5:
      entry.append({'firstName': crr[1], 'lastName': crr[0], 'color': crr[3], 'phone': crr[2], 'zipcode': crr[4] })
    elif len(crr) == 4 and len(crr[2]) == 5 and len(crr[3]) == 12 :
      spl = crr[0].split(' ')
      entry.append({'firstName': spl[0], 'lastName': spl[1], 'color': crr[1], 'phone': crr[3], 'zipcode': crr[2] })
    elif ord(crr[2][0]) < 58 and ord(crr[2][0]) > 47 and len(crr[2]) == 5 and len(crr[3]) == 12 :
      entry.append({'firstName': crr[0], 'lastName': crr[1], 'color': crr[4], 'phone': crr[3], 'zipcode': crr[2] })
    else:
      mistake.append(i)

  obj["entries"] = entry
  obj["errors"] = mistake
  f.close()
  sorted_obj = dict(obj) 
  sorted_obj["entries"] = sorted(obj['entries'], key=lambda x: x['lastName'], reverse=False) 
  jsonAns = json.dumps(sorted_obj, sort_keys=True, skipkeys=False, indent=2)
  return jsonAns

print(jsonOutput('data.in'))
  