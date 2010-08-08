function InitTopMenu() {
    function menuHoverOver() {
        var td = $j(this);
        var div = $j(this).children("div");
        var a = div.children("a");

        a.addClass("hover");
        td.addClass("hover");

        var dd = $j(".ddm." + td.attr("id"));
        if (dd.length > 0) {
            
            dd.addClass("hover");
            
            //if (!dd.hasClass("ddInitialized")) {
                childrenWidth = 0;
                dd.children().each(function() { childrenWidth += $j(this).outerWidth(); });
                dd.css("width", childrenWidth);
                calculateDropDownPosition(td, div, dd);
                
                dd.mouseover(function() {
                    td.triggerHandler("mouseover");
                }).mouseout(function() {
                    td.triggerHandler("mouseout");
                });
                //dd.addClass("ddInitialized");
            //}   
        }

    }


    function calculateDropDownPosition(topMenuCell, divContainer, dropDownDiv) {

        var a = topMenuCell.children("a");
        dropDownDiv.css("top", topMenuCell.height() + topMenuCell.position().top + "px");
        dropDownDiv.css("position", "absolute");

        var iPosLeft = a.position().left;
        var iMenuRightEdge = 0;

//        var c = topMenuCell.parent('tr').children();
//        var lastMenuItem = c[c.length - 1];
//        iMenuRightEdge = $j(lastMenuItem).outerWidth() + $j(lastMenuItem).position().left;

        var divTopMenu = $j("#divTopMenu");
        var iMenuRightEdge = divTopMenu.position().left + divTopMenu.width();
        if (iPosLeft + dropDownDiv.width() > iMenuRightEdge) {
            iPosLeft = topMenuCell.position().left - (dropDownDiv.outerWidth() - topMenuCell.outerWidth());
        }
        else if (iPosLeft < 0) {
            iPosLeft = 0;
        }

        if (iPosLeft < 0) {
            iPosLeft = divTopMenu.width() - dropDownDiv.width();
        }
        
        dropDownDiv.css("left", iPosLeft + "px");

    }

    function menuHoverOut() {
        var td = $j(this);
        var div = $j(this).children("div");
        var a = $j(this).children("a");
        a.removeClass("hover");
        td.removeClass("hover");

        var dd = $j(".ddm." + td.attr("id"));
        if (!dd.hasClass("hovering"))
            dd.removeClass("hover");
    }

    var hoverConfig = {
        interval: 50,
        sensitivity: 12,
        over: menuHoverOver,
        timeout: 100,
        out: menuHoverOut
    };

    
    $j("#divTopMenu td").hoverIntent(hoverConfig);
}