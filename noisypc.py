#!/usr/bin/env python3

import time
import os
import random
import subprocess

DISK_DEVICE = "nvme0n1"  # or sdb, nvme0n1, etc.
SOUND_DIR = os.path.expanduser("~/.config/noisypc/sounds/hdd")
SOUND_COOLDOWN = 1.5  # seconds between sounds to avoid rapid-fire
CHECK_INTERVAL = 0.5  # how often to check disk stats


def get_disk_stats(device):
    with open("/proc/diskstats", "r") as f:
        for line in f:
            if device in line:
                parts = line.split()
                # Read sectors: field 5, Write sectors: field 9
                read_sectors = int(parts[5])
                write_sectors = int(parts[9])
                return read_sectors, write_sectors
    return 0, 0


def play_random_sound():
    if not os.path.isdir(SOUND_DIR):
        return
    sounds = [f for f in os.listdir(SOUND_DIR) if f.endswith((".wav", ".mp3"))]
    if not sounds:
        return
    sound_file = os.path.join(SOUND_DIR, random.choice(sounds))
    subprocess.Popen(
        ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", sound_file]
    )


def main():
    print("NoisyPC is running... Ctrl+C to quit.")
    last_read, last_write = get_disk_stats(DISK_DEVICE)
    last_played = 0

    while True:
        time.sleep(CHECK_INTERVAL)
        current_read, current_write = get_disk_stats(DISK_DEVICE)
        delta_read = current_read - last_read
        delta_write = current_write - last_write
        last_read, last_write = current_read, current_write

        if (delta_read > 10 or delta_write > 10) and (
            time.time() - last_played > SOUND_COOLDOWN
        ):
            play_random_sound()
            last_played = time.time()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting NoisyPC.")
