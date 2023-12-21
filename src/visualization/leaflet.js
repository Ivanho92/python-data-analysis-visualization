const COUNTRY_SIZE_MULTIPLICATOR = 6;

const map = L.map('map', {
    minZoom: 4,
    maxZoom: 5,
    zoomSnap: 0.25
});

const cartodbAttribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://carto.com/attribution">CARTO</a>';

L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    attribution: cartodbAttribution
}).addTo(map);

map.setView([49.945126920172086, 11.694728318204573], 0);

console.log(data);

for (const {country, coords, seizures} of data) {
    const circleMarker = L.circle([coords.lat, coords.lng], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: seizures * COUNTRY_SIZE_MULTIPLICATOR
    }).addTo(map);

    circleMarker.bindTooltip(country);
    circleMarker.on('mouseover', (e) => {
        e.target.openTooltip();
    });
}
