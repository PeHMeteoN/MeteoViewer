window.addEventListener("map:init", function (event) {
var map = event.detail.map.setView( [-15, -75], 4);

//Download GeoJSON data with Ajax
// Geometria de estaciones
// fetch(dataurl)
//   .then(function(resp) {
//     return resp.json();
//   })
//   .then(function(data) {
//    var estaciones = L.geoJson(data, {
//      onEachFeature: function onEachFeature(feature, layer) {
//        var props = feature.properties;
//        var content = `<h3>${props.estado}</h3><p>${props.nom}</p>`;
//        layer.bindPopup(content);
//    }});
//   });

var estaciones = L.tileLayer.wms("http://localhost:8080/geoserver/climatic-data/wms", {
   layers: "climatic-data:opendata_historic",
   iconUrl: 'img/red.png',
   format: 'image/png',
   transparent: true
});

var departamentos = L.tileLayer.wms("http://localhost:8080/geoserver/climatic-data/wms", {
   layers: "climatic-data:departamentos",
   format: 'image/png',
   transparent: true
});

var provincias = L.tileLayer.wms("http://localhost:8080/geoserver/climatic-data/wms", {
   layers: "climatic-data:provincias",
   format: 'image/png',
   transparent: true
});

var zonavida = L.tileLayer.wms("http://idesep.senamhi.gob.pe/geoserver/g_05_06/wms", {
   layers: "05_06_001_03_001_521_0000_00_00",
   format: 'image/png',
   transparent: true
});

var groupedOverLayers = {
  "Base": {
    "Departamentos": departamentos,
    "Provincias": provincias
  },
  "Data": {
    "Estaciones": estaciones,
    "Zona de Vida": zonavida
  }
};

L.control.groupedLayers(null, groupedOverLayers, {
    collapsed: false,
    position: 'topleft'
}).addTo(map);
//L.control.layers(overlayMaps).addTo(map);


/////////////////////////////////////

var url = 'http://localhost:8080/geoserver/climatic-data/wms';
var dep = L.tileLayer.betterWms(url, {
    layers: 'climatic-data:departamentos',
    transparent: true,
    format: 'image/png'
}).addTo(map);

////////////////////////////////////






});
