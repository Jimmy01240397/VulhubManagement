var allvulns = null;

axios.get("/list")
    .then( (res) => {
        allvulns = res.data;
	var ul = document.getElementById("allvulns");
	
	allvulns.forEach(function(item, i) {
	    var li =document.createElement("li");
	    ul.appendChild(li);
	    var form = document.createElement("form");
	    form.method = "post";
	    form.action = "/vuldetail/" + item.split('/')[2];
	    var id = item;
	    li.appendChild(form);
	    var cveid = document.createElement("input");
	    cveid.type = "hidden";
	    cveid.name = "cveid";
	    cveid.value = item;
	    form.appendChild(cveid);
	    var bt = document.createElement("button");
	    bt.type = 'submit';
	    bt.innerHTML = item.split('/')[2];
	    form.appendChild(bt);
	});
    })
    .catch( (err) => {
        console.log(err);
    });
