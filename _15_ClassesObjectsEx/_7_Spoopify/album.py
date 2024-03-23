from song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif self.songs.__contains__(song):
            return "Song is already in the album"
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}"

    def remove_song(self, name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        found_song = next((song for song in self.songs if song.name == name), None)

        if found_song is None:
            return "Song is not in the album."

        self.songs.remove(found_song)

        return f"Removed song {found_song.name} from album {self.name}"

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        else:
            return f"Album {self.name} is already published."

    def details(self):
        res = f"Album {self.name}\n"

        for song in self.songs:
            res += f"== {song.get_info()}\n"

        return res.strip()
