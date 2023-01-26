# README

This script allows you to extract data from npm packages and save it to a CSV file.

This project is a Python script that utilizes the npm registry API (https://github.com/npm/registry/blob/master/docs/REGISTRY-API.md#objects) to retrieve information about a specified npm package. The script specifically retrieves the total number of downloads for the package since its creation.

The retrieved information is then organized and saved into a CSV file, which is encoded in ISO-8859-1 and uses the "|" character as a delimiter.

## Usage

1. Run the script using the command `python3 script.py package1 package2 package3` (replace package1, package2, package3 with the names of the packages you want to extract data from).

2. The script will extract the following data for each package:
    - name
    - description
    - license
    - latest version
    - author's name
    - author's email
    - total downloads from 2010-01-13 to today

3. The extracted data will be saved to two CSV files:
    - packageData.csv: contains data for each package in a separate row
    - packageData2.csv: contains all the data for all the packages in the same file

4. The script uses the npm API to get package data and the requests library to handle API calls. It also uses the csv library to write data to the CSV files and sys library to get the command line argument.

5. Each time the script runs, it will overwrite the existing CSV files.

## Dependencies
This script utilizes the following Python packages:
- requests

You will need to have these packages installed before running the script. You can install them using pip:
```
pip install requests
```

## Contribution

This project is for educational purposes, and therefore it is not expected to be improved upon. However, if anyone is interested in contributing, feel free to fork the project and make a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
