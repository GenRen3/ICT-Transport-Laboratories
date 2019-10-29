import pymongo as pm

# configuration
client = pm.MongoClient('bigdatadb.polito.it', ssl=True, authSource = 'carsharing', tlsAllowInvalidCertificates=True)
db = client['carsharing'] #Choose the database to use
db.authenticate('ictts', 'Ictts16!')# , mechanism='MONGODB-CR')
# comment

permanentBook = db['PermanentBookings']
permanentPark = db['PermanentParkings']
activeBook = db['ActiveBookings']
activePark = db['ActiveParkings']

enjoy_permanentBook = db['enjoy_PermanentBookings']
enjoy_permanentPark = db['enjoy_PermanentParkings']
enjoy_activeBook = db['enjoy_ActiveBookings']
enjoy_activePark = db['enjoy_ActiveBookings']

ict_PermanentBook = db['ictts_PermanentBookings']
ict_enjoy_PermanentBook = db['ictts_enjoy_PermanentBookings']


query = {"city":"Torino", "init_fuel" : {"$gt":0}}
print("Here!")
result = permanentBook.find(query).count(True) # searching for vehicles in Turin with fuel greater than 14
print(result)