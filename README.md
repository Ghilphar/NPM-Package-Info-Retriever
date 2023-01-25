# README

This project is a Python script that utilizes the npm registry API (https://github.com/npm/registry/blob/master/docs/REGISTRY-API.md#objects) to retrieve information about a specified npm package. The script specifically retrieves the total number of downloads for the package since its creation.

The retrieved information is then organized and saved into a CSV file, which is encoded in ISO-8859-1 and uses the "|" character as a delimiter.

## Usage
To use the script, navigate to the directory where the script is located and run the following command:

```
python script.py <package_name>
```

Where `<package_name>` is the name of the npm package you wish to retrieve information for.

Please make sure that you have python3 installed.

## Dependencies
This script utilizes the following Python packages:
- requests
- pandas

You can install them using pip:

```
pip install requests pandas
```

## Contribution

This project is for educational purposes, and therefore it is not expected to be improved upon. However, if anyone is interested in contributing, feel free to fork the project and make a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
