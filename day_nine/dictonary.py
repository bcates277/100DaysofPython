#!/usr/bin/env python3

risk_items = {
        "id": 1,
        "title": "Unauthorized Access",
        "severity": "High",
        "status": "Open",
        "owner": "Security Team"
    }
# print(risk_items["owner"])
risk_items["name"] = "add person's name"
# print(risk_items)

empty_dictionary = {}

risk_items["status"] = "closed"
# print(risk_items)

for key in risk_items:
    print(key)
    print(risk_items[key])