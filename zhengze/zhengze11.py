import json

json_str = '{"name": "qiyue", "age": 18}'

student = json.loads(json_str)
print(student)
print('Student\'s name is ' +  str(student['name']))
print('Student\'s age is ' +  str(student['age']))

