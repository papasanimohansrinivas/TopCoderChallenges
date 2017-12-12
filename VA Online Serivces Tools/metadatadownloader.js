var y = require('download-file');


var url = "https://www.data.va.gov/data.json";

options = {

	directory :"./metadata",
	filename :"metadata_1.json"
}

// console.log(process.argv.slice(1));


y(url,options);
