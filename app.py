import logging.config
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests
import json
from flask import make_response
from urllib.parse import urljoin

app = Flask(__name__)


@app.route('/')
def home():
    request_url = "https://cloud-demo-httptrigger.azurewebsites.net/api/"
    response = requests.get(request_url + 'getNotes?code=EwlnZnJcEw3ktpi9nLb3Ptdbcg29347AKyUzJuqxFrEs2TV05ERloA==')
    notes = response.json()
    return render_template("index.html", notes=notes)

def main():
    app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
    main()
    # comment
