import requests
import os
import json
from flask import Flask, request

access_token = "NzE3NmMyMmYtYjYxNS00NTBlLWE1ZGYtMmJhYjdiNzhlNDBmZjUwZWRjNWQtODk4_PF84_6121c98f-64c5-48a2-95f7" \
               "-6e1f074ad37f "
app = Flask(__name__)


def name(person_id):
    headers = {'Authorization': 'Bearer ' + access_token, 'content-type': 'application/json'}
    response = requests.get("https://api.ciscospark.com/v1/people/" + person_id, headers=headers)
    response = json.loads(response.text)
    return response["displayName"]


def post_message(person_id, room_id):
    headers = {'Authorization': 'Bearer ' + access_token, 'content-type': 'application/json'}
    data = {'roomId': room_id, 'text': 'Hello ' + name(person_id) + ', How are you doing?'}
    response = requests.post("https://api.ciscospark.com/v1/messages", json=data, headers=headers)
    return response.text


@app.route('/', methods=['POST'])
def main():
    json_data = request.json
    data = json_data['data']
    person_email = data['personEmail']
    if person_email == "testbot2.1@webex.bot":
        return "DONE"
    person_id = data["personId"]
    room_id = data["roomId"]
    return json.loads(post_message(person_id, room_id))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
