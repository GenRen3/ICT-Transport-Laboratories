import pymongo as pm #pymongo
import pprint as pp #pretty print

#Here we set the client
client = pm.MongoClient('bigdatadb.polito.it', ssl=True,
         authSource = 'carsharing', tlsAllowInvalidCertificates=True)

#Here we access to a specific collection of the client
db = client['carsharing']
db.authenticate('ictts', 'Ictts16!', mechanism='SCRAM-SHA-1') #authentication

Bookings_collection = db['PermanentBookings'] #Collection for Car2go to use

#Example of a json file of a car in Vancouver
pp.pprint(Bookings_collection.find_one({"city":"Vancouver"}))

#Here finds the city of Turin in a certain set of time
Bookings_collection.find( {"city": "Torino"},{"init_time":1, "city":1, "_id":0,
                           "init_date":1})
