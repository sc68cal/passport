/*
Library meant for easy to use Javascript functions to add dynamic content to Sitecore Sites utilizing jQuery
*/
var $j = jQuery.noConflict();

var drexel = {
    HideShow: function(toggleID) {
        $j("#" + toggleID).toggle();
    },

	Toggle: {
		Init: function() {
			$j(".DUToggle").click(function() {
				if($j(this).attr("DUTarget") != "")
				{
					$j("#" + $j(this).attr("DUTarget")).toggle();
				}
				return false;
			});
		}
	},
	
	Accordion: {
		Init: function() {
			$j(".DUAccordion").click(function() {
				if($j(this).hasClass("open"))
				{
					$j(this).removeClass("open");
				}
				else
				{
					$j(this).addClass("open");
				}
				$j(this).next('div').toggle();
				return false;
			}).next('div').hide();
			$j(".DUAccordion.open").next('div').toggle();
		}
	},
	
	AccordionOnePane: {
		Init: function() {
			$j(".DUAccordionOnePane").click(function() {
				if($j(".DUAccordionSpacer").length > 0 && $j(".DUAccordionSpacer.closed").length < 1)
				{
					$j(".DUAccordionSpacer").addClass("closed").slideUp(425);
				}
				if($j(this).hasClass("open"))
				{
					$j(this).removeClass("open");
					
					if($j(".DUAccordionSpacer").length > 0 && $j(".DUAccordionSpacer.closed").length > 0)
					{
						//$j(".DUAccordionSpacer.closed").removeClass("closed").slideDown(400);
						$j(".DUAccordionSpacer.closed").removeClass("closed").show()
						$j(this).next('div').hide();
					}
					else
					{
						$j(this).next('div').slideUp(400);
					}
				}
				else
				{
					$j(".DUAccordionOnePane.open").removeClass("open").next('div').slideUp(410);
					$j(this).addClass("open");
					$j(this).next('div').slideDown(400);
				}
				
				return false;
			}).next('div').hide();
		}
	},
	
    Hover: {
        Init: function() {
            drexel.Hover.Preload();

            $j(".DUHover").hover(
				function() { $j(this).attr('src', drexel.Hover.NewImage($j(this).attr('src'))); },
				function() { $j(this).attr('src', drexel.Hover.OldImage($j(this).attr('src'))); }
			);
        },

        Preload: function() {
            $j(window).bind('load', function() {
                $j('.DUHover').each(function(key, elm) {
                    var sHoverImage = drexel.Hover.NewImage($j(this).attr('src'));
                    var currObj = $j(this);

                    var imageTest = new Image();
                    imageTest.onerror = function() {
                        $j(currObj).removeClass("DUHover");
                        $j(currObj).unbind("mouseenter").unbind("mouseleave");
                    };
                    imageTest.onload = function() {
                        $j('<img>').attr('src', sHoverImage);
                    };
                    imageTest.src = sHoverImage;
                });
            });
        },

        NewImage: function(src) {
            var iExtensionPoint = src.search(".ashx");
            return src.substring(0, iExtensionPoint) + '_hover' + src.substring(iExtensionPoint);
        },

        OldImage: function(src) {
            return src.replace(/_hover\./, '.');
        }
    },

    EnlargeImageHover: function() {
        $j(".DUEnlargeImage").parent().hover(
			function() { $j(this).children(".DUEnlargeImage").attr('src', 'images/enlarge-image-hover.gif'); },
			function() { $j(this).children(".DUEnlargeImage").attr('src', 'images/enlarge-image.gif'); }
		);
    },

    SacramentoSearchBox: function() {
        location.href = "http://sacramento.drexel.edu/search.aspx?q=" + escape(document.getElementById("textTopMenuSearch").value);
    },
	
	FacilitiesBuildingMenu: function(selObj) {
		window.open("http://deptapp.drexel.edu/facilities/design/pages/buildings.asp?BID=" + selObj.options[selObj.selectedIndex].value, "_blank");
	},
	
	IFrame: {
		Build: function() {
			var sUrl = $j(".DUIFrame").text();
			var height = '1400';
			var scroll = 'no';
			if($j(".DUIFrame").hasClass("DUFrame2400")) {
				height = '2400';
			}
			else if($j(".DUIFrame").hasClass("DUFrame34000")) {
				height = '34000';
			}
			else if($j(".DUIFrame").hasClass("DUFrame1000")) {
				height = '1000';
			}
			
			if($j(".DUIFrame").hasClass("DUFrameScroll")) {
				scroll = 'auto';
			}
		
			$j(".DUIFrame").before('<iframe src="' + sUrl +'" id="DUIFrame" frameborder="0" scrolling="'+ scroll +'" style="background-color: transparent; width: 100%; height: ' + height + 'px;" allowtransparency="true"></iframe>');
			$j(".DUIFrame").remove();
		},
		
		Size: function() {
			return true;
		}
	}
}

