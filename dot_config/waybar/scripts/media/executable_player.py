#!/bin/python

import subprocess
import re
import json
import sys
import time
from types import SimpleNamespace


def request_media_status():
    metadata = SimpleNamespace()
    metadata.status = subprocess.run(
        ["playerctl", "status"], capture_output=True, text=True
    ).stdout

    proc_metadata = subprocess.run(
        ["playerctl", "metadata"], capture_output=True, text=True
    ).stdout
    player = None

    if not proc_metadata:
        return None

    player_metadata = proc_metadata.split("\n")

    for data in player_metadata:

        fields = re.split("\\s+", data, maxsplit=2)
        if not player:
            player = fields[0]
        elif player != fields[0]:
            break

        type = fields[1]
        value = fields[2] if len(fields) == 3 else None

        if type == "xesam:title" and value:
            metadata.title = value
        elif type == "xesam:album" and value:
            metadata.album = value
        elif type == "xesam:artist" and value:
            metadata.artist = value

    return metadata


def format_json_output(media_status):
    if not media_status:
        return None

    # print(media_status)

    json_data = dict()

    if media_status.status == "Stopped":
        json_data["text"] = "⏹ No Media"
        json_data["class"] = "stopped"
    else:
        button = None
        if re.match("paused", media_status.status, re.IGNORECASE):
            button = "⏵"
            json_data["class"] = "paused"
        elif re.match("playing", media_status.status, re.IGNORECASE):
            button = "⏸"
            json_data["class"] = "playing"

        media_txt = []

        if hasattr(media_status, "artist"):
            media_txt.append(media_status.artist)
        if hasattr(media_status, "album"):
            media_txt.append(media_status.album)
        if hasattr(media_status, "title"):
            media_txt.append(media_status.title)

        text = f"{button} {" - ".join(media_txt)}"
        if len(text) > 40:
            text = f"{text[:40]}…"

        json_data["text"] = text

    return json.dumps(json_data)


def main():
    while True:
        output = format_json_output(request_media_status())
        if output:
            sys.stdout.write(output)
            sys.stdout.flush()

        time.sleep(0.1)


if __name__ == "__main__":
    main()
