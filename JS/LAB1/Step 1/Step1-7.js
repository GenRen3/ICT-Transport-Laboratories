var cities = ["Milano", "Frankfurt", "New York City"];
var TimeZone = [-1,-1,5]

for(var i = 0; i < cities.length; i++){
    var addedTime = TimeZone[i]*60*60
    var startUnixTime =(new Date("2017-12-01") / 1000) + addedTime
    var endUnixTime = (new Date("2017-12-31") / 1000) + addedTime
    var countRecord = db.PermanentBookings.find({"city": cities[i], "init_time": {$gte: startUnixTime , $lte: endUnixTime}}).count();   
    print("Recorded booking in"+ cities[i]+ ":" + countRecord);  
}
//Recorded booking inMilano:209359
//Recorded booking inFrankfurt:52319
//Recorded booking inNew York City:71907