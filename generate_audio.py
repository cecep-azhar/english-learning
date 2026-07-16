#!/usr/bin/env python3
"""Generate audio files from scripts.json using edge-tts with async batch processing.

Works with the flat scripts.json format:
  scripts[].num_id -> /audio/{num_id}.mp3 and /audio/{num_id}_id.mp3
"""

import asyncio
import json
import os
import edge_tts

AUDIO_DIR = "/home/cecep/english-learning/audio"
SCRIPTS_FILE = "/home/cecep/english-learning/scripts.json"
EN_VOICE = "en-US-GuyNeural"
ID_VOICE = "id-ID-ArdiNeural"


async def generate_audio(text: str, voice: str, output_path: str) -> bool:
    """Generate a single audio file."""
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_path)
        return True
    except Exception as e:
        print(f"  ERROR generating {output_path}: {e}")
        return False


async def generate_all_audio(scripts: list) -> None:
    """Generate all English and Indonesian audio files concurrently."""
    semaphore = asyncio.Semaphore(10)  # limit concurrency

    async def limited_generate(text, voice, path):
        async with semaphore:
            return await generate_audio(text, voice, path)

    tasks = []
    for script in scripts:
        num_id = script["num_id"]
        en_path = os.path.join(AUDIO_DIR, f"{num_id}.mp3")
        id_path = os.path.join(AUDIO_DIR, f"{num_id}_id.mp3")

        # Skip if both already exist
        if os.path.exists(en_path) and os.path.exists(id_path):
            continue

        tasks.append(limited_generate(script["en"], EN_VOICE, en_path))
        tasks.append(limited_generate(script["translation"], ID_VOICE, id_path))

    if not tasks:
        print("All audio files already exist. Nothing to generate.")
        return

    print(f"Generating {len(tasks)} audio files ({len(scripts)*2 - len([t for t in tasks if t])} needed)...")
    results = await asyncio.gather(*tasks)
    success = sum(1 for r in results if r)
    print(f"Done: {success}/{len(tasks)} files generated successfully.")


async def main():
    # Load scripts
    with open(SCRIPTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    scripts = data["scripts"]
    print(f"Loaded {len(scripts)} scripts from {SCRIPTS_FILE}")

    # Ensure audio directory exists
    os.makedirs(AUDIO_DIR, exist_ok=True)
    print(f"Audio output directory: {AUDIO_DIR}")

    # Generate all audio
    await generate_all_audio(scripts)

    # List generated files
    files = sorted(os.listdir(AUDIO_DIR))
    print(f"\nTotal audio files in {AUDIO_DIR}: {len(files)}")


if __name__ == "__main__":
    asyncio.run(main())
