var fs = require('fs');
var readline = require('readline');
var stream = require('stream');

var instream = fs.createReadStream('just.txt');
var outstream = new stream;
var rl = readline.createInterface(instream, outstream);


rl.dummy = []

var array = [];
rl.on('line', function(line) {
  // process line here
  console.log(line);
  rl.dummy.push(line); 
});

rl.on('close', function(line) {
  // do something on finish here
   array.push(line);

});


console.log(rl.dummy.length);