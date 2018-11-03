// This example adds a search box to a map, using the Google Place Autocomplete
// feature. People can enter geographical searches. The search box will return a
// pick list containing a mix of places and predicted search terms.

// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:

function initMap() {
var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 34.1, lng: -117.7},
    zoom: 13,
    mapTypeControl: false,
    mapTypeId: 'roadmap'
});

// Create the search box and link it to the UI element.
var inputFrom = document.getElementById('pac-input-from');
var searchBoxFrom = new google.maps.places.SearchBox(inputFrom);
var inputTo = document.getElementById('pac-input-to');
var searchBoxTo = new google.maps.places.SearchBox(inputTo);

// Bias the SearchBox results towards current map's viewport.
map.addListener('bounds_changed', function() {
    searchBoxFrom.setBounds(map.getBounds());
    searchBoxTo.setBounds(map.getBounds());
});

var markers = [];
// Listen for the event fired when the user selects a prediction and retrieve
// more details for that place.
searchBoxFrom.addListener('places_changed', function() {
    var places = searchBoxFrom.getPlaces();

    if (places.length == 0) {
    return;
    }

    // Clear out the old markers.
    markers.forEach(function(marker) {
    marker.setMap(null);
    });
    markers = [];

    // For each place, get the icon, name and location.
    var bounds = new google.maps.LatLngBounds();
    places.forEach(function(place) {
    if (!place.geometry) {
        console.log("Returned place contains no geometry");
        return;
    }
    var icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
    };

    // Create a marker for each place.
    markers.push(new google.maps.Marker({
        map: map,
        icon: icon,
        title: place.name,
        position: place.geometry.location
    }));

    if (place.geometry.viewport) {
        // Only geocodes have viewport.
        bounds.union(place.geometry.viewport);
    } else {
        bounds.extend(place.geometry.location);
    }
    });
    map.fitBounds(bounds);
});
// Listen for the event fired when the user selects a prediction and retrieve
// more details for that place.
searchBoxTo.addListener('places_changed', function() {
    var places = searchBoxTo.getPlaces();

    if (places.length == 0) {
    return;
    }

    // Clear out the old markers.
    markers.forEach(function(marker) {
    marker.setMap(null);
    });
    markers = [];

    // For each place, get the icon, name and location.
    var bounds = new google.maps.LatLngBounds();
    places.forEach(function(place) {
    if (!place.geometry) {
        console.log("Returned place contains no geometry");
        return;
    }
    var icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
    };

    // Create a marker for each place.
    markers.push(new google.maps.Marker({
        map: map,
        icon: icon,
        title: place.name,
        position: place.geometry.location
    }));

    if (place.geometry.viewport) {
        // Only geocodes have viewport.
        bounds.union(place.geometry.viewport);
    } else {
        bounds.extend(place.geometry.location);
    }
    });
    map.fitBounds(bounds);
});
}
