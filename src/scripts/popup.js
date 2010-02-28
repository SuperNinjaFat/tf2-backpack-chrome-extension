var itemContentSelector = "#unplaced table.unplaced td img, #backpack table.backpack td img, span.equipped";


var backpack = {
    feed: null,
    defs: null,

    init: function() {
	this.loadItemDefs();
	this.loadAndShow();
    },

    loadItemDefs: function() {
	var req = new XMLHttpRequest();
	var self = this;
	req.onreadystatechange = function() {
	    if (req.readyState == 4) {
		self.defs = JSON.parse(req.responseText);
	    }
	}
	req.open("GET", chrome.extension.getURL("data/items.json"), false);
	req.send();
    },

    loadAndShow: function () {
	var xml = storage.cachedFeed();
	var self = this;
	if (xml) {
	    $(itemContentSelector).fadeOut().remove();
	    window.setTimeout(function() {
	    self.feed = (new DOMParser()).parseFromString(xml, "text/xml");
	    pageOps.putItems(self.feed);
	    pageOps.putCharInfo(self.feed);
	    }, 150)
	} else {
	    // handle empty
	}
    },
};


var pages = {
    current: 1,
    count: 1,

    init: function() {
	this.count = $("#backpack table.backpack tbody").length;
	this.current = 1 + $("#backpack tbody").filter(":visible").index();
	this.updateNav();
	$(".nav:first a").live("click", function (e) {return pages.nav(e, -1)});
	$(".nav:last a").live("click",  function (e) {return pages.nav(e, 1)});
    },

    nav: function(event, offset) {
	if (event.detail != 1) { return }
	var self = this;
	if ((self.current + offset) > 0 && (self.current + offset <= self.count)) {
	    $("#backpackPage-" + self.current).fadeOut(250, function() {
		self.current += offset;
		$("#backpackPage-" + self.current).fadeIn(250);
		self.updateNav();
	    });
	}
	return false;
    },

    updateNav: function () {
	$("#pages").text(this.current + "/" + this.count);
	if (this.current == 1) {
	    $(".nonav:first").show();
	    $(".nav:first").hide();
	} else {
	    $(".nonav:first").hide();
	    $(".nav:first").show();
	}
	if (this.current == this.count) {
	    $(".nonav:last").show();
	    $(".nav:last").hide();
	} else {
	    $(".nonav:last").hide();
	    $(".nav:last").show();
	}
    },
};


var showTab = {
    externalBackpack: function() {
	return this.open(this.isTF2ItemsUrl, profile.backpackViewUrl());
    },

    steamProfile: function() {
	return this.open(this.isSteamCommunityProfileUrl, profile.communityUrl());
    },

    sourceOp: function() {
	return this.open(this.isSourceOpUrl, urls.sourceOp);
    },

    pnaturalProfile: function() {
	return this.open(this.isPnaturalUrl, urls.pnatural);
    },

    options: function() {
	chrome.tabs.create({url:"./options.html"});
	window.close();
	return false;
    },

    isTF2ItemsUrl: function (url) {
	var urlItems = profile.backpackViewUrl();
	if (url.indexOf(urlItems) != 0) {
	    return false;
	}
	return url.length == urlItems.length ||
            url[urlItems.length] == "?" ||
	    url[urlItems.length] == "#";
    },

    isSteamCommunityProfileUrl: function (url) {
	var urlProfile = urls.steamCommunity + "profiles/" + storage.profileId();
	return (url.indexOf(urlProfile) == 0);
    },

    isSourceOpUrl: function (url) {
	return (url.indexOf(urls.sourceOp) == 0);
    },


    isPnaturalUrl: function (url) {
	return (url == urls.pnatural);
    },

    open: function(match, newUrl) {
	chrome.tabs.getAllInWindow(undefined,
            function(tabs) {
                for (var i = 0, tab; tab = tabs[i]; i++) {
                    if (tab.url && match(tab.url)) {
		        window.close();
                        chrome.tabs.update(tab.id, {selected:true});
                        return false;
                    }
                }
	        window.close();
                chrome.tabs.create({url:newUrl});
	        return false;
            });
    },

};


