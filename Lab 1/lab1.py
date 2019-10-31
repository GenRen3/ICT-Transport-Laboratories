import pymongo as pm

# configuration
client = pm.MongoClient('bigdatadb.polito.it', ssl=True, authSource = 'carsharing', tlsAllowInvalidCertificates=True)
db = client['carsharing'] #Choose the database to use
db.authenticate('ictts', 'Ictts16!')# , mechanism='MONGODB-CR')


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


# query = {"city":"Torino", "init_fuel": {"$gt":0}} # query about cars in torino with init fuel greater that 0
# result = permanentBook.find(query).count() # searching for vehicles in Turin with fuel greater than 14

# -------------------------------------------------------------------1
# r = permanentBook.count()
# print(r) # = 28180508

# r = activeBook.count()
# print(r) # = 8743

# r = permanentPark.count()
# print(r) # = 28312676

# r = activePark.count()
# print(r) # = 4790

# r = enjoy_activePark.count()
# print(r) # = 0

# r = enjoy_activeBook.count()
# print(r) # = 0

# r = enjoy_permanentPark.count()
# print(r) # = 6689979

# r = enjoy_permanentBook.count()
# print(r) # = 6653472

# ---------------------------------------------------------------------3
# totalCities = permanentBook.distinct("city")
# print(totalCities)

# ------------------------------------------------------------------------4
# resultFr = permanentBook.find({"city":"Frankfurt"}).count()
# resultMil = permanentBook.find({"city":"Milano"}).count()
# resultNy = permanentBook.find({"city": "New York City"}).count()
# print("Frankfurt, Milano, New York City: ", resultFr, resultMil, resultNy)


# -----------------------------------------------------------------------------------------------------7
# result: Milano: 213364; Frankfurt:53944; NYC:74325 for newyork 5 ore indietro! calcolo del timestamp
# locale per 1/12/17 e 31/12/17 e poi per new york ricalcolo tenendo conto del fuso orario di 5 ore indietro
# query = {"city":"New York City", "init_time":{
#             "$gte": 1512068399, # 1/12/17 at 00:00:00; per new York usa --> 1512068399
#             "$lte": 1514743199 # 31/12/2017 at 23:59:59; per New York usa --> 1514743199
#             }
#         }
# result = permanentBook.find(query).count()
# print(result)

