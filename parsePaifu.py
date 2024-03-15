import PaifuTypesPydantic
import pydantic
import json
import os

paifu = "gameDataSample.json"
json_file = open(paifu, "r")
json_data = json.load(json_file)

paifu = PaifuTypesPydantic.Paifu.model_validate_json(json.dumps(json_data), strict=True)
print(paifu)
