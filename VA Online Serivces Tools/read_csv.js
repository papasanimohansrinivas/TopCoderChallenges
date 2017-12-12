var fs = require('fs');



var dir = require('node-dir');


var ass = [];

var filenames = dir.files('..\\VA Online Serivces Tools\\cemetry data\\cemetry data 1',{sync:true});


// console.log(filenames.length);

var num = 0;
var call = function(dirname){


	var f= fs.readFileSync(dirname).toString();


	var rowstrings=f.split('\n');


	csv_rows = [];

	for(var u=0;u<rowstrings.length;u++){
		csv_rows.push(rowstrings[u].split(','));
		// console.log(rowstrings[u].split(',').length);
	}
	num+=csv_rows.length;
	// console.log(csv_rows[0]);

}

for(k in filenames){
	// console.log(filenames[k]);
	call(filenames[k]);
}

console.log("number of rows "+num)
