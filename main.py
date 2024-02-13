import json
import requests

def main():
    compareLocations()

def compareLocations():
    #issLatitude, issLongitude = getIssLocation()
    print(getIssLocation())

def getIssLocation():
    response = requests.get("http://api.open-notify.org/iss-now.json")

    if response.status_code == 200:
        data = response.json()
        issLatitude = float(data['iss_position']['latitude'])
        issLongitude = float(data['iss_position']['longitude'])
        return(issLatitude, issLongitude)
    else:
        print("Failed to fetch ISS position:", response.status_code)

if __name__ == "__main__":
    main()
