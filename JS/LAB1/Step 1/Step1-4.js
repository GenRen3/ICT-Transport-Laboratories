db.PermanentParkings.find({},{"init_time":1,"init_date":1, "_id" :0}).sort({"init_time":1}).limit(1)
# Result : "init_time" : 1481650658, "init_date" : ISODate("2016-12-13T09:37:38.000Z")

db.PermanentParkings.find({},{"init_time":1, "init_date":1, "_id":0}).sort({"init_time":-1}).limit(1)
# Result : "init_time" : 1517404293, "init_date" : ISODate("2018-01-31T14:11:33.000Z")