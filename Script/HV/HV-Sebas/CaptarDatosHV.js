function obtener(){
	var url= location.search.replace("?", "");
	//url= location.search.replace("+", " ");
	var arrUrl = url.split("&");
	var urlObj={};   
	for(var i=0; i<arrUrl.length; i++){
		var x= arrUrl[i].split("=");
		urlObj[x[0]]=x[1]
	}
	return urlObj;
}
function escribir(){
	var misVariablesGet = obtener();
		document.getElementById("Nombre").innerHTML = misVariablesGet.Nombre;
		document.getElementById("Inde").innerHTML = misVariablesGet.Inde;
		document.getElementById("Nac").innerHTML = misVariablesGet.Nac;
		document.getElementById("EsCv").innerHTML = misVariablesGet.EsCv;
		document.getElementById("Dir").innerHTML = misVariablesGet.Dir;
		document.getElementById("Tel").innerHTML = misVariablesGet.Tel;
		document.getElementById("EsSec").innerHTML = misVariablesGet.EsSec;
		document.getElementById("EsUn").innerHTML = misVariablesGet.EsUn;
		document.getElementById("EsCom").innerHTML = misVariablesGet.EsCom;
		document.getElementById("Exp").innerHTML = misVariablesGet.Exp;
		document.getElementById("RefLab").innerHTML = misVariablesGet.RefLab;
		document.getElementById("RefPer").innerHTML = misVariablesGet.RefPer;
		document.getElementById("Fir").innerHTML = misVariablesGet.Fir;
		document.getElementById("Fecha").innerHTML = misVariablesGet.Fecha;
}