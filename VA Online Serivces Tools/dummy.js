var fs = require('fs');



var dir = require('node-dir');


var ass = [];

var filenames = dir.files('..\\VA Online Serivces Tools\\cemetry data\\cemetry data 1',{sync:true});


// console.log(filenames.length);


var call = function(dirname){


	var f= fs.readFileSync(dirname).toString();


	var rowstrings=f.split('\n');


	csv_rows = [];

	for(var u=0;u<rowstrings.length;u++){
		csv_rows.push(rowstrings[u].split(','));
	}

	// console.log(csv_rows.length);

}

for(k in filenames){
	// console.log(filenames[k]);
	call(filenames[k]);
}


// call("../VA Online Serivces Tools/cemetry data/cemetry data 1/ngl_wyoming_0.csv")