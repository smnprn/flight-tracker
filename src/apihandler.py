import json
from filereader import *
from requests import *

create_endpoint = "https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create"
poll_endpoint = "https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/poll/"

# The API key used below is the public key used for testing
headers = {
    "x-api-key": "sh428739766321522266746152871799"
}

filer_reader = FileReader()
settings = filer_reader.load_settings()

data = {
            "query": {
                "market":"IT",
                "locale":"it-IT",
                "currency": settings["currency"],
                "query_legs":[
                    {
                        "origin_place_id":{"iata":settings["origin_place_id"]},
                        "destination_place_id":{"iata":settings["destination_place_id"]},
                        "date":{"year":settings["year"],"month":settings["month"],"day":settings["day"]}
                    }
                ],
                "adults":settings["adults"],
                "cabin_class":"CABIN_CLASS_ECONOMY"
            }
        }

class ApiHandler:
    def search_flight(self):
        print(json.dumps(data))
        response = post(create_endpoint, headers=headers, data=json.dumps(data))

        return response
