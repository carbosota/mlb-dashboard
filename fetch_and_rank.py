import json
# Simulate ranked output
data = [{"playerID": "123", "playerName": "Test Player", "team": "NYM", "position": "1B", "hits": {"one": "-110", "two": "+300"}, "bases": {"total": "1.5", "over": "+120", "under": "-140"}, "runs": {"total": "0.5", "over": "+180", "under": "-200"}, "confidence": 88.6}]
with open("ranked_props.json", "w") as f:
    json.dump(data, f)
with open("index.html", "r") as f:
    html = f.read()
# No need to rewrite HTML here – assumed static
