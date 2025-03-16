from flask import Flask, render_template, json, jsonify
import requests

key = ""
app = Flask(__name__)

@app.route('/')
def index():
    return 'example'

@app.route('/schoolinfo')
def timetable(school: str, grade: str, class_name: str):
    if school == '' or grade == '' or class_name == '':
        return 1
    try:
        res = requests.get(f'https://open.neis.go.kr/hub/schoolinfo?SCHUL_NM={school}&type=json&key={key}')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return 0

