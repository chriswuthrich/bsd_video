#!/usr/bin/env bash

## ffmpeg -framerate 60 -i INPUT%04d.png -c:v prores_ks -profile:v 4 -pix_fmt yuva444p10le output.mov

# Exit if any command fails
set -e

# Check arguments
if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "Usage: $0 INPUT [OUTPUT]"
  echo "If OUTPUT is omitted, it defaults to INPUT"
  exit 1
fi

INPUT="$1"

if [ "$#" -eq 2 ]; then
  OUTPUT="$2"
else
  OUTPUT="$1"
fi

FIRST_FRAME="media/images/${INPUT}0001.png"

if [ ! -f "$FIRST_FRAME" ]; then
  echo "Error: Input file '$FIRST_FRAME' does not exist."
  exit 1
fi

ffmpeg -framerate 60 \
  -i "media/images/${INPUT}%04d.png" \
  -c:v prores_ks \
  -profile:v 4 \
  -pix_fmt yuva444p10le \
  "media/mov_videos/${OUTPUT}.mov"

echo "done. Output in media/mov_videos/${OUTPUT}.mov"