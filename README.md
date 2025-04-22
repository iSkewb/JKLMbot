# JKLM Bomb Party Bot 

A Python bot that plays [Bomb Party](https://jklm.fun), a fast-paced word game, by automatically detecting patterns and typing valid words into the game.

> **Disclaimer**: This bot is intended for educational purposes only. Use responsibly and do not violate the terms of service of any game.
<img src="https://github.com/user-attachments/assets/6b5be97c-0cf3-41ab-bbe6-5b31ab865544" width="400"/>

---

## Features

- Searches for valid words containing a given pattern
- Types them automatically with human-like delays
- Prioritizes words that use unused letters for an extra life
- Uses mouse and keyboard automation

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/JKLMBot.git
cd JKLMBot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Running the Bot

- 1. Launch the game in your browser at https://jklm.fun

- 2. Ensure the game input box is visible on screen

- 3. Change the mouse move coordinates to match the locations on your screen

- 4. Start a game and run the bot

```bash
python jklm.py
```

- 5. Enter the pattern shown on the bomb

- 6. The bot will select the best word and type it into the game

## How It Works

- The bot filters a large list of words to find valid ones containing the target pattern
- It prioritizes words that use letters not yet used for an extra life
- Mouse and keyboard modules simulate human actions
- Screen click coordinates may need adjustment depending on your screen resolution

## Notes

- The mouse.move() and mouse.click() coordinates are hardcoded for a specific screen layout and might need to be changed
- Not all words in the word list are guaranteed to be accepted by JKLM
- Uses both .csv and .txt word lists - you can modify or replace them

## Author

Devon Meyer  
Computer Engineering & MS Finance  
Texas A&M University
