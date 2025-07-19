#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 /path/to/video.mp4 app_label.model_name"
    exit 1
fi

VIDEO_PATH="$1"
MODEL_NAME="$2"
VIDEO_TITLE=$(basename "$VIDEO_PATH")

if [ ! -f "$VIDEO_PATH" ]; then
    echo "File not found: $VIDEO_PATH"
    exit 1
fi

APP_LABEL=$(echo "$MODEL_NAME" | cut -d. -f1)
MODEL_CLASS=$(echo "$MODEL_NAME" | cut -d. -f2)

python3 manage.py shell <<EOF
from foliofin.apps import apps
from django.core.files import File

Model = apps.get_model("$APP_LABEL", "$MODEL_CLASS")
if not Model:
    print("Error: Could not find model $MODEL_NAME")
    exit()

with open("$VIDEO_PATH", "rb") as f:
    file_content = f.read()
    f.seek(0)
    video_instance = Video(
        title="$VIDEO_TITLE",
        file=File(f, name="$VIDEO_TITLE"),
        video=file_content
    )
    video_instance.save()
print("Video added successfully to $MODEL_NAME: $VIDEO_TITLE")
EOF