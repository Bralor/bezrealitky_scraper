import os
import json

import requests


class Scraper:
    def __init__(self, url: str, json_files: str):
        self.url = url
        self.json_files = json_files


    def send_request(self, params):
        if not params:
            raise Exception(f"Missing argument {params}")

        self.response = requests.post(self.url, params)


    def load_json(self, json_f):
        if not isinstance(json_f, str):
            raise Exception("Response object is not str")

        self.content = json.loads(json_f)


    @staticmethod
    def find_params(path: str) -> list:
        if not os.path.isdir(path):
            raise Exception(f"Folder: {path}, does not exist.")

        return [
            file
            for file in os.listdir(path)
            if os.path.splitext(file)[1] == ".json"
        ]
