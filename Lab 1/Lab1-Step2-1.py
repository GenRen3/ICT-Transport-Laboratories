import pymongo as pm
import pprint as pp
import numpy as np
import matplotlib.pyplot as plt
import datetime, time
import os

#Here we set the client
client = pm.MongoClient('bigdatadb.polito.it', ssl=True,
         authSource = 'carsharing', tlsAllowInvalidCertificates=True)

#Here we access to a specific collection of the client
db = client['carsharing']
db.authenticate('ictts', 'Ictts16!', mechanism='SCRAM-SHA-1') #authentication

#Collection for Car2go
Car2goPermanentBook = db['PermanentBookings']
Car2goPermanentPark = db['PermanentParkings']
Car2goActiveBook = db['ActiveBookings']
Car2goActivePark = db['ActiveParkings']

#Collection for enjoy
enjoyPermanentBook = db['enjoy_PermanentBookings']
enjoyPermanentPark = db['enjoy_PermanentParkings']
enjoyActiveBook = db['enjoy_ActiveBookings']
enjoyActivePark = db['enjoy_ActiveBookings']


ict_PermanentBook = db['ictts_PermanentBookings']
ict_enjoy_PermanentBook = db['ictts_enjoy_PermanentBookings']

first_oct_day = time.mktime((datetime.datetime(2017, 10, 1, 0, 0)).timetuple())
last_oct_day = time.mktime((datetime.datetime(2017, 11, 1, 0, 0)).timetuple())

citiesTimezone = {"Milano": -1, "Frankfurt": -1, "New York City": 5}
dataRow = {}
cumulative = {}
folder = os.path.dirname(os.path.abspath(__file__))

for city in citiesTimezone:
    addTime = citiesTimezone[city]*60*60
    resultQuery = Car2goPermanentBook.aggregate([
        {"$match":  # stage 1 of the pipeline
             {"$and": [{"city": city},
                       {"init_time": {"$gte": first_oct_day + addTime}},
                       {"init_time": {"$lte": last_oct_day + addTime}}
                       ]}
        }, {"$project": {
            "_id": 0,
            "durationBook": {"$divide": [{"$subtract": ["$final_time", "$init_time"]}, 60]},
            # week returns the number of week (1,2,3,4) in october
            "week": {"$divide": [{"$subtract": ["$init_time", 1506801599]}, 604800]},
            "moved": {"$ne": [{"$arrayElemAt": ["$origin_destination.coordinates", 0]},
                              {"$arrayElemAt": ["$origin_destination.coordinates", 1]}]}
            }
        }, {"$match": {
             "moved": True}
        }
    ])
    dataRow[city] = {}
    dataRow[city][1] = []
    dataRow[city][2] = []
    dataRow[city][3] = []
    dataRow[city][4] = []
    dataRow[city]['tot'] = []
    cumulative[city] = {}
    cumulative[city][1] = []
    cumulative[city][2] = []
    cumulative[city][3] = []
    cumulative[city][4] = []
    cumulative[city]['tot'] = []

    for item in resultQuery:
        dataRow[city]['tot'].append(item["durationBook"])
        if int(item["week"]) == 1:
            dataRow[city][1].append(item["durationBook"])
        elif int(item["week"]) == 2:
            dataRow[city][2].append(item["durationBook"])
        elif int(item["week"]) == 3:
            dataRow[city][3].append(item["durationBook"])
        elif int(item["week"]) >= 4:
            dataRow[city][4].append(item["durationBook"])

    fig = plt.figure(city, figsize=(20, 10))

    bins = np.arange(np.floor(min(dataRow[city]['tot'])), np.ceil(max(dataRow[city]['tot'])))
    values, base = np.histogram(dataRow[city]['tot'], bins=bins, density=1)
    cumulative[city]['tot'] = np.cumsum(values)
    plt.plot(base[:-1], cumulative[city]['tot'], 'b*', label="Month")

    for j in [1, 2, 3, 4]:
        bins = np.arange(np.floor(min(dataRow[city][j])), np.ceil(max(dataRow[city][j])))
        values, base = np.histogram(dataRow[city][j], bins=bins, density=1)
        cumulative[city][j] = np.cumsum(values)

        plt.plot(base[:-1], cumulative[city][j], label="Week" + str(j), linewidth=3.5)
        plt.xlabel('Minutes')
        plt.legend()

    plt.title("CDF booking/parking duration in "+city+", October 2017")
    fig.savefig(folder + '/' + city + '-booking.png')
    plt.legend(prop={'size': 20})
    plt.close(fig)
