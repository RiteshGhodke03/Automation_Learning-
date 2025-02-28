import json

# Data to write
data = {
    "name": "Ritesh",
    "role": "Tester",
    "skills": ["Python", "Selenium", "SQL"]
}

# Writing to JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data written to JSON file successfully!")
