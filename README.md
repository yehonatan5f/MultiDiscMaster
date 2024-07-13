# 💿 RetroDiscOrganizer

Automatically organize your multi-disc retro game ROMs with ease!

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎮 Features

- 🔍 Detects and organizes multi-disc games
- 📁 Creates game-specific folders
- 📝 Generates .m3u playlists automatically
- 🔢 Handles games with any number of discs
- 🛡️ Preserves existing organization
- 🏷️ Renames folders to .m3u format
- 📊 Provides detailed console output

## 🚀 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/RetroDiscOrganizer.git

2. Navigate to the script directory:
   ```bash
    cd RetroDiscOrganizer
3. Run the script:
   ```bash
   python organize_games.py /path/to/your/rom/folder


📋 Requirements
* 📝 Python 3.6+
* 📝 tqdm library (install with pip install tqdm)
  

📘 How It Works
1. Scans the specified directory for game files with "Disc" in the filename
2. Groups files belonging to the same game
3. Creates a folder for each game
4. Moves all related files into the game's folder
5. Renames the folder to add the .m3u extension


🎯 Use Case
Perfect for retro gaming enthusiasts with large ROM collections, especially for multi-disc systems like PlayStation 1, Sega CD, or PC Engine CD. Streamlines your library for seamless use with various emulators.

⚠️ Caution
Always backup your ROM collection before running this script!

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

📜 License
Distributed under the MIT License. See LICENSE for more information.


Credit: yehonatan5f.
