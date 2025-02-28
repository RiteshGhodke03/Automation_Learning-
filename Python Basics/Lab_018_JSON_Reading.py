import json

# Reading from JSON file
with open("data.json", "r") as file:
    content = json.load(file)

print(content)  # Output: {'name': 'Ritesh', 'role': 'Tester', 'skills': ['Python', 'Selenium', 'SQL']}
print(content["name"])  # Output: Ritesh
