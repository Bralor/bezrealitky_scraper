import os
import json
from importlib import import_module

import requests


class Scraper:
    def __init__(self, url: str, source: str, location: str):
        self.url = url
        self.source = source
        self.location = location


    def find_params(self) -> str:
        if not os.path.isdir(self.source):
            raise Exception(f"Folder: {self.source}, does not exist.")

        return [
            file
            for file in os.listdir(self.source)
            if os.path.splitext(file)[1] == ".py"
            and os.path.splitext(file)[0] == self.location
        ].pop()


    def get_module_name(self, py_file: str) -> tuple:
        return (
            path := os.path.join(self.source, py_file),
            os.path.splitext(path.replace(os.sep, ".", 2))[0]
        )


    @staticmethod
    def load_params(path: str, modulename: str) -> dict:
        if not os.path.isfile(path):
            raise Exception(f"File \"{path}\" does not exists")

        return import_module(modulename).request_params


    def send_request(self, params):
        if not params:
            raise Exception(f"Missing argument {params}")

        self.response = requests.post(self.url, params).text


    @staticmethod
    def read_json(str_json):
        if not isinstance(str_json, str):
            raise Exception("Response object is not str")

        return json.loads(str_json)


