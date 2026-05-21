# ABAP Programs Vault

A personal web app to store, view, search, and manage your SAP ABAP practice programs.
Built with Python (Flask) + SQLite backend and a plain HTML frontend.

---

## Project Structure

```
abap-vault/
├── server.py        → Python backend (API + database logic)
├── index.html       → Frontend (opens in browser)
├── abap_vault.db    → SQLite database (auto-created on first run)
└── README.md        → This file
```

---

## Requirements

- Python 3.x
- VS Code
- Live Server extension in VS Code
- A browser (Chrome recommended)

---

## Step 1 — Create the Project Folder

1. Create a new folder anywhere on your computer, e.g. `abap-vault` on your Desktop
2. Place `server.py` and `index.html` inside that folder
3. Open VS Code → File → Open Folder → select `abap-vault`

Your folder should look like this:
```
abap-vault/
├── server.py
└── index.html
```

---

## Step 2 — Install Python Libraries (One Time Only)

Open the terminal in VS Code using `Ctrl + ~` and run:

```bash
py -m pip install flask flask-cors
```

Wait until you see `Successfully installed`. You only need to do this once.

---

## Step 3 — Start the Server

Every time you want to use the app, run this in the VS Code terminal:

```bash
py server.py
```

You should see:
```
  ABAP Vault Server
  Running at http://localhost:5000
```

> Important: Keep this terminal open while using the app.
> If you close it, the app stops working.

---

## Step 4 — Open the App

1. In VS Code, right-click on `index.html`
2. Click **"Open with Live Server"**
3. Browser opens at `http://127.0.0.1:5500/index.html`
4. The app loads and connects to your server automatically

---

## Step 5 — Using the App

### Add a Program
1. Click **+ Add Program** (top right)
2. Fill in the form:
   - **Program Name** — e.g. `Z_HELLO_WORLD` (required)
   - **Description** — what the program does (required)
   - **T-Code** — e.g. `SE38` (optional)
   - **Tags** — e.g. `OOP, DDIC, Basics` (optional)
   - **ABAP Code** — paste your code (required)
3. Click **Save Program**

### View a Program
- Click any program name in the left sidebar
- Details and code appear on the right side

### Search
- Type in the search bar at the top
- Searches by name, description, T-code, and tags in real time

### Copy Code
- Open a program → click the **Copy** button
- Code is copied to your clipboard instantly

### Edit a Program
- Open a program → click **Edit Program**
- Make your changes → click **Save Program**

### Delete a Program
- Open a program → click **Delete**
- Confirm the popup → program is permanently removed

---

## Step 6 — Check Your Data (Optional)

Your programs are stored in `abap_vault.db` — a SQLite file created automatically in the same folder as `server.py`.

### Option A — Via Terminal
```bash
py -m sqlite3 abap_vault.db
```
Then type:
```sql
SELECT * FROM programs;
```
Type `.exit` to quit.

### Option B — DB Browser for SQLite (Visual)
1. Download from: https://sqlitebrowser.org
2. Open it → click **Open Database** → select `abap_vault.db`
3. Click **Browse Data** tab → select `programs` table
4. See all your saved programs like a spreadsheet

---

## How It All Works

```
Browser (index.html)
       ↓  sends requests using fetch()
Python Server (server.py) on port 5000
       ↓  reads and writes using SQL
SQLite Database (abap_vault.db)
```

- `index.html` — the UI you see in the browser
- `server.py` — receives requests, talks to the database
- `abap_vault.db` — the file where all programs are permanently stored

---

## API Reference

| Method | URL | What it does |
|--------|-----|--------------|
| GET | /programs | Get all programs |
| POST | /programs | Add a new program |
| PUT | /programs/:id | Update a program |
| DELETE | /programs/:id | Delete a program |

---

## Common Problems & Fixes

### "Cannot connect to server" in the app
- You forgot to run `py server.py`
- Or you closed the terminal — reopen and run it again

### `py` command not found
- Try `python server.py` instead
- Make sure Python is installed and added to PATH

### `pip` not recognized
- Use `py -m pip install flask flask-cors` instead

### Programs disappear after closing browser
- This means the server was not running when you opened the app
- Always start `py server.py` first, then open the app

### Port 5000 already in use
- Another app is using port 5000
- Stop it, or change `port=5000` to `port=5001` in `server.py`
- Then also change `const API = 'http://localhost:5000'` to `5001` in `index.html`

---

## Every Time You Use the App

1. Open VS Code → open the `abap-vault` folder
2. Open terminal with `Ctrl + ~`
3. Run `py server.py`
4. Right-click `index.html` → Open with Live Server
5. Start coding! 

---

## Author

Krishnakumar G B
ABAP Developer Intern | BEC Bagalkote