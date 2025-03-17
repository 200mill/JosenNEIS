# from flask import Flask, json, jsonify
import requests


key = ""


def schoolInfo(school: str):
    if school == "" or school == None:
        return 1
    try:
        res = requests.get(f'https://open.neis.go.kr/hub/schoolInfo?SCHUL_NM={school}&Type=json&key={key}')
        school_info = res.json()
        school_info_jsonparsed = {"ATPT_OFCDC_SC_CODE": str(school_info["schoolInfo"]["row"]["ATPT_OFCDC_SC_CODE"]),
                                  "SD_SCHUL_CODE" : str(school_info["schoolInfo"]["row"]["SD_SCHUL_CODE"]),
                                  "SCHUL_KND_SC_NM" : str(school_info["schoolInfo"]["row"]["SCHUL_KND_SC_NM"])}
        return school_info_jsonparsed
    except:
        return 2
    