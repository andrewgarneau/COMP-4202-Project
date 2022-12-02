import logo from './logo.svg';
import './App.css';
import Map, {Marker, Source, Layer} from 'react-map-gl'
// import 'mapbox-gl/dist/mapbox-gl.css';


const geojsondata = {"type": "FeatureCollection", "features": [{"id": "0", "type": "Feature", "properties": {"u": 3116958148, "v": 4827861112, "osmid": 490601246, "highway": "path", "width": "3", "oneway": false, "length": 83.481}, "geometry": {"type": "LineString", "coordinates": [[-75.7635352, 45.3450694], [-75.7644495, 45.3446812]]}}, {"id": "1", "type": "Feature", "properties": {"u": 3116958148, "v": 3130225133, "osmid": 490601246, "highway": "path", "width": "3", "oneway": false, "length": 42.468}, "geometry": {"type": "LineString", "coordinates": [[-75.7635352, 45.3450694], [-75.7630689, 45.3452655]]}}, {"id": "2", "type": "Feature", "properties": {"u": 5986227749, "v": 4827861113, "osmid": 634281772, "highway": "footway", "width": null, "oneway": false, "length": 10.37}, "geometry": {"type": "LineString", "coordinates": [[-75.764638, 45.3446009], [-75.764527, 45.344652]]}}, {"id": "3", "type": "Feature", "properties": {"u": 5986227749, "v": 167025321, "osmid": 490601251, "highway": "path", "width": "3", "oneway": false, "length": 64.34700000000001}, "geometry": {"type": "LineString", "coordinates": [[-75.764638, 45.3446009], [-75.7648381, 45.3445343], [-75.7651318, 45.3444439], [-75.7654058, 45.3443991]]}}, {"id": "4", "type": "Feature", "properties": {"u": 167025321, "v": 5986227749, "osmid": 490601251, "highway": "path", "width": "3", "oneway": false, "length": 64.347}, "geometry": {"type": "LineString", "coordinates": [[-75.7654058, 45.3443991], [-75.7651318, 45.3444439], [-75.7648381, 45.3445343], [-75.764638, 45.3446009]]}}, {"id": "5", "type": "Feature", "properties": {"u": 167025321, "v": 1790766093, "osmid": 490601251, "highway": "path", "width": "3", "oneway": false, "length": 317.48299999999995}, "geometry": {"type": "LineString", "coordinates": [[-75.7654058, 45.3443991], [-75.765484, 45.344379], [-75.765732, 45.344287], [-75.7671545, 45.3435887], [-75.7675316, 45.3434653], [-75.768127, 45.343351], [-75.768416, 45.343255], [-75.7689394, 45.3430339]]}}, {"id": "6", "type": "Feature", "properties": {"u": 1790766093, "v": 1790766095, "osmid": 167702461, "highway": "footway", "width": "1.5", "oneway": false, "length": 54.595}, "geometry": {"type": "LineString", "coordinates": [[-75.7689394, 45.3430339], [-75.7692655, 45.3434681]]}}, {"id": "7", "type": "Feature", "properties": {"u": 1790766093, "v": 167025321, "osmid": 490601251, "highway": "path", "width": "3", "oneway": false, "length": 317.48299999999995}, "geometry": {"type": "LineString", "coordinates": [[-75.7689394, 45.3430339], [-75.768416, 45.343255], [-75.768127, 45.343351], [-75.7675316, 45.3434653], [-75.7671545, 45.3435887], [-75.765732, 45.344287], [-75.765484, 45.344379], [-75.7654058, 45.3443991]]}}, {"id": "8", "type": "Feature", "properties": {"u": 3130225133, "v": 3116958148, "osmid": 490601246, "highway": "path", "width": "3", "oneway": false, "length": 42.468}, "geometry": {"type": "LineString", "coordinates": [[-75.7630689, 45.3452655], [-75.7635352, 45.3450694]]}}, {"id": "9", "type": "Feature", "properties": {"u": 3130225133, "v": 3130225148, "osmid": 490601246, "highway": "path", "width": "3", "oneway": false, "length": 34.447}, "geometry": {"type": "LineString", "coordinates": [[-75.7630689, 45.3452655], [-75.7626907, 45.3454246]]}}, {"id": "10", "type": "Feature", "properties": {"u": 1790766095, "v": 1790766093, "osmid": 167702461, "highway": "footway", "width": "1.5", "oneway": false, "length": 54.595}, "geometry": {"type": "LineString", "coordinates": [[-75.7692655, 45.3434681], [-75.7689394, 45.3430339]]}}, {"id": "11", "type": "Feature", "properties": {"u": 4827861112, "v": 3116958148, "osmid": 490601246, "highway": "path", "width": "3", "oneway": false, "length": 83.481}, "geometry": {"type": "LineString", "coordinates": [[-75.7644495, 45.3446812], [-75.7635352, 45.3450694]]}}, {"id": "12", "type": "Feature", "properties": {"u": 4827861112, "v": 4827861113, "osmid": 634281772, "highway": "footway", "width": null, "oneway": false, "length": 6.872}, "geometry": {"type": "LineString", "coordinates": [[-75.7644495, 45.3446812], [-75.764527, 45.344652]]}}, {"id": "13", "type": "Feature", "properties": {"u": 4827861113, "v": 4827861112, "osmid": 634281772, "highway": "footway", "width": null, "oneway": false, "length": 6.872}, "geometry": {"type": "LineString", "coordinates": [[-75.764527, 45.344652], [-75.7644495, 45.3446812]]}}, {"id": "14", "type": "Feature", "properties": {"u": 4827861113, "v": 5986227749, "osmid": 634281772, "highway": "footway", "width": null, "oneway": false, "length": 10.37}, "geometry": {"type": "LineString", "coordinates": [[-75.764527, 45.344652], [-75.764638, 45.3446009]]}}, {"id": "15", "type": "Feature", "properties": {"u": 3130225148, "v": 3130225133, "osmid": 490601246, "highway": "path", "width": "3", "oneway": false, "length": 34.447}, "geometry": {"type": "LineString", "coordinates": [[-75.7626907, 45.3454246], [-75.7630689, 45.3452655]]}}, {"id": "16", "type": "Feature", "properties": {"u": 3130225148, "v": 3130225150, "osmid": 490601246, "highway": "path", "width": "3", "oneway": false, "length": 20.657}, "geometry": {"type": "LineString", "coordinates": [[-75.7626907, 45.3454246], [-75.7624639, 45.34552]]}}, {"id": "17", "type": "Feature", "properties": {"u": 3130225150, "v": 3130225148, "osmid": 490601246, "highway": "path", "width": "3", "oneway": false, "length": 20.657}, "geometry": {"type": "LineString", "coordinates": [[-75.7624639, 45.34552], [-75.7626907, 45.3454246]]}}]}

const MAPBOX_TOKEN = "pk..p3JMZyTUTGmMuXk-TKraog"

const layerStyle = {
  id: 'layerForPath',
  type: 'line',
  paint: {
    'line-color': '#007cbf',
    'line-width': 4,
  },
  layout: {
    'line-cap': 'round'
  }
};

function App() {
  return (
    <div className="MapApp">
      <Map
        initialViewState={{
          longitude: -75.76,
          latitude: 45.34,
          zoom: 14
        }}
        // className="Map"
        styles={{width: 800, height: 400}}
        mapStyle="mapbox://styles/mapbox/streets-v9"
        mapboxAccessToken={MAPBOX_TOKEN}
      >
        <Marker longitude={-75.76992997643495} latitude={45.34365181227424} color="red"/>
        <Source id="my-data" type="geojson" data={geojsondata}>
          <Layer {...layerStyle} />
        </Source>
      </Map>

    </div>
  );
}

export default App;
      // {/* <img src="https://phantom-marca.unidadeditorial.es/b156931cfe86ee1ea7e9807400c29cdd/resize/660/f/webp/assets/multimedia/imagenes/2022/07/12/16576470696919.jpg"/> */}
