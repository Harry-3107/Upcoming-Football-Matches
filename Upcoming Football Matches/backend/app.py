from flask import Flask, jsonify, send_from_directory
import requests
from flask_cors import CORS
import os

# Adjust the static_folder to point to ../frontend
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

API_KEY = 'd0319e445be94fd294640efc149de787'
HEADERS = {'X-Auth-Token': API_KEY}
API_BASE_URL = 'https://api.football-data.org/v4'  # Correct API base

# Serve the frontend index.html
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static assets like JS/CSS
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

# API endpoints
@app.route('/api/leagues')
def get_leagues():
    try:
        res = requests.get(f'{API_BASE_URL}/competitions', headers=HEADERS)
        return jsonify(res.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/teams/<league_code>')
def get_teams(league_code):
    try:
        url = f'{API_BASE_URL}/competitions/{league_code}/teams'
        res = requests.get(url, headers=HEADERS)
        return jsonify(res.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/league/<league_code>/matches')
def get_league_matches(league_code):
    try:
        url = f'{API_BASE_URL}/competitions/{league_code}/matches?status=SCHEDULED'
        response = requests.get(url, headers=HEADERS)
        return jsonify({'matches': response.json().get('matches', [])})
    except Exception as e:
        return jsonify({'error': 'Failed to load matches'}), 500

@app.route('/api/matches/<int:team_id>')
def get_matches(team_id):
    try:
        url = f'{API_BASE_URL}/teams/{team_id}/matches?status=SCHEDULED'
        res = requests.get(url, headers=HEADERS)
        return jsonify(res.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
