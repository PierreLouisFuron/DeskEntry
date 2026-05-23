# DeskEntry

A simple graphical editor for Linux `.desktop` launcher files.

DeskEntry helps you create, edit and manage desktop entries used by GNOME and other Linux desktop environments. It provides a convenient Qt-based interface for modifying application launchers without manually editing `.desktop` files.

Built with Python and PySide6.

---

## Features

- Create new `.desktop` launcher files
- Edit existing desktop entries
- Modify:
  - application name
  - executable command
  - icon
  - categories
  - terminal mode
  - startup behavior
- Browse and select icons visually
- Save launchers directly to the appropriate desktop entry directories
- Lightweight Qt interface

---

## Screenshots

*(Add screenshots here later)*

---

## Requirements

- Linux
- Python 3.10+
- PySide6

---

## Installation

Clone the repository:

```bash
git clone https://github.com/PierreLouisFuron/DeskEntry.git
cd DeskEntry
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running

Launch the application with:

```bash
python __main__.py
```

---

## About `.desktop` files

Desktop entry files are part of the XDG Desktop Entry Specification and are used by Linux desktop environments to define application launchers.

Typical locations include:

```text
~/.local/share/applications/
```

and

```text
/usr/share/applications/
```

---

## Development

This project uses:

- Python
- PySide6 / Qt6
- Qt Designer

Generated files, virtual environments and IDE metadata are excluded from version control through `.gitignore`.

---

## Contributing

Contributions, suggestions and bug reports are welcome.

Feel free to open an issue or submit a pull request.

---

## License

MIT License
