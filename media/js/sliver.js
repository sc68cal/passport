function $sliver(el) {
  return document.getElementById(el);
}
function InitSearch() {
	try
	{
		var sb = $sliver("tbSearch");
    
		sb.onfocus = function() {
			if (sb.value.toLowerCase() == "search...") sb.value = "";    
		}
		sb.onblur = function() {
			if (sb.value == "") sb.value = "Search...";
		}
		sb.onkeypress = Search;
	}
	catch(err)
	{
	
	}
}

function SearchClick() {
    location.href = "http://www.drexel.edu/search.aspx?q=" + escape(document.getElementById("tbSearch").value);
}

function Search(e) {
    var d = "http://www.drexel.edu/search.aspx?q=";
    var keyCode;
    var source;
    
    if (!e) var e = window.event;
    
    keyCode = e.keyCode ? e.keyCode : e.charCode;
    source = e.srcElement ? e.srcElement : e.target;
    
    if (keyCode == 13) {
        location.href = d + escape(source.value);
        return false;
    }
}
function InitHovers() {
    window.setTimeout("SetHovers()", 500);
}
function SetHovers() {
    var img_a = document.getElementsByTagName("img");
    if (!img_a) return;
    for (var x=0;x<img_a.length;x++) {
        var i = img_a[x];
        if (i.src.indexOf("blank.gif") == -1 && $j(i).hasClass("hover")) { //i.className.indexOf("hover") != -1) {
            i.onmouseover = function() {
                var arr = this.src.split(".");
                arr[arr.length-2] += "-over"; 
                this.src = arr.join(".");
            }
            i.onmouseout = function() {
                this.src = this.src.replace("-over.", ".");
            }
        }
    }
}

var _LoadEventFunctions = Array();

function AddLoadEvent(func) {
	_LoadEventFunctions[_LoadEventFunctions.length] = func;	
}
function LoadEvents() {
	for (var x=0;x<_LoadEventFunctions.length;x++) {
		var func = _LoadEventFunctions[x];
		func();	
	}
}

AddLoadEvent(InitSearch);
AddLoadEvent(InitHovers);

window.onload = LoadEvents;