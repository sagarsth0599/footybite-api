from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return "Match API is Running"

@app.route('/matches')
def get_matches():
    url = "https://footybite.to/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    matches = []
    for item in soup.find_all('div', class_='content-box'):
        try:
            title = item.find('a').text.strip()
            link = item.find('a')['href']
            time = item.find('span').text.strip()
            matches.append({
                'title': title,
                'time': time,
                'link': link
            })
        except:
            continue

    return jsonify(matches)