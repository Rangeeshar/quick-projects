# This is a sample Python script.
# CSV containing ->
# IP address , Country, Region Name, City
import requests
import json
import csv


def external_api(ipadress):
    """
    Makes external APi call
    """
    url = "http://ip-api.com/json/{}".format(ipadress)
    response = requests.get(url)
    if response.ok:
        data = json.loads(response.text)
        if data.get("status") != "fail":
            return data
    print("Failed/Not Found for the IPaddress:  {}, {}".format(url, response.text))
    return {}


def write_to_csv(batch, file_name="output.csv"):
    """
    Takes input batch and writes a csv file
    """
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=batch[0].keys())
        writer.writeheader()
        writer.writerows(batch)


def main(path_of_file):
    """
    Takes path of file as input
    Return: CSV file with specific columns
    """
    batch = []
    with open(path_of_file, 'r') as file_object:
        for line in file_object.readlines():
            print(line.strip())
            resp_data = external_api(line.strip())
            template = {
                "ipaddress": line.strip(),
                "country": resp_data.get("country"),
                "region_name": resp_data.get("region"),
                "city": resp_data.get("city")
            }
            batch.append(template)
    write_to_csv(batch)


if __name__ == '__main__':
    path_of_file_txt = "sample.txt"
    main(path_of_file_txt)
