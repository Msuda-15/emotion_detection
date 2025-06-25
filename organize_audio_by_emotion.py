import os
import shutil

# === CONFIGURATION ===
source_folders = [
    "Audio_Speech_Actors_01-24",  # Speech data
    "Audio_Song_Actors_01-24"     # Song data
]
include_songs = True  # Set to False if you want to ignore song files
destination_folder = "data"

# RAVDESS emotion mapping
emotion_map = {
    "01": "neutral",
    "02": "calm",
    "03": "happy",
    "04": "sad",
    "05": "angry",
    "06": "fearful",
    "07": "disgust",
    "08": "surprised"
}

# === SCRIPT ===
print("🟢 Starting audio file organization...")

os.makedirs(destination_folder, exist_ok=True)

for folder in source_folders:
    if not include_songs and "Song" in folder:
        print(f"🔕 Skipping songs from {folder}")
        continue

    if not os.path.exists(folder):
        print(f"⚠️ Source folder not found: {folder}")
        continue

    for actor_dir in os.listdir(folder):
        actor_path = os.path.join(folder, actor_dir)
        if not os.path.isdir(actor_path):
            continue

        for file in os.listdir(actor_path):
            if file.endswith(".wav"):
                parts = file.split("-")
                if len(parts) < 2:
                    continue  # skip invalid filename
                emotion_code = parts[2]
                emotion_label = emotion_map.get(emotion_code)

                if emotion_label is None:
                    continue

                # Create target folder if it doesn't exist
                target_dir = os.path.join(destination_folder, emotion_label)
                os.makedirs(target_dir, exist_ok=True)

                source_path = os.path.join(actor_path, file)
                target_path = os.path.join(target_dir, file)

                try:
                    shutil.copy(source_path, target_path)
                    print(f"✅ Copied {file} → {emotion_label}/")
                except Exception as e:
                    print(f"❌ Error copying {file}: {e}")

print("🎉 All files processed.")
