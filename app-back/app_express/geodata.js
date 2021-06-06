//*Use the require function to read the json file. Will return the json data as a js method.
//? this is a synchronous function, fs.ReadFil is async and will not block program (notes for future)
/* const geo_data = require("../../Data/brazil-states.geojson");
const j_geo = require("../../Data/brazol.json");
console.log(j_geo);
 */
var fs = require("fs");

fs.readFile("../../Data/brazil-states.geojson", "utf8", function (err, data) {
  if (err) throw err; // we'll not consider error handling for now
  var obj = JSON.parse(data);
  console.log(obj);
});
