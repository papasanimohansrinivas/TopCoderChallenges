var metadata=require('./metadata/metadata.json');


function satisfactory_conditions(dataset){
	if (dataset.programCode[0]=="029:001"){
		if (dataset.keyword.includes("burial data")){

			distributions = dataset.distribution
			for (var t = 0 ; t<distributions.length;t++ ){
				if(distributions[t].format=='csv'){
					// console.log(distributions[t].downloadURL+"  "+distributions[t].accessURL);
					// console.log("\n")
					if(distributions[t].downloadURL!=undefined){

						return {'index':t,'url':distributions[t].downloadURL};	
					}
					// return {'index':t,'url':distributions[t].downloadURL};
				}
			}
		}
		else{
			return false;
		}

	}
	else{
		return false;
	}
}
var list =  metadata.dataset

var ee = 0;

files_to_download = []

var xx = 0;

for (var i = 0; i < list.length; i++) {
	var res = satisfactory_conditions(list[i]);
	if (res){
		// console.log(res);
		ee+=1;
		files_to_download.push(res.url);
	}
	distributions = list[i].distribution;
	if (distributions!= undefined){

		for (var t = 0 ; t<distributions.length;t++ ){
			if(distributions[t].format=='csv'){
				if (list[i].distribution[t].downloadURL || list[i].distribution[t].accessURL){
					xx+=1;

					console.log(list[i].distribution[t].downloadURL+" "+list[i].distribution[t].accessURL);
				}
				// return {'index':t,'url':distributions[t].downloadURL};
			}
		}

	}
	// console.log(list[i].distribution[0].downloadURL);
}

console.log(xx);
console.log(files_to_download.length);

var downloadurl = require('download-file');

function download(){
	var daetetime = new Date();

	var index = 0;

	while(index<files_to_download.length){



		var options = {

			directory:'./cemetry data/cemetry data '+1,
			filename:'file_'+index+'.csv'
		}

		if(files_to_download[index] != undefined){

			downloadurl(files_to_download[index],options,function(err){

				if(err){
					throw err;
				}
				console.log(err+" file name is "+files_to_download[index]+index);
			});
			console.log("downloaded file "+" "+files_to_download[index]+"  "+index);
			console.log(files_to_download.length);


		}

		index=index+1;

	}
	

}

// download();
