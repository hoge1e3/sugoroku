import json
import re
file="logs/log.jsonl"
def add(data):
    with open(file,"a") as f:
        json.dump(conv(data), f)
        f.write("\n")
def conv(e, visited=None):
    if isinstance(e, int):
        return e
    if isinstance(e, float):
        return e
    if isinstance(e, str):
        return e
    if not visited:
        visited=set()
    if id(e) in visited:
        return None
    visited.add(id(e))
    if isinstance(e, dict):
        for k in e:
            conved=conv(e[k], visited)    
            if conved!=None:
                e[k]=conved
    if isinstance(e, list):
        return [conv(el, visited) for el in e]
    if e:
        o={"class": type(e).__name__ }
        for n in dir(e):
            if re.search(r"^__",n):continue
            v=e.__getattribute__(n)
            if callable(v):continue
            o[n]=conv(v, visited)                
        return o
    return e