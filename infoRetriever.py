import requests
import csv
from datetime import datetime, timedelta
import sys

def get_package_downloads(package_name):
    dateCreationOfNpm = "2010-01-13"
    date = datetime.today().strftime('%Y-%m-%d')
    downloads = 0

    while (date != "2015-01-10"):
        try:
            url = f"https://api.npmjs.org/downloads/point/{dateCreationOfNpm}:{date}/{package_name}"
            responseDownloads = requests.get(url)
            dataDownloads = responseDownloads.json()
            downloads += dataDownloads["downloads"]
            date = (datetime.strptime(dataDownloads["start"], '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
        except:
            print(f'An error occurred when trying to get downloads for package {package_name}.')
            downloads = f'An error occurred when trying to get downloads for package {package_name}.'
            break
    return downloads

def get_package_data(package_name):
    try:
        url = f"https://registry.npmjs.org/{package_name}"
        response = requests.get(url)
        data = response.json()

        packageData = {}
        author = data["versions"][data["dist-tags"]["latest"]].get("author")
        packageData["name"] = data.get("name", "N/A")
        packageData["description"] = data.get("description", "N/A")
        packageData["license"] = data.get("license")
        packageData["latest_version"] = data.get("dist-tags").get("latest")
        if (type(author) == "dict"):
            packageData["author_name"] = author.get("name", "N/A")
            packageData["author_email"] = author.get("email", "N/A")
        else:
            packageData["author_name"] = "N/A"
            packageData["author_email"] = "N/A"
        packageData["downloads"] = get_package_downloads(package_name)
    except:
        packageData = {
            "name": "package_name",
            "description": "An error occurred when trying to download the data."
            }
    return packageData

def write_to_csv(package_data, filename):
    fieldnames = ["name", "downloads","description", "license", "latest_version", "author_name", "author_email"]
    with open(filename, 'w', newline='', encoding='ISO-8859-1') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
        csvwriter.writeheader()
        csvwriter.writerows(package_data)

def main():
    try:
        packageNumber = 1
        numberOfPackage = len(sys.argv)

        #Create the list for the csv2
        myList = []

        while (packageNumber < numberOfPackage):
            package_name = sys.argv[packageNumber]
            packageNumber += 1
            package_data = get_package_data(package_name)
            myList.append(package_data)

        write_to_csv(myList, "packageData.csv")
    except:
        print("Something went wrong.")

#Author: FGaribot
if __name__ == "__main__":
    main()