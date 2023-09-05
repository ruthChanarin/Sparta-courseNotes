import json

# dump(s) turn Python dict into JSON - json dump() writes to file & dumps() help writes JSON (a P string)
# json load() works with files and loads() with strings to turn into Python dicts

course = {"name":"Data 249","trainer":"Paula"}

print(type(course))
print(course)

# prints type as dict

course_json_str = json.dumps(course)
print(type(course_json_str))
print(course_json_str)

# now prints type as a string, but still looks similar 

# json.dump() takes two parameters: content in dict form, and filename

with open("new_json_data.json", "w") as jsonfile:
    json.dump(course, jsonfile)

# load() used to read json file as python dict

with open("new_json_data.json") as jsonfile: 
    course_file = json.load(jsonfile)
    print(course_file)
    print(type(course_file))