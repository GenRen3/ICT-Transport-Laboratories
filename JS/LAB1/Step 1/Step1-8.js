var cities = ["Milano", "Frankfurt", "New York City"];
for(var i = 0; i < cities.length; i++){
var countBooking = db.PermanentBookings.find({"city":cities[i],
    $or:[ {"walking.duration":{$ne:-1}},{"public_transport.duration": {$ne:-1}} ] }).count();
print("Number of booking that had an alternative transportation in " + cities[i] + " : " + countBooking);   
}
// Number of booking that had an alternative transportation in Milano : 728653
// Number of booking that had an alternative transportation in Frankfurt : 0
// Number of booking that had an alternative transportation in New York City : 0