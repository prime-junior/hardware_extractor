# Hardware Extractor: Part Number Extraction and Update via Google Sheets

## Project Overview

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-ff4b4b?logo=streamlit)
![WIP](https://img.shields.io/badge/Project-WIP-yellow)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Enabled-4285F4?logo=googlecloud)
![Pandas](https://img.shields.io/badge/Pandas-Enabled-150458?logo=pandas)
![gspread](https://img.shields.io/badge/gspread-Enabled-34a853)

After extracting data from PDF files and moving them to a Google Sheet as described in the repository (https://github.com/prime-junior/pdf_data_extract), this project provides a web interface for further processing and management of part numbers. Using Streamlit, it allows users to input a part number, automatically extract all its variations from the Google Sheet, and update the relevant cells accordingly. The tool streamlines the workflow of validating, extracting, and organizing hardware part numbers, ensuring that the Google Sheet remains up-to-date and consistent for further analysis or reporting.


The final deliverable of this project is a standalone Windows executable (`.exe`) built with PyInstaller, so that end users can run the application with a double-click — no Python installation or terminal required.

**Note:** For accessing Google Sheets, it is necessary to create a service account in Google Cloud Platform as described in the [gspread documentation](https://docs.gspread.org/en/latest/oauth2.html)


## Technologies Used

| Technology | Purpose |
|---|---|
| [Python 3.8+](https://www.python.org/) | Core language |
| [Streamlit](https://streamlit.io/) | Web interface |
| [gspread](https://docs.gspread.org/) | Google Sheets API client |
| [Pandas](https://pandas.pydata.org/) | DataFrame manipulation |
| [Google Cloud (Service Account)](https://cloud.google.com/) | Authentication for Google Sheets |
| [PyInstaller](https://pyinstaller.org/) | Package app as standalone `.exe` |

---

## Project Structure

```
hardware_extractor/
├── main.py                  # Streamlit app entry point (UI + logic)
├── utils.py                 # Helper functions: open_gsheet(), extract_update_cell()
├── hdw_extractor_run.py     # Launcher for the PyInstaller executable
├── hdw_extractor_run.spec   # PyInstaller build spec
├── requirements.txt         # Python dependencies
├── .streamlit/
│   └── config.toml          # Streamlit server configuration
├── hooks/
│   └── hook-streamlit.py    # Custom PyInstaller hook for Streamlit
├── dist/
│   └── hdw_extractor_run.exe  # Generated Windows executable
└── media/
    └── demo.mp4             # Application demo
```

---

## Installation & Running

### Prerequisites

- Python 3.8+
- A Google Cloud service account with access to the target Google Sheet (see [gspread OAuth2 docs](https://docs.gspread.org/en/latest/oauth2.html))
- The service account credentials file (`service_account.json`) placed in the default `gspread` config path:
  - Windows: `%APPDATA%\gspread\service_account.json`
  - Linux/macOS: `~/.config/gspread/service_account.json`

### 1. Clone the repository

```bash
git clone https://github.com/prime-junior/hardware_extractor.git
cd hardware_extractor
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Build and run the executable

Build the standalone `.exe` with PyInstaller:

```bash
pyinstaller hdw_extractor_run.spec
```

The executable will be generated at `dist\hdw_extractor_run.exe`. After the build, simply double-click it to launch the application — no terminal or Python installation needed.

> **Note:** On the first run the browser may take a few seconds to open while Streamlit initialises inside the executable.

---

## Application Demo
[VIEW DEMO](./media/demo.mp4)

## License
MIT