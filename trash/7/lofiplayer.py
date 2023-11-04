import pafy
import vlc
import time

volume = 40
url = "https://www.youtube.com/watch?v=i-DJquV-T98"

video = pafy.new(url)
best = video.getbestaudio()
playurl = best.url


instance = vlc.Instance('--input-repeat=1')
player = instance.media_player_new()
media = instance.media_new(playurl)
media.get_mrl()
player.audio_set_volume(volume)
player.set_media(media)
player.play()

time.sleep(10000)