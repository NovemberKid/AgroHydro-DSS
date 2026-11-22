import json
from pathlib import Path


# Project root:
# AgroHydro-DSS/
# └── data/
#     └── fields.json
DATA_FILE = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "fields.json"
)


def get_all_fields():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_field_by_id(field_id: str):
    fields = get_all_fields()

    for field in fields:
        if field["field_id"] == field_id:
            return field

    return None