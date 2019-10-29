import pymongo as pm
import pprint as pp

#Here we set the client
client = pm.MongoClient('bigdatadb.polito.it', ssl=True,
         authSource = 'carsharing', tlsAllowInvalidCertificates=True)

#Here we access to a specific collection of the client
db = client['carsharing']
db.authenticate('ictts', 'Ictts16!', mechanism='SCRAM-SHA-1') #authentication

#Collection for Car2go to use, this a cursor that I need to convert as a list (PANDAS)
Bookings_collection_1 = db['PermanentBookings']
Bookings_collection_2 = db['ActiveBookings']


#Example of a json file of a car in Vancouver
pp.pprint(Bookings_collection_1.find_one({"city":"Vancouver"}))


#Here counts the cars the city of Turin in a certain set of time
print(Bookings_collection_1.find({"city": "Torino"}).count(True))
