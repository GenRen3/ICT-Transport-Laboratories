# count the documents of each collection (Car2Go)
db.ActiveBookings.find().count() #8743
db.ActiveParkings.find().count() #4790
db.PermanentBookings.find().count() #28180508
db.PermanentParkings.find().count() #28312676


# count the documents of each collection (Enjoy)
db.enjoy_ActiveBookings.find().count() #0
db.enjoy_ActiveParkings.find().count() #0
db.enjoy_PermanentBookings.find().count() #6653472
db.enjoy_PermanentParkings.find().count() #6689979