var pageOps = {
    init: function() {
	chrome.extension.onRequest.addListener(this.refreshHandler);
	$("table.unplaced td:has(img)")
	    .live("mouseenter", function() {$(this).addClass("itemHover")})
	    .live("mouseleave", function() {$(this).removeClass("itemHover")});
        $("body").mousedown(function(){return false}) //disable text selection
	$("#toolbar").css("width", -6 + Math.max(400, $("#backpack tr:first").width()));
	$("table.backpack td").click(this.itemClicked);
	$("table.backpack td, table.unplaced td")
            .live("mouseenter", showToolTip)
            .live("mouseleave", hideToolTip);
    },

    refreshHandler: function(request, sender, response) {
	switch(request.type) {
	case "okay":
	    console.log("popup received refresh complete msg");
	    backpack.loadAndShow();
	    pages.init();
	    $("#error").text(Date().split(" ", 5).join(" ")).fadeIn();
	    break;
	case "fail":
	    console.log("popup received refresh failed msg");
	    break;
	default:
	    console.log("unknown refresh msg");
	}
	response({});
    },

    itemImage: function(t) {
	return "<img style='display:none' src='icons/"+t+".png' onerror='pageOps.missingImage(this, "+t+")' />"
    },

    itemClicked: function(event) {
	if (!event.ctrlKey) {
	    $("table.backpack td").removeClass("selected");
	}
	$(this).addClass("selected");
    },

    requestRefresh: function(event) {
	chrome.extension.sendRequest({type:"feedRefresh"}, function(response) {} );
	return false;
    },

    missingImage: function(img, typ) {
	if (img) {
	    img.src = "icons/missing.png";
	    img.onerror = null;
	    return true;
	}
    },

    showStats: function() {
	$("#stats").fadeIn();
	$("#controls a:contains('Stats')").fadeOut();
	return false;
    },

    putCharInfo: function(feed) {
	$("#steamID a").text($("steamID", feed).text());
	var avatarUrl = $("avatarFull", feed).text();
	if (avatarUrl) {
	    $("#avatar img").fadeOut().remove();
	    $("#avatar").append("<img src='" + avatarUrl + "' />");
	}
	$(["numHats", "numNormal", "numMisc",
	   "numMetal", "numUnknown", "totalItems",
	   "metalWorth"]).each(function(index, key) {
	       $("#"+key).text( $("backpack "+key, feed).text() );
	});
    },

    putNewItem: function(index, node) {
	var type = $(node).attr("definitionIndex");
	if (!type) {
	    return;
	}
	if ($("table.unplaced td:not(:has(img))").length == 0) {
	    var cells = new Array(5+1).join("<td><div></div></td>");
	    $("table.unplaced").append("<tbody><tr>" + cells + "</tr></tbody>");
	}
	$("table.unplaced td:eq("+index+") div").append(pageOps.itemImage(type));
	$("table.unplaced td img:last").data("node", node);
    },

    putOldItem: function(index, node) {
	var pos = $("position", node).text();
	var type = $(node).attr("definitionIndex");
	var element = $("#c" + (pos & 0xffff) + " div");
	element.append(pageOps.itemImage(type));
	var img = $("img:last", element);
	img.data("node", node);
	if (pos & 0x80000000 && pos & 0x0FFF0000) {
	    // nudge the image up a bit; related to margin-top on the equipped class
	    img.css("margin-top", "-5px");
	    img.after("<span style='display:none' class='equipped'>Equipped</span>");
	}
    },

    putItems: function(feed) {
	$("#unplaced table.unplaced td img, #backpack table.backpack td img").fadeOut().remove();
	$("span.equipped").fadeOut().remove();
	if (!feed) {
	    console.log("empty feed");
	    return;
	}
	var newNodes = $("item", feed).filter(
	    function (index) { return $("position", this).text() == "0" }
	).each(this.putNewItem);

	$("#unplaced, hr.unplaced").toggle(newNodes.length > 0);

	$("item", feed).filter(
	    function (index) { return $("position", this).text() != "0" }
	).each(this.putOldItem);

	$("#unplaced td img, #backpack td img, span.equipped").fadeIn(750);
    },

};


function showToolTip(event) {
    var cell = $(this), tooltip = $("#tooltip");
    if (!cell.children().length) {
	return;
    }
    try {
	var node = $( $("img", cell).data("node") );
	var type = node.attr("definitionIndex");
	var item = backpack.defs[type];
	var levelType = item.type;
	var level = $("level", node).text();
    } catch (e) {
	return;
    }
    tooltip.hide().css({left:0, top:0});
    $("#tooltip h4").text(item.description).removeClass("valve community");
    $("#tooltip .level").text("Level " + level + (levelType ? " " + levelType : ""));

    // special formatting valve and community weapons
    var extras = [];
    var attrMap = {};
    $.each($("attributes attribute", node), function(index, value) {
	var index = $(value).attr("definitionIndex");
        var format = backpack.defs["other_attributes"][index] || "";
	if (format) {
	    extras.push( format.replace("%s1", $(value).text()) );
	}
	attrMap[index] = $(value).text();
    });
    if (item["alt"]) {
	item["alt"].concat(extras);
    } else if (extras) {
	item["alt"] = extras;
    }
    if (attrMap["134"] == "2") {
	$("#tooltip h4").text($("#tooltip h4").text().replace("The ", ""));
	$("#tooltip h4").addClass("valve");
    } else if (attrMap["134"] == "4") {
	$("#tooltip h4").text($("#tooltip h4").text().replace("The ", ""));
	$("#tooltip h4").addClass("community");
    }

    // add the various descriptions
    $(["alt", "positive", "negative"]).each(function(index, key) {
	if (item[key]) {
	    var value = item[key].join("<br />");
	    $("#tooltip ." + key).html(value).show();
	} else {
	    $("#tooltip ." + key).text("").hide();
	}
    });
    tooltip.show().hide();
    // position and show the tooltip
    var pos = cell.position();
    var minleft = cell.parent().position().left;
    var cellw = cell.width();
    var toolw = tooltip.width();
    var left = pos.left - (toolw/2.0) + (cellw/2.0) - 4; // 4 == half border?
    left = left < minleft ? minleft : left;
    var maxright = cell.parent().position().left + cell.parent().width();
    if (left + toolw > maxright) {
    	left = cell.position().left + cellw - toolw - 12;
    }
    left = left < 0 ? (window.innerWidth/2)-toolw/2 : left;
    var top = pos.top + cell.height() + 12;
    if (top + tooltip.height() > (window.innerHeight+window.scrollY)) {
    	top = pos.top - tooltip.height() - 36;
    }
    tooltip.css({left:left, top:top});
    tooltip.show();
}


function hideToolTip(event) {
    $("#tooltip").hide();
}


function popupInit() {
    if (!storage.profileId()) {
        $("body > *:not(#unknownProfile)").hide()
	$("#unknownProfile").show();
	optionsAltInit();
	return;
    }
    pages.init();
    backpack.init();
    pageOps.init();
    $("#error").text(Date().split(" ", 5).join(" ")).fadeIn();
}

