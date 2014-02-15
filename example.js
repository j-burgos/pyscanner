/* 
* This function does something
*/

Date d = new Date();

function something(){
	$.ajax({
		url: "/something",
		method: "POST"
	}).done(function(){
		while(1)
			alert("done");
	});
	~
}




