import urllib.parse
from bs4 import BeautifulSoup


def main():
# read an XML file
    # Relative path to an XML export of your library with the wrong file locations
    with(open("./rekordbox-collection-wrong-file-location-2022-10-24.xml")) as f:
        data = f.read()
        Bs_data = BeautifulSoup(data, "xml")
        # find DJ_PLAYLISTS -> COLLECTION -> TRACK
        TRACKS = Bs_data.find("DJ_PLAYLISTS").find("COLLECTION").find_all("TRACK")
        # print(TRACKS)
        for track in TRACKS:
            artist = track.get("Artist")
            title = track.get("Name")
            album = track.get("Album")
            kind = track.get("Kind")
            trackNumberPadded = track.get("TrackNumber").zfill(2)
            extension = ""
            if kind == "WAV File":
                extension = "wav"
            elif kind == "MP3 File":
                extension = "mp3"
            elif kind == "FLAC File":
                extension = "flac"
            elif kind == "M4A File":
                extension = "m4a"

            basePath = "file://localhost/C:/Users/"
            
            proposed_location_string = "My Name/Dropbox/Music/" + artist + "/" + album + "/" + trackNumberPadded + " - " + title + "." + extension
            urlEncodedPath = urllib.parse.quote(proposed_location_string)
            fullPath = basePath + urlEncodedPath
            track["Location"] = fullPath
        print(Bs_data.prettify())

main()
