from os import path

file_path = path.relpath("settings.txt")

class FileReader:
    def load_settings(self):
        with open(file_path) as settings_file:
            for line in settings_file:
                settings = {
                    "currency": "",
                    "origin_place_id": "",
                    "destination_place_id": "",
                    "year": "",
                    "month": "",
                    "day": "",
                    "adults": ""
                }

                parts = line.split(",")

                settings["currency"] = parts[0]
                settings["origin_place_id"] = parts[1]
                settings["destination_place_id"] = parts[2]
                settings["year"] = parts[3]
                settings["month"] = parts[4]
                settings["day"] = parts[5]
                settings["adults"] = parts[6]
        
        return settings