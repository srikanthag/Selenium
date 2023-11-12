from requests import request
import json
import csv

def read_csv():
    data = []
    with open('./data_files/bank.csv') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            data.append((row[0], row[1]))
    return data

codes = read_csv()

for code in codes:
    ifsc_code, expected_branch = code
    url = f"https://ifsc.razorpay.com/{ifsc_code}"
    response = request("GET", url)
    
    print(f"Hitting the URL: {url}")

    # De-Serilisation   (Converting JSON str into a Python Object is called as de-serilization)
    data = json.loads(response.text)

    try:
        assert data['BRANCH'] == expected_branch
        print(f"actual branch: {data['BRANCH']} and expected branch: {expected_branch}")
    except AssertionError:
        print(f"The expected branch is {expected_branch} and the actual received from WS is {data['BRANCH']}")











