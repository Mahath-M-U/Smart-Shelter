var db = firebase.firestore();

function shutteropen(){
	
db.collection("SMART-SHELTER").doc("Shutter").set({
    Shutter_pos: "open"
})
.then(function() {
    console.log("Document successfully written!");
})
.catch(function(error) {
    console.error("Error writing document: ", error);
});
	var Sh_S = "SHUTTER OPEND";
document.getElementById("SHUTTER").innerHTML = Sh_S;
STATUS();
}
function shutterclose(){
	
db.collection("SMART-SHELTER").doc("Shutter").set({
    Shutter_pos: "close"
})
.then(function() {
    console.log("Document successfully written!");
})
.catch(function(error) {
    console.error("Error writing document: ", error);
});
		var Sh_S = "SHUTTER CLOSED";
document.getElementById("SHUTTER").innerHTML = Sh_S;
STATUS();		
}
		
		
function ledon(){
	
db.collection("SMART-SHELTER").doc("LIGHT").set({
    led_s: "ON"
})
.then(function() {
    console.log("Document successfully written!");
})
.catch(function(error) {
    console.error("Error writing document: ", error);
});
	var LED_S = "LIGHT STATUS : ON";
document.getElementById("LED").innerHTML = LED_S;
	SHOW();
}
			
		
function ledoff(){
	
db.collection("SMART-SHELTER").doc("LIGHT").set({
    led_s: "OFF"
})
.then(function() {
    console.log("Document successfully written!");
})
.catch(function(error) {
    console.error("Error writing document: ", error);
});
				var LED_S = "LIGHT STATUS : OFF";
document.getElementById("LED").innerHTML = LED_S;
SHOW();
	
	
}	
	
		
		
		
function rotate_fs(){
	
db.collection("SMART-SHELTER").doc("FLATFROM").set({
    flatform_value: "rotate"
})
.then(function() {
    console.log("Document successfully written!");
})
.catch(function(error) {
    console.error("Error writing document: ", error);
});
document.getElementById('fm').src='R_3.png';	
setTimeout(f1, 500)




			
function rotate_fr(){
	
db.collection("SMART-SHELTER").doc("FLATFROM").set({
    flatform_value: "STOP"
})
.then(function() {
    console.log("Document successfully written!");
})
.catch(function(error) {
    console.error("Error writing document: ", error);
});
setTimeout(f5, 500)	
}	
	
	
	
	
	

		function f1(){
			
			document.getElementById('fm').src='R_4.png';
			setTimeout(f2, 500)
		}
		function f2(){
			
			document.getElementById('fm').src='R_5.png';
			setTimeout(f3, 500)
			
		}		
	function f3(){
			
			document.getElementById('fm').src='R_6.png';
			setTimeout(f4, 500)
			
		}	
	function f4(){
			
			document.getElementById('fm').src='R_7.png';
			setTimeout(rotate_fr, 500)
		}
	function f5(){
			
			document.getElementById('fm').src='R_1.png';
			
		}	
}	
		
function OnSHOW(){

var docRef =db.collection("SMART-SHELTER").doc("LIGHT");			

docRef.get().then(function(doc) {
    if (doc.exists) {	
		var data=JSON.stringify(doc.data(),null,2);
		var str={
			"led_s": "ON"
				}
		var full= JSON.stringify(str,null,2);
		console.log("Document data:", doc.data());
		if(data === full){
		document.getElementById('myImage').src='on.png';
		}
		else
			{
				document.getElementById('myImage').src='off.png';
			}
    } else {
        // doc.data() will be undefined in this case
        console.log("No such document!");
    }
}).catch(function(error) {
    console.log("Error getting document:", error);
});	
STATUS();
}
		
		
function STATUS(){
	var docRef =db.collection("SMART-SHELTER").doc("Shutter");			

docRef.get().then(function(doc) {
    if (doc.exists) {	
		var SHD=JSON.stringify(doc.data(),null,2);
		var SHS={
			"Shutter_pos": "open"
				}
		var FI= JSON.stringify(SHS,null,2);
		console.log("Document data:", doc.data());
		if(FI === SHD){
		document.getElementById('sh').src='open.png';
		}
		else
			{
				document.getElementById('sh').src='closed.png';
			}
    } else {
        // doc.data() will be undefined in this case
        console.log("No such document!");
    }
}).catch(function(error) {
    console.log("Error getting document:", error);
});	
	
}
function SHOW(){

var docRef =db.collection("SMART-SHELTER").doc("LIGHT");			

docRef.get().then(function(doc) {
    if (doc.exists) {	
		var data=JSON.stringify(doc.data(),null,2);
		var str={
			"led_s": "ON"
				}
		var full= JSON.stringify(str,null,2);
		console.log("Document data:", doc.data());
		if(data === full){
		document.getElementById('myImage').src='on.png';
		}
		else
			{
				document.getElementById('myImage').src='off.png';
			}
    } else {
        // doc.data() will be undefined in this case
        console.log("No such document!");
    }
}).catch(function(error) {
    console.log("Error getting document:", error);
});	
}	