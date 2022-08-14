from flask import *
from flask_cors import CORS

import json
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index(channel="not insert channel"):
    channel = str(request.args.get('channel'))
    janerr="sport"
    name=""
    ename=""
    link=""
    print(channel)
    if channel=="11" or channel=="12" or channel=="13" or channel=="14":
        janerr="news"
    if channel == "11":
        name="כאן 11"
        ename="kan 11"
    if channel == "12":
        name="קשת 12"
        ename="keshet 12"
    if channel == "13":
        name="רשת 13"
        ename="reshet 13"
    if channel == "14":
        name="עכשיו 14"
        ename="now 14"
    if channel == "51":
        name="ספורט 1"
        ename="sport 1"
    if channel == "52":
        name="ספורט 2"
        ename="sport 2"
    if channel == "53":
        name="ספורט 3"
        ename="sport 3"
    if channel == "54":
        name="ספורט 4"
        ename="sport 4"
    if channel == "55":
        name="ספורט 5"
        ename="sport 5"
    if channel == "56":
        name="ספורט 5 פלוס"
        ename="sport 5 plus"
    if channel == "57":
        name="ספורט 5 גולד"
        ename="sport 5 gold"
    if channel == "58":
        name="ספורט 5 לייב"
        ename="sport 5 live"
    if janerr=="sport":
        link=f"https://poscitech.click/player/ch{(int)(channel)+89}.php"
    json_dump={"num":channel,"name":name,"ename":ename,"janerr":janerr,"link":link}
    return json_dump
app.run(host='0.0.0.0', port=80)
