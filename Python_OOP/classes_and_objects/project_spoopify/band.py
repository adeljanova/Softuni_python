
class Band:

    def __init__(self, name: str):
        self.name = name
        self.attribute_albums = []

    def add_album(self, new_album):
        if new_album in self.attribute_albums:
            return f"Band {self.name} already has {new_album.name} in their library."
        self.attribute_albums.append(new_album)
        return f"Band {self.name} has added their newest album {new_album.name}."

    def remove_album(self, album_name):
        for album in self.attribute_albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.attribute_albums.remove(album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.attribute_albums:
            result += album.details() + "\n"

        return result.strip()


