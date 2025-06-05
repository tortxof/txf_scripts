#! /usr/bin/env python3

import json
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Track:
    title: str
    artist: str | None
    album: str | None
    track_number: int
    total_tracks: int | None
    file: Path


try:
    with open("info.json") as f:
        info = json.load(f)
except FileNotFoundError:
    print("File info.json not found. Writing info.json template.")
    with open("info.json", "w") as f:
        json.dump({"artist": None, "album": None, "tracks": ["", ""]}, f, indent=4)

    sys.exit(1)

flac_files = sorted(Path(".").glob("*.flac"))

default_artist = info.get("artist")
default_album = info.get("album")
num_tracks = len(info["tracks"])

tracks: list[Track] = []
for track_number, (file, track) in enumerate(
    zip(flac_files, info["tracks"], strict=True), start=1
):
    if isinstance(track, str):
        track = {"title": track}

    tracks.append(
        Track(
            title=track["title"],
            artist=track.get("artist", default_artist),
            album=track.get("album", default_album),
            track_number=track_number,
            total_tracks=num_tracks,
            file=file,
        )
    )


for track in tracks:
    lines = []
    if track.artist is not None:
        lines.append(f"artist={track.artist}")
    if track.album is not None:
        lines.append(f"album={track.album}")
    if track.total_tracks is not None:
        lines.append(f"tracknumber={track.track_number}/{track.total_tracks}")
    else:
        lines.append(f"tracknumber={track.track_number}")
    lines.append(f"title={track.title}")

    with open(track.file.with_suffix(".tag"), "w") as f:
        f.writelines(f"{line}\n" for line in lines)
