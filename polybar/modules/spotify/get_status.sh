#!/bin/sh

STATUS=$(playerctl --player=spotify status 2>/dev/null)

if [ "$STATUS" = "Playing" ] || [ "$STATUS" = "Paused" ]; then
    CURRENT_ARTIST=$(playerctl --player=spotify metadata artist)
    CURRENT_SONG=$(playerctl --player=spotify metadata title)
    echo "$CURRENT_ARTIST: $CURRENT_SONG"
else
    echo "Spotify is not playing"
fi
