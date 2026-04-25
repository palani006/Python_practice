import json as n
json_txt='{"name":"palani","marks":[55,54,57,56,58]}'
data=n.loads(json_txt)
print(type(data))
print("marks")
print("name")

dict={"name":"palani","marks":[55,54,57,56,58],"roll":597}
json_std=n.dumps(dict)
print(type(json_std))
print(json_std)