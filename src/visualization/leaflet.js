const COUNTRY_SIZE_MULTIPLICATOR = 6;

const map = L.map('map', {
    center: [48, 12],
    zoom: 4,
    minZoom: 4,
    maxZoom: 6,
    zoomSnap: 0.25,
    zoomControl: false,
    maxBounds: [[66, -30], [28, 53]]
});

const cartodbAttribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://carto.com/attribution">CARTO</a>';

L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    attribution: cartodbAttribution
}).addTo(map);

L.control.zoom({
    position: 'bottomleft'
}).addTo(map);

console.log(data);

for (const {country, coords, seizures} of data) {
    console.log(country, seizures * COUNTRY_SIZE_MULTIPLICATOR)
    const circleMarker = L.circle([coords.lat, coords.lng], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: Math.max(1500, seizures * COUNTRY_SIZE_MULTIPLICATOR)
    }).addTo(map);

    circleMarker.bindTooltip(`${country} - ${Math.round(seizures)}`);
    circleMarker.on('mouseover', (e) => {
        e.target.openTooltip();
    });
}
