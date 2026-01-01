def favorite_songs(playlist: list[dict]) -> list:
    playlist.sort(key=lambda song: song["plays"], reverse=True)
    playlist_list = [song["title"] for song in playlist]
    return playlist_list[:2]
