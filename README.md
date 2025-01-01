# Faceit Player Statistics Script

## Releases

Download pre-built executables for **Linux** and **Windows** from the [Releases page](https://github.com/Slipum/Script-Faceit-Stats/releases).

---

## Description

This script retrieves a **Faceit** player's statistics for **CS2** using their username. Users provide a Faceit nickname, and the script queries the Faceit API to fetch and display relevant statistics.

---

## Requirements

### Libraries:

1. **os** - standard Python library for interacting with the operating system.
2. **requests** - for making HTTP requests.

To install the `requests` library, use:

```bash
pip install requests
```

---

## Features

### Main workflow:

1. The user inputs a Faceit username.
2. The script queries the Faceit API to retrieve the player's ID.
3. If the ID is found:
   - A second request fetches the player's statistics for CS2.
   - The script processes and displays the following statistics:
     - **Username**.
     - **Current ELO**.
     - **Skill level**.
     - **Average damage per round (avg)**.
     - **Kill/Death ratio (K/D)**.
     - **Kills per round (K/R)**.
     - **Headshot percentage (hs)**.
4. If the requests fail, an error message is displayed.
5. At the end, the user can choose to:
   - Fetch statistics for another player.
   - Exit the program.

---

## How to Use

1. Save the script as `faceit_stats.py`.
2. Run the script:
   ```bash
   python faceit_stats.py
   ```
3. Enter the Faceit username when prompted:
   ```
   Enter faceit username: player_name
   ```
4. The script will display the player's statistics or an error message if data is unavailable.

---

## Example Output

```
Enter faceit username: test_user
test_user
elo: 1234
lvl: 7
avg: 68.7
k/d: 1.12
k/r: 0.83
hs: 56
Choose an action:
1. Exit the application
2. Get statistics
Your choice:
```

---

## Possible Improvements

- [ ] **Error handling**: Add more robust error handling (e.g., invalid username input or network issues).
- [ ] **Formatting**: Use libraries like `prettytable` for a cleaner display of data.
- [ ] **Localization**: Support multiple languages (e.g., English, Russian).
- [ ] **Testing**: Add unit tests to ensure the script handles various scenarios correctly.

---

Feel free to suggest additional features or improvements by creating an issue[issue](https://github.com/Slipum/Script-Faceit-Stats/issues) or [pull](https://github.com/Slipum/Script-Faceit-Stats/pulls) request!
