from flask import Flask, request, render_template
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)
base_url = "https://api.spotify.com/v1/me/player/queue"
access_token = ""
refresh_token = os.environ.get('SPOTIFY_REFRESH_TOKEN')
client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/queue', methods=['GET'])
def get_current_queue():
    global access_token
    response = requests.get(base_url, headers={"Authorization": f"Bearer {access_token}"})
    if response.status_code == 401:
        access_token = refresh_access_token()
        response = requests.get(base_url, headers={"Authorization": f"Bearer {access_token}"})
    return response.json()


@app.route('/api/queue', methods=['POST'])
def add_to_queue():
    global access_token
    uri = request.json['uri']
    url = f"{base_url}?uri={uri}"

    response = requests.post(url, headers={"Authorization": f"Bearer {access_token}"})
    if response.status_code == 401:
        access_token = refresh_access_token()
        response = requests.post(url, headers={"Authorization": f"Bearer {access_token}"})
    return str(response.status_code)


def refresh_access_token():
    global access_token
    url = "https://accounts.spotify.com/api/token"
    body = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, data=body)
    if response.status_code == 200:
        access_token = response.json()['access_token']
    else:
        print(f"Error in refreshing access token: {response.json()}")
        return None


if __name__ == '__main__':
    refresh_access_token()
    app.run(debug=True, port=5000)
