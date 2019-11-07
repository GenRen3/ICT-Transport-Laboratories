db.PermanentParkings.distinct("city").sort() 
# Total: 26 cities
# "Amsterdam", "Austin", "Berlin", "Calgary", "Columbus", "Denver", "Firenze", "Frankfurt", "Hamburg",
# "Madrid", "Milano", "Montreal", "Munchen", "New York City", "Portland", "Rheinland", "Roma", "San Diego", 
# "Seattle", "Stuttgart", "Torino", "Toronto", "Twin Cities", "Vancouver", "Washington DC", "Wien"

db.enjoy_PermanentParkings.distinct("city").sort() 
# Total: 6 cities 
# "Bologna", "Catania", "Firenze", "Milano", "Roma", "Torino"