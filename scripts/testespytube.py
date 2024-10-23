from pytube import Playlist, YouTube
teste_playlist = Playlist("https://www.youtube.com/playlist?list=PL-EWx9Mw_fia6Od7xe3w3EdYrIdEn_DQm")

for _ in teste_playlist.videos:
    try:
        print(_.title)
    except KeyError:
        print(f"Erro ao obter título do vídeo: {_.watch_url}")

