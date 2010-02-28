var alsoRefresh = false;


function markDirty() {
    $("#save").attr("disabled", false);
}


function markClean() {
    $("#save").attr("disabled", true);
}


function save() {
    var newProfileId = $("#profileId").attr("value");
    if (newProfileId == storage.profileId()) { return; }

    profile.search(newProfileId,
    function(lookupId) {
	if (newProfileId != lookupId) {
	    $("#msg").text("Using SteamID " + lookupId + " for " + newProfileId + ".")
	        .fadeIn()
	        .delay(5000)
	        .fadeOut();
        }
        $("#profileId").attr("value", lookupId);
        storage.profileId(lookupId);
	//what?
	//chrome.extension.getBackgroundPage().backgroundInit();
	if (alsoRefresh) {
            $("body > *:not(#unknownProfile)").fadeIn();
	    hideToolTip();
	    $("#unknownProfile").fadeOut();
	    popupInit();
	}
    },
    function() {
	$("#profileId").select().focus();
	$("#msg").text("SteamID not found.  Please try again.").fadeIn().delay(5000).fadeOut();
    });
}


function optionsInit() {
    $("#profileId").attr("value", storage.profileId());
    $("#profileId").change(markDirty).keypress(markDirty);
    $("#save").click(save);
    $("#cancel").click(optionsInit);
    markClean();
}


function optionsAltInit() {
    alsoRefresh = true;
    $("#profileId").attr("value", storage.profileId());
    $("#profileId").change(markDirty);
    $("#save").click(save);
    $("#cancel").click(optionsAltInit);
    $("#unknownProfile input:first").select();
    markDirty();
}

