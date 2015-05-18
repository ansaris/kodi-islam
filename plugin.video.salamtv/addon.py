import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

guideustvurl = 'http://salam/strm/__GuideUS_tv__.strm'
guideusimg = "http://salam/strm/guideustv.jpg"
guideustv = xbmcgui.ListItem('GuideUS TV', iconImage=guideusimg, thumbnailImage=guideusimg)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=guideustvurl, listitem=guideustv)

peacetvurduurl = "http://salam/strm/__Peace_TV_URDU__.strm"
peacetvurduimg = "http://salam/strm/peacetvurdu.jpg"
peacetvurdu = xbmcgui.ListItem('Peace TV Urdu', iconImage=peacetvurduimg, thumbnailImage=peacetvurduimg)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=peacetvurduurl, listitem=peacetvurdu)

peacetvukurl = "http://salam/strm/__Peace_TV_UK__.strm"
peacetvimg = "http://salam/strm/peacetv.jpg"
peacetvuk = xbmcgui.ListItem('Peace TV UK', iconImage=peacetvimg, thumbnailImage=peacetvimg)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=peacetvukurl, listitem=peacetvuk)

peacetvusaurl = "http://salam/strm/__Peace_TV_USA__.strm"
peacetvusaimg = "http://salam/strm/peacetv.jpg"
peacetvusa = xbmcgui.ListItem('Peace TV USA', iconImage=peacetvusaimg, thumbnailImage=peacetvusaimg)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=peacetvusaurl, listitem=peacetvusa)

xbmcplugin.endOfDirectory(addon_handle)