$j(document).ready(function() {
    $j("ul:not(:has(li))").remove();

    iBox.setPath('/sc_scripts/ibox/');
    // If an object has the class DUHover, make our magic happen
    if ($j('.DUHover').length > 0) {
        drexel.Hover.Init();
    }

    // If an object has the class DUEnlargeImage, make our magic happen
    if ($j('.DUEnlargeImage').length > 0) {
        drexel.EnlargeImageHover();
    }

    // If an object with the mediaPlayer class exists, include the needed JS file and initiate them
    if ($j('.mediaPlayer').length > 0) {
        $j.getScript("/sc_scripts/jquery.media.js", function() {
            $j('.mediaPlayer').media();
        });
    }

    if ($j('.DUTabs').length > 0) {
        // If the tabs function exists already, no need to load another jquery UI....
        if (typeof $j('').tabs == 'function') {
            $j('.DUTabs').tabs();
        }
        else {
            $j.getScript("/sc_scripts/jquery-ui-1.6.custom.min.js", function() {
                $j('.DUTabs').tabs();
            });
        }
    }

    if ($j('.DUCorner').length > 0) {
        $j.getScript("/sc_scripts/jquery.corner.js", function() {
            $j('.DUCorner').corner();
        });
    }

    if ($j("#sac-footer").length > 0) {
        $j("#lnkSearch").attr("href", "javascript: drexel.SacramentoSearchBox();");

        var sb = document.getElementById("textTopMenuSearch");
        sb.onkeypress = null;
        $j('#textTopMenuSearch').keyup(function(e) {
            //alert(e.keyCode);
            if (e.keyCode == 13) {
                drexel.SacramentoSearchBox();
            }
        });
    }
	
	if($j(".DUVendors.AndLogic").length > 0)
	{
		$j.getScript("/sc_scripts/table-sort-and-logic.js");
		$j('head').prepend("<link id=\"table-sort-stylesheet\" href=\"/sc_styles/procurement-vendor.css\" rel=\"stylesheet\">");
	}
	else if($j(".DUVendors").length > 0)
	{
		$j.getScript("/sc_scripts/table-sort.js");
		$j('head').prepend("<link id=\"table-sort-stylesheet\" href=\"/sc_styles/procurement-vendor.css\" rel=\"stylesheet\">");
	}
	
	if($j(".DUPhotoGallery").length > 0)
	{
		$j('head').prepend("<link id=\"jquerylightbox\" href=\"/sc_styles/jquery.lightbox-0.5.css\" rel=\"stylesheet\">");
		$j.getScript("/sc_scripts/jquery.lightbox-0.5.min.js", function() {
			$j(".DUPhotoGallery a.DUPhoto").lightBox();
		});
	}
	
	if($j(".DUAccordion").length >0)
	{
		drexel.Accordion.Init();
	}
	
	if($j(".DUAccordionOnePane").length > 0)
	{
		drexel.AccordionOnePane.Init();
	}
	
	if($j(".DUToggle").length >0)
	{
		drexel.Toggle.Init();
	}
	
	
	if($j(".FeebackFormPageField input.scfSingleLineTextBox").length > 0)
	{
		$j(".FeebackFormPageField input.scfSingleLineTextBox").val(document.referrer.toLowerCase());
	}
	
	if($j(".FeedbackFormPageField input.scfSingleLineTextBox").length > 0)
	{
		$j(".FeedbackFormPageField input.scfSingleLineTextBox").val(document.referrer.toLowerCase());
	}
	
	if($j("div.CheckListDisableOtherTextBox").length > 0)
	{
		$j("div.OtherBoxDisable input").attr("disabled", "disabled");
		$j("div.CheckListDisableOtherTextBox td:last input").click(function () {
			if($j("div.CheckListDisableOtherTextBox td:last input").is(":checked"))
			{
				$j(this).parents("div.CheckListDisableOtherTextBox").next("div.OtherBoxDisable").children("div").children("input").attr("disabled", "");
			}
			else
			{
				$j(this).parents("div.CheckListDisableOtherTextBox").next("div.OtherBoxDisable").children("div").children("input").attr("disabled", "disabled");
			}
		});
	}
	
	if($j(".DUIFrame").length >0)
	{
		drexel.IFrame.Build();
	}
});