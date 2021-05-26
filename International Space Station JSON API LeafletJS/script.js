

// constant URL API

// creating map and tiles
const issMap = L.map('issMap').setView([0, 0], 1);
const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
const tileUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
const tiles = L.tileLayer(tileUrl, {attribution});

tiles.addTo(issMap);

// creating custom marker & icon
const issIcon = L.icon ({
    iconUrl: 'iss.png',
    iconSize: [50, 32],
    iconAnchor: [25, 16],
});

const marker = L.marker([0, 0], {icon: issIcon}).addTo(issMap);

const api_url = "https://api.wheretheiss.at/v1/satellites/25544";

async function getISS(){
    const response = await fetch(api_url);
    const data = await response.json();

    const { latitude, longitude } = data;

    // setting marker location
    marker.setLatLng([latitude, longitude]);
    issMap.setView([latitude, longitude], 3)

    // adjusting values
    document.getElementById("lat").textContent = latitude;
    document.getElementById('lon').textContent = longitude;

}

function getTime() {
    // setting date & retrieving times
    const date = new Date();
    var hour = date.getHours();
    var min = date.getMinutes();
    var sec = date.getSeconds();

    if (min<10) {
        min = "0" + min
    } 
    if (sec<10){
        sec = "0" + sec
    }
    
    document.getElementById('time').textContent = hour + ":" + min + ":" + sec;

    // auto refresh every 30 seconds
    setTimeout("getTime()",5000);
    getISS();
}

