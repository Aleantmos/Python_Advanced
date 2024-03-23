from album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if self.albums.__contains__(album):
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        searched_album = next((album for album in self.albums if album.name == album_name), None)
        if searched_album is None:
            return f"Album {album_name} is not found."

        if searched_album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(searched_album)
        return f"Album {searched_album.name} has been removed"

    def details(self):
        res = f"Band {self.name}\n"
        for album in self.albums:
            res += f"{album.details()}\n"

        return res.strip()