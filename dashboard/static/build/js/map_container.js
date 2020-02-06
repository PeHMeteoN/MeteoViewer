window.addEventListener("map:init", function (event) {
var map = event.detail.map.setView( [-15, -75], 4);

var departamentos = L.tileLayer.wms("http://localhost:8080/geoserver/bd/wms", {
   layers: "bd:gpo_departamentos",
   format: 'image/png',
   transparent: true
});

var provincias = L.tileLayer.wms("http://localhost:8080/geoserver/bd/wms", {
   layers: "bd:gpo_provincias",
   format: 'image/png',
   transparent: true
});

var gpo_puno = L.tileLayer.wms("http://localhost:8080/geoserver/bd/wms", {
   layers: "bd:gpo_dep_puno",
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
    "Provincias": provincias,
    "Puno": gpo_puno
  },
  "Data": {
    "Zona de Vida": zonavida
  }
};

L.control.groupedLayers(null, groupedOverLayers, {
    collapsed: false,
    position: 'topleft'
}).addTo(map);



});
