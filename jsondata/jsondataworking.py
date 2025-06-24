import json
#
# # serialization : convert dictionary to json
# # dumps()
data = {
    'username': 'sanket',
    'contact': 123456,
    'isAdmin': True
}
jsondata= json.dumps(data)
print(jsondata)

# # pydata=json.loads(jsondata)
# # print(pydata)
# # json.load(data,'sample.txt')
# with open('sample.json','w') as file:
#     json.dump(data,file)
#
#
# import json
#
# with open('sample.json', 'r') as file:
#     pydata = json.load(file)
#
#     # loaded_data = json.load(pydata)
#
# content = json.dumps(pydata)
# print(content)