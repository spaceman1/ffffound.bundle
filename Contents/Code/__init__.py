PLUGIN_PREFIX   = "/photos/fffound"
RSS_FEED        = "http://feeds.feedburner.com/ffffound/everyone"

####################################################################################################

def Start():
	Plugin.AddPrefixHandler(PLUGIN_PREFIX, HandlePhotosRequest, "FFFFOUND!", "icon-default.png", "art-default.jpg")
	Plugin.AddViewGroup("ImageStream", viewMode="ImageStream", mediaType="items")
	MediaContainer.art = R("art-default.jpg")
	MediaContainer.viewGroup = 'ImageStream'
	
####################################################################################################
def HandlePhotosRequest():
	dir = MediaContainer(title1="FFFFOUND!")
	
	for item in RSS.FeedFromURL(RSS_FEED).entries:
		node = HTML.ElementFromString(item.summary)
		img = node.xpath("//img")[0].get('src')
		dir.Append(PhotoItem(img, title=item.title, thumb=img))

	return dir
