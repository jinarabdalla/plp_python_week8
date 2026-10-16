# Personal Mini-Toolkit

## What it does
This beginner-friendly Python program brings together three tools in one menu:
- **Simple Calculator** — adds, subtracts, multiplies, or divides two numbers.
- **To-Do List** — adds, displays, and removes tasks during the program run.
- **Number Guessing Game** — gives hints until the player guesses the secret number.

The project practices variables, input/output, conditionals, loops, lists, functions, comments, and f-strings. It also handles common invalid inputs politely.

## Files
- `toolkit_plan.txt` — the plan and menu design.
- `toolkit.py` — the working program.
- `screenshots/` — add screenshots showing the menu, an invalid menu choice, and each tool in action.

## How to run
1. Install Python 3 if it is not already installed.
2. Open a terminal in this repository's folder.
3. Run:
   ```bash
   python toolkit.py
   ```
   On some computers, use `python3 toolkit.py` instead.
4. Follow the numbered menu. Choose **4** to quit.

## Reflection
The hardest part was planning how the main menu should return after each tool finishes. The to-do list needed extra care because the list changes whenever a task is added or removed. One bug to watch for was entering letters instead of numbers, so the program uses `try/except` to handle invalid numeric input without crashing. I also checked that division by zero and invalid menu choices receive helpful messages. The tools use functions to keep the code organized and easier for another learner to read. With one more week, I would add a feature to save the to-do list to a file so tasks can be kept after the program closes.

## Screenshots checklist
Run the program and save your own screenshots inside `screenshots/`:
1. Main menu and invalid menu choice message.
2. Calculator showing a result.
3. To-do list with a task added and displayed.
4. Number guessing game showing a successful guess.
5. Quit message.
