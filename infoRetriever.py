import requests
import pandas as pd
import json
import csv


package_name = "express"
url = f"https://registry.npmjs.org/{package_name}"
response = requests.get(url)

data = response.json()

packageData = {}
packageData["name"] = data["name"]
packageData["description"] = data["description"]
packageData["license"] = data["license"]
packageData["latest_version"] = data["dist-tags"]["latest"]
packageData["author_name"] = data["versions"][data["dist-tags"]["latest"]]["author"]["name"]
packageData["author_email"] = data["versions"][data["dist-tags"]["latest"]]["author"]["email"]

# Create the DataFrame
df = pd.DataFrame(packageData, index=[0])

# Write the DataFrame to a CSV file
df.to_csv("packageData.csv", sep='|', encoding='ISO-8859-1')

#with open("packageData.csv", 'w', newline='') as file:
#    writer = csv.DictWriter(file, fieldnames=packageData.keys())
#    writer.writeheader()
#    writer.writerow(packageData)


#with open("package_data.json", "w") as outfile:
#    json.dump(packageData, outfile)

#print(data)

#json_string = json.dumps(packageData)


#data_frame = pd.DataFrame.from_dict(packageData)
#print(data_frame)

#data_frame.to_csv("package_data.csv", sep='|', encoding='ISO-8859-1')
