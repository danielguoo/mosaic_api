import sys
import os
import django

sys.path.append(".")  # here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mosaic_api.settings")
django.setup()
import spotipy
import spotipy.util as util
from music.models import Album

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_albums(limit=50)
    for item in results['items']:
        album_record = item['album']
        album = Album(released=2017, title=album_record['name'], artist=album_record['artists'][0]
                      ['name'], spotify_URL=album_record['id'], cover_art=album_record['images'][0]['url'])
        print(album)
        album.save()
else:
    print("Can't get token for", username)
