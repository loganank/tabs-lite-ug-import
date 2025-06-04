import csv
import json
import re

# Read CSV and extract tabId from URL
input_csv = 'tabs.csv'
entries = []

with open(input_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        url = row['URL']
        print(url)
        match = re.search(r'-([0-9]+)$', url)
        print(match)
        if match:
            tab_id = int(match.group(1))
            entries.append({
                "tabId": tab_id,
                "transpose": 0
            })

# Build JSON structure
output_data = {
    "playlists": [{
        "playlistId": -1,
        "title": "Favorites",
        "description": "",
        "userCreated": False,
        "entries": entries
    }]
}

# Write to JSON file
with open('tabs_lite_import.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(output_data, jsonfile, indent=4)

print("tabs_lite_import.json created successfully.")
