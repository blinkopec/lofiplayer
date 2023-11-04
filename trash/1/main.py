from yandex_music import Client
from yandex_music.exceptions import NotFoundError

artist_id = 8268430
token = 'y0_AgAAAAAkdPrzAAG8XgAAAADud0eHLREUXYrHSNWSiKKaxlyvZN3T5us'

client = Client(token).init()

#пример как скачать трек
#client.users_likes_tracks()[0].fetch_track().download('example.mp3')



queues = client.queues_list()
# Последняя проигрываемая очередь всегда в начале списка
last_queue = client.queue(queues[0].id)

last_track_id = last_queue.get_current_track()
last_track = last_track_id.fetch_track()

artists = ', '.join(last_track.artists_name())
title = last_track.title
print(f'Сейчас играет: {artists} - {title}')

try:
    lyrics = last_track.get_lyrics('LRC')
    print(lyrics.fetch_lyrics())

    print(f'\nИсточник: {lyrics.major.pretty_name}')
except NotFoundError:
    print('Текст песни отсутствует')