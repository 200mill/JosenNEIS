

if school_info_jsonparsed["SCHUL_KND_SC_NM"] == "초등학교":
        res = requests.get(f'https://open.neis.go.kr/hub/elsTimetable?Type=json&ATPT_OFCDC_SC_CODE={school_info_jsonparsed["ATPT_OFCDC_SC_CODE"]}\
                           &SD_SCHUL_CODE={school_info_jsonparsed["SD_SCHUL_CODE"]}')
        return 0
    elif school_info_jsonparsed["SCHUL_KND_SC_NM"] == "중학교":
        return 0
    elif school_info_jsonparsed["SCHUL_KND_SC_NM"] == "고등학교":
        return 0
    else:
        return 1