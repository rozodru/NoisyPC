# NoisyPC

Bring the glorious chaos of the 90s back to your modern Linux machine.

**NoisyPC** is a small Linux utility that plays retro computer sounds—like hard drive clicks, modem screeches, and fan whines—based on real system activity. It's like installing a sound skin for your PC that turns disk I/O, CPU load, and more into an ambient nostalgia trip.

![Retro PC](https://upload.wikimedia.org/wikipedia/commons/3/32/IBM_PS2_Model_25.jpg)

> Remember when opening a file _sounded like_ opening a file? Yeah, I do too.

---

## 🧰 Features

- 💽 Plays hard drive seek/spin sounds based on real disk access
- 📡 Optional modem screech on network activity (coming soon)
- 🧠 Customizable sound themes (HDD, modem, CPU, etc.)
- 🔧 Lightweight Python script that runs quietly in the background
- ☠️ Zero actual impact on performance or I/O—it’s all fake noise, for fun

---

## 🔧 Installation

### 1. Install Dependencies

You'll need Python 3 and `ffplay` from the `ffmpeg` package:

```bash
# Arch Linux
sudo pacman -S ffmpeg

# Debian/Ubuntu
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg
```

### 2. Clone the Repo

```bash
git clone https://github.com/rozodru/noisypc.git
cd noisypc
```

### 3. Add Some Sounds

Create the sound directory and drop in some `.wav` or `.mp3` files:

```bash
mkdir -p ~/.config/noisypc/sounds/hdd
cp ./sounds/hdd1.wav ~/.config/noisypc/sounds/hdd/
```

You can find retro PC sound effects from:

- [https://freesound.org](https://freesound.org)
- [https://archive.org/details/RetroComputerSounds](https://archive.org/details/RetroComputerSounds)

### 4. Run It

```bash
python3 noisypc.py
```

Or make it executable:

```bash
chmod +x noisypc.py
./noisypc.py
```

---

## 📁 Directory Structure

```
~/.config/noisypc/
  └── sounds/
        └── hdd/
              ├── hdd1.wav
              ├── hdd2.wav
              └── ...
```

---

## ⚙️ Configuration (Coming Soon)

In the next release: config file support for:

- Disk device selection
- Volume and cooldown
- Sound themes
- Toggling features

---

## 🧠 Why?

Because silent computers are boring.  
Because SSDs are too fast.  
Because we _miss_ the sound of our machine _doing something_.

---

## 💡 Roadmap

- [x] Disk I/O-triggered HDD sounds
- [ ] Network activity-triggered modem sounds
- [ ] CPU load-triggered fan or coil whine
- [ ] Config file support (TOML/YAML)
- [ ] GUI/TUI toggle or system tray icon
- [ ] Theme packs: IBM, Gateway, Packard Bell

---

## 👤 Author

**andrew@andmc.ca**  
Retro computing enthusiast, Linux tinkerer, chaos enjoyer.

---

## 🧡 Contributing

PRs welcome! Especially if you:

- Want to add new sound trigger types
- Have a great archive of retro sounds
- Can build out systemd or autostart support

---

## 📜 License

MIT License.  
Make noise, not spyware.
