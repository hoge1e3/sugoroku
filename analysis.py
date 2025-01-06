import json
import os
from pathlib import PurePath
match_chunk=None
map_chunk=None
def proc_map(map_chunk):
    map_file=map_chunk[0]
    if not os.path.exists(map_file):
        return
    sum_turns=0
    sum_win_point=0
    sum_lose_point=0
    sum_stops=dict()
    for (turns, win_point, lose_point, stops) in map_chunk[1:]:
        sum_turns+=turns
        sum_win_point+=win_point
        sum_lose_point+=lose_point
        for cell in stops:
            if not cell in sum_stops: sum_stops[cell]=(0,0) 
            (sw,sl)=sum_stops[cell]
            (w,l)=stops[cell]
            sum_stops[cell]=(sw+w,sl+l)
    le=len(map_chunk[1:])
    for cell in sum_stops:
        (w,l)=sum_stops[cell]
        sum_stops[cell]=int((w*100)/(w+l))-50
    if sum_turns/le>30:
        dst=os.path.join( os.path.dirname(map_file), "toolong", os.path.basename(map_file))
        os.rename(map_file, dst)
    else:
        print(map_file, sum_win_point/le, sum_lose_point/le, sum_turns/le , sum_stops)
def proc_match(match_chunk):
    global map_chunk
    map_file=match_chunk[0][1]
    if map_chunk==None or map_chunk[0]!=map_file:
        if map_chunk:proc_map(map_chunk)
        map_chunk=[map_file]
    winner=match_chunk[-1][1]
    stops=[m for m in match_chunk if m[0]=="stop"]
    stopc=dict()
    for s in stops[:-1]:
        myp=s[1]
        enp=s[2]
        cell=myp["cell"]["class"]
        if not (cell in stopc): stopc[cell]=(0,0)
        (w,l)=stopc[cell]
        if myp["name"]==winner:
            stopc[cell]=(w+1,l)
        else:
            stopc[cell]=(w,l+1)
    laststop=stops[-1]
    winp=laststop[1]
    losep=laststop[2]
    diff_stops=dict()
    map_chunk.append((len(stops), winp["point"], losep["point"], stopc))#, winner_stops, loser_stops)

with open("logs/log.jsonl","r") as f:
    ln=0
    for line in f.readlines():
        try:
            ln+=1
            data=json.loads(line)
            #print(data)
            if data[0]=="start":
                match_chunk=[data]
            elif data[0]=="winner":
                if match_chunk:
                    match_chunk.append(data)
                    proc_match(match_chunk)
                match_chunk=None
            elif match_chunk:
                match_chunk.append(data)
        except Exception as e:
            print("At line ",ln, ":", line)
            print(e)
            raise e
"""
["start", "maps/map-20241206-161445.json"]
["stop", 
{"class": "Player", 
    "cell": {"class": "GateCell4", "number": 8}, 
    "dir": {"class": "tuple"}, "human": false, "name": "p1", 
    "point": 10000.0, "pos": {"class": "tuple"}, "win": 0, "x": 7.0, "y": 0}, 
{"class": "Player", "cell": {"class": "cell28", "number": 1}, "dir": {"class": "tuple"}, "human": false, "name": "p2", "point": 1000.0, "pos": {"class": "tuple"}, "win": 0, "x": 3.0, "y": 0}]
["winner", "p1"]
"""