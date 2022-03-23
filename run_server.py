from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

TOKEN = os.environ.get("GITHUB_TOKEN")
OWNER = os.environ.get("GITHUB_OWNER")
REPO = os.environ.get("GITHUB_REPO")
VERSION = os.environ.get("VERSION")

headers = {
  "Accept": "application/vnd.github.v3+json",
  "Authorization": f"token {TOKEN}",
}

data = {
  "event_type": "run-server",
  "client_payload": {
    "version": VERSION
  }
}

url = f"https://api.github.com/repos/{OWNER}/{REPO}/dispatches"

thing = requests.post(
  f"https://api.github.com/repos/{OWNER}/{REPO}/dispatches",
  data=data,
  headers=headers
)

response = requests.post(url, data=json.dumps(data), headers=headers)

# print("I think it worked...")
print(thing.headers)
print(thing.json())



