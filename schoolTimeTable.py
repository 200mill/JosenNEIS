import schoolInfo.py
import requests

key = ""

def schoolTimeTable(school : str, 
                    grade : int,
                    classNum : int):
    school_info_jsonparsed = schoolInfo.schoolInfo(str(school),)
    if school_info_jsonparsed["SCHUL_KND_SC_NM"] == "초등학교":
        res = requests.get(f'https://open.neis.go.kr/hub/elsTimetable?Type=json&ATPT_OFCDC_SC_CODE={school_info_jsonparsed["ATPT_OFCDC_SC_CODE"]}\
                           &SD_SCHUL_CODE={school_info_jsonparsed["SD_SCHUL_CODE"]}&key={key}')
        
        return 0
    elif school_info_jsonparsed["SCHUL_KND_SC_NM"] == "중학교":
        print()
        return 0
    elif school_info_jsonparsed["SCHUL_KND_SC_NM"] == "고등학교":
        print()
        return 0
    else:
        return 1
