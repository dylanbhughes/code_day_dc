import requests

# We're making a request to the DCGIS Open API for some data about parking tickets
response = requests.get(
    url="https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_APPS/SR_30days_Open/MapServer/8/query?where=1%3D1&outFields=*&outSR=4326&f=json"
)

records = response.json()["features"]
geometry = []
tickets = []

for record in records:
    tickets.append(record["attributes"])
    geometry.append(record["geometry"])