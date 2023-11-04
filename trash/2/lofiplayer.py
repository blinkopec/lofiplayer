import vlc
import pafy
import time

url = "https://www.youtube.com/watch?v=5qap5aO4i9A"
video = pafy.new(url)
best = video.getbest()
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()

