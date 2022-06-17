import requests

url = "http://192.168.49.1:8079/users"

payload = "{\n    \"ime\": \"Stefan\",\n    \"prezime\": \"Janicijevic\",\n    \"smer\": \"RI\",\n    \"predmeti\": [\n        {\n            \"ime\": \"LAAG\",\n            \"espb\": \"8\"\n        }\n        ,\n        {\n            \"ime\": \"Arhitektura racunara\",\n            \"espb\": \"6\"\n        },\n        {\n            \"ime\": \"Namenski racunarski sistemi\",\n            \"espb\": \"7\"\n        }\n        \n    ]\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "db0493e1-702b-fa70-eecc-316bdfb615bb"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)