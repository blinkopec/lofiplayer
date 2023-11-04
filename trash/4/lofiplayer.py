import vlc
import time
# придется брать музыку с ютуба т.к невозможно найти плейлисты
volume = 40
url = 'https://rr17---sn-n8v7knez.googlevideo.com/videoplayback?expire=1697881888&ei=wEozZYzIAsjhgAeB-5PgDw&ip=217.138.192.220&id=jfKfPfyJRdk.2&itag=137&aitags=133%2C134%2C135%2C136%2C137%2C160&source=yt_live_broadcast&requiressl=yes&spc=UWF9fyVh_QCa-l8OjpleKJVWYDwgJPQ&vprv=1&live=1&hang=1&noclen=1&svpuc=1&mime=video%2Fmp4&gir=yes&keepalive=yes&fexp=24007246,24350018&beids=24350018&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Clive%2Chang%2Cnoclen%2Csvpuc%2Cmime%2Cgir&sig=AGM4YrMwRQIhAOArewkwMoyG4y8188f-HXPNgaUQu4tMqisPXV2SWb1LAiBvHXP1FuTR7bbuij1cj3DO4MIFSByy_MRvjJYF1XX4Zw%3D%3D&rm=sn-5hnezs7e&req_id=82c0c57bfa7ea3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-gvnuxaxjvh-ov1e7e&cms_redirect=yes&cmsv=e&hcs=sd&mh=rr&mip=37.22.115.228&mm=29&mn=sn-n8v7knez&ms=rdu&mt=1697859895&mv=m&mvi=17&pl=27&rmhost=rr11---sn-n8v7knez.googlevideo.com&smhost=rr2---sn-n8v7kn7z.googlevideo.com&lsparams=hcs,ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl,rmhost,smhost&lsig=AK1ks_kwRQIhAPwOcOPSaq7fOJBzNlG4Rf5OIiKLKwDUnKXAyhLAf_gJAiABhCWwbM92aHirc87BHkeu93QFqQK3GeWbGrZAYC3jmw%3D%3D'

# * video is playing, only downloaded and url (+ volume)
# player = vlc.MediaPlayer()
# media = vlc.Media(url)
# player.set_media(media)
# player.play()

# * вариант с настройкой громкости
instance = vlc.Instance('--input-repeat=1')
player = instance.media_player_new()
media = instance.media_new(url)
media.get_mrl()
player.audio_set_volume(volume)
player.set_media(media)
player.play()

# 10 секунд будет идти музыка
time.sleep(10)