# -*- coding: utf-8 -*-
CHANNEL_URL = 'http://www.tvcatchup.com/watch.html?c=%d'
ICON_URL    = 'http://images-cache.tvcatchup.com/NEW/images/channels/hover/channel_%d.png'

####################################################################################################

def Start():
  Plugin.AddPrefixHandler('/video/tvcatchup', MainMenu, 'TVCatchup', 'icon-default.png', 'art-default.jpg')
  Plugin.AddViewGroup('InfoList', viewMode='InfoList', mediaType='items')
  MediaContainer.art = R('art-default.jpg')
  HTTP.Headers['User-agent'] = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.10) Gecko/20100914 Firefox/3.6.10'

####################################################################################################

def MainMenu():
  dir = MediaContainer(viewGroup='InfoList', title1='TVCatchup Channel List')
  for channel in Dict['channels']:
    channel_id, channel_name = channel
    dir.Append( WebVideoItem( CHANNEL_URL % (channel_id), title=channel_name, thumb=Function(GetThumb, channel_id=channel_id) ) )

  dir.Append(PrefsItem('Settings', thumb=R('icon-prefs.png')))
  return dir

####################################################################################################

def GetThumb(channel_id):
  try:
    data = HTTP.Request( ICON_URL % (channel_id), cacheTime=CACHE_1MONTH).content
    return DataObject(data, 'image/png')
  except:
    return Redirect(R('icon-default.png'))
