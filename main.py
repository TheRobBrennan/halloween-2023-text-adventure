import time

def main():
    print_ascii_text()
    select_path()

# Function to print ASCII text
def print_ascii_text():
  # ASCII art for the game title
  ascii_text = [
  " ░█▀▀▀█ █──█ █▀▀█ █── █── █───█ █▀▀ █▀▀▄ █▀▀ █▀▀▀ ─▀─ █▀▀▄ ▀█",
  " ─▀▀▀▄▄ █▀▀█ █▄▄█ █── █── █▄█▄█ █▀▀ █▀▀▄ █▀▀ █─▀█ ▀█▀ █──█ █▀",
  " ░█▄▄▄█ ▀──▀ ▀──▀ ▀▀▀ ▀▀▀ ─▀─▀─ ▀▀▀ ▀▀▀─ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀──▀ ▄─",
  ]
  for line in ascii_text:
    print(line)
  print("\n")

# Function to handle the storyline when going alone
def go_alone():
    go_alone_story = [
        "╭────────────────────────────── Alone in the Mist ───────────────────────────╮",
        "│  Darcy decided to go alone to explore the legend of the Corpse Bride.      │",
        "│  Her heart pounded as she made the daring choice to venture into the misty │",
        "│  graveyard alone.                                                          │",
        "│  The wind whispered through the ancient tombstones, sending shivers down   │",
        "│  her spine.                                                                │",
        "│  With every step, the fog grew thicker, obscuring her path and filling her │",
        "│  with a sense of dread.                                                    │",
        "│  She finally reached the forgotten tombstone, said to be the resting place │",
        "│  of the Corpse Bride.                                                      │",
        "│  Suddenly, eerie whispers and ghostly footsteps echoed around her. Shadows │",
        "│  danced in the moonlight.                                                  │",
        "│  Darcy realized she wasn't alone. The legend of the Corpse Bride was all   │",
        "│  too real.                                                                 │",
        "╰────────────────────────────────────────────────────────────────────────────╯"
    ]

    # Visual enhancements
    for line in go_alone_story:
        print(line)
        time.sleep(2)
    select_path()

# Function to handle user game play
def select_path():
    user_input = input("Will Darcy go alone (A) or quit (Q)? ").lower()
    if user_input == 'a':
        go_alone()
    elif user_input == 'q':
        print("╭━━━━━━━━━━━━━━━Thanks for playing! Goodbye.━━━━━━━━━━━━━━╮")
        print("╰─────────────────────────────────────────────────────────╯")
        return
    else:
        print("Invalid choice. Please select 'A' or 'q` to quit.")
        select_path()

if __name__ == "__main__":
    main()
