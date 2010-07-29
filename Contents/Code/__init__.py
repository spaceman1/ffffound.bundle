from PMS import Plugin, Log, DB, Thread, XML, HTTP, JSON, RSS, Utils
from PMS.MediaXML import MediaContainer, DirectoryItem, PhotoItem

PLUGIN_PREFIX   = "/photos/fffound"
RSS_FEED        = "http://feeds.feedburner.com/ffffound/everyone"

####################################################################################################
def Start():
  Plugin.AddRequestHandler(PLUGIN_PREFIX, HandlePhotosRequest, "FFFFOUND!", "icon-default.png", "art-default.jpg")
  Plugin.AddViewGroup("ImageStream", viewMode="ImageStream", contentType="items")

####################################################################################################
def HandlePhotosRequest(pathNouns, count):
  dir = MediaContainer("art-default.jpg", "ImageStream", "FFFFOUND!")
  
  if count == 0:
    for item in RSS.Parse(RSS_FEED).entries:
      node = XML.ElementFromString(item.summary, True)
      img = node.xpath("//img")[0].get('src')
      dir.AppendItem(PhotoItem(img, item.title, '', img))

  return dir.ToXML()
