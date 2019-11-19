var cities = ["Milano", "Frankfurt", "New York City"];

for (var i=0; i<cities.length; i++){   
    c = cities[i];
    a = db.ActiveBookings.distinct("plate",{city: c});
    b = db.ActiveParkings.distinct("plate",{city: c});
    print ("Available car in", cities[i], ":" ,a.length + b.length);
}