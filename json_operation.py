import json

#opening file and fetch data to variable data
mf = open("D:\documents\python\milk_product\data.json",'r')

data = json.load(mf)

sm = data["sm"]
sm1 = sm[0]

fcm = data['fcm']
fcm1 = fcm[0]

curd = data['curd']
curd1 = curd[0]

sm170 = sm1["sm170"]
sm500 = sm1["sm500"]
sm1l  = sm1["sm1L"]

fcm250 = fcm1["fcm250"]
fcm500 = fcm1["fcm500"]
fcm1l  = fcm1["fcm1L"]

c140 = curd1["c140"]
c500 = curd1["c500"]
cup50 = curd1["cup50"]
cup100 = curd1["cup100"]
cup200 = curd1["cup200"]
bm = curd1["bu_milk"]


mf.close()