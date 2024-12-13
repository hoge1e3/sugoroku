import cell
import re
import json
import datetime
n2c=dict()
for n in dir(cell):
    if re.match(r"(Gate)?[Cc]ell\d+",n ):
        cl=cell.__getattribute__(n)
        n2c[n]=cl
        n2c[n.lower()]=cl
        #print (n, cl, cl.__name__)

def conv(e):
    if e:
        o={"class": type(e).__name__ }
        for n in dir(e):
            if re.search(r"^__",n):continue
            v=e.__getattribute__(n)
            if callable(v):continue
            o[n]=v                
        return o
    return e
def save(map, prefix="map"):
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    filename=now.strftime(f'maps/{prefix}-%Y%m%d-%H%M%S.json')
    with open(filename,"w") as f:
        json.dump(map, f,default=conv,indent=2)
    return filename

def unconv(d):
    cls=n2c[d["class"]]
    res=cls()
    for k in d:
        if d=="class":continue
        res.__setattr__(k, d[k])
    return res
def load(filename):
    with open(filename, "r") as f:
        data=json.load(f,object_hook=unconv)
    return data 

#print(load("maps/map-20241204-112006.json")  )