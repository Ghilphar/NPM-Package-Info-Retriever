import requests
import csv
from datetime import datetime
import sys

packageNumber = 1
numberOfPackage = len(sys.argv)

#Create the list for the csv2
MyList = []

# Create the fieldnames and the csv
fieldnames = ["name", "downloads","description", "license", "latest_version", "author_name", "author_email"]
with open("packageData.csv", 'w', newline='', encoding='ISO-8859-1') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
    csvwriter.writeheader()

while (packageNumber < numberOfPackage):
    package_name = sys.argv[packageNumber]
    packageNumber += 1
    #Get all the downloads of a package
    dateCreationOfNpm = "2010-01-13"
    dateStart = datetime.today().strftime('%Y-%m-%d')
    dateEnd = dateCreationOfNpm
    downloads = 0

    while (dateEnd != dateStart):
        url = f"https://api.npmjs.org/downloads/point/{dateCreationOfNpm}:{dateStart}/{package_name}"
        responseDownloads = requests.get(url)
        dataDownloads = responseDownloads.json()
        print(dataDownloads)
        downloads += dataDownloads["downloads"]
        dateStart = dataDownloads["start"]
        dateEnd = dataDownloads["end"]

    #Get the info of the package
    url = f"https://registry.npmjs.org/{package_name}"
    response = requests.get(url)
    data = response.json()

    #Create the dictionary for the csv
    packageData = {}
    author = data["versions"][data["dist-tags"]["latest"]].get("author", {})
    packageData["name"] = data["name"]
    packageData["description"] = data["description"]
    packageData["license"] = data["license"]
    packageData["latest_version"] = data["dist-tags"]["latest"]
    packageData["author_name"] = author.get("name", "N/A")
    packageData["author_email"] = author.get("email", "N/A")
    packageData["downloads"] = downloads

    print(packageData)

    #Add the dictionary to the list of the csv2
    MyList.append(packageData)
    #Create a list to add it to the csv1
    rows = [packageData]

    # Open the file and write the data using the csv module
    with open("packageData.csv", 'a', newline='', encoding='ISO-8859-1') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
        csvwriter.writerows(rows)

with open("packageData2.csv", 'w', newline='', encoding='ISO-8859-1') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
    csvwriter.writeheader()
    csvwriter.writerows(MyList)

#This is the end of the project We show 2 ways of create a csv file with the data we extracted.
#Author: FGaribot