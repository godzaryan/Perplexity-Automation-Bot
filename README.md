# Perplexity Automation Bot

A professional Python automation script that interacts with [Perplexity AI](https://www.perplexity.ai/) through Firefox using Selenium WebDriver.  
Automate sending prompts and retrieving AI responses dynamically and efficiently, with your logged-in Firefox profile.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Getting Started (Beginner Guide)](#getting-started-beginner-guide)  
- [Usage](#usage)  
- [Code Overview](#code-overview)  
- [Troubleshooting](#troubleshooting)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview

**Perplexity Automation Bot** automates interaction with Perplexity AI by leveraging Selenium and your existing Firefox browser profile.  
It sends prompts via the live web UI dynamically, waits intelligently for the AI to finish generating responses, and outputs results directly to the console.

Project repository: [https://github.com/godzaryan/Perplexity-Automation-Bot](https://github.com/godzaryan/Perplexity-Automation-Bot)

---

## Features

- Integrates with your real Firefox profile to preserve logged-in sessions  
- Detects and interacts with Perplexity’s dynamic contenteditable prompt input  
- Sends prompts with human-like typing delays  
- Waits dynamically for response generation completion by detecting UI state changes  
- Prints responses directly in the console — no intermediate files  
- Supports continuous interaction: send multiple prompts without restarting  
- Reliable, minimal, and easy to extend  

---

## Prerequisites

- Windows 10/11 (Linux/macOS users will need to adapt paths)  
- Python 3.7 or higher  
- Mozilla Firefox installed  
- Selenium (`pip install selenium`)  
- Geckodriver compatible with your Firefox version (must be in system PATH or specify path in code)  

---

## Installation

1. **Install Python**:  
   Download and install from [python.org](https://www.python.org/downloads/) with “Add Python to PATH” enabled.

2. **Install Selenium package**:
``` 
pip install selenium
```

3. **Download Geckodriver**:  
- Visit [Mozilla’s Geckodriver releases](https://github.com/mozilla/geckodriver/releases)  
- Pick the version matching your Firefox and OS  
- Extract `geckodriver.exe` and place in your system PATH or a known folder

4. **Locate your Firefox profile folder**:  
- Launch Firefox, enter `about:support` in the address bar  
- Click “Open Folder” for **Profile Folder**  
- Note the full folder path (something like `C:\Users\<User>\AppData\Roaming\Mozilla\Firefox\Profiles\<profile>.default-release`)

5. **Edit the script configuration**:  
Change `FIREFOX_PROFILE_PATH` and `FIREFOX_BINARY_PATH` in the script to match your system.

---

## Getting Started (Beginner Guide)

1. Ensure Firefox is installed and you have logged in to [Perplexity AI](https://www.perplexity.ai/) using your normal Firefox browser profile.

2. Follow installation steps above to set up Python, Selenium, and Geckodriver.

3. Clone or download this repository from [GitHub](https://github.com/godzaryan/Perplexity-Automation-Bot).

4. Update the configuration constants in the Python script with your Firefox profile and executable paths.

5. Run the script via command line:
```
python main.py
```

6. Enter your prompts as requested. The AI’s answers will print directly in your console.

7. To stop, type `exit` or press Enter on an empty prompt.

---

## Usage

Run from your terminal:
```
python main.py
```

Example interaction:

Enter prompt (or 'exit' / empty to quit): What is quantum entanglement?

Sending prompt:
What is quantum entanglement?
Waiting for Perplexity to finish generating...

--- Perplexity AI Response ---

Quantum entanglement is a quantum phenomenon where particles become interconnected such that the state of one instantly influences the state of another, regardless of distance.


---

## Code Overview

- Opens Firefox with your existing profile using Selenium WebDriver.  
- Waits for the dynamic contenteditable prompt input (`div` with changing placeholder text).  
- Sends user prompts with human-like typing.  
- Detects the visible “stop generating response” button to know when generation is active, waiting until it disappears signaling completion.  
- Extracts the latest response text from Perplexity’s markdown output container and prints it.  
- Loops until the user exits manually.

---

## Troubleshooting

- Ensure no conflicting Firefox instances block profile usage during automation.  
- Double-check your Firefox profile path and binary executable path.  
- Make sure Geckodriver is installed and accessible via system PATH.  
- If AI response fails to appear, consider increasing `WAIT_PAGE_LOAD` and `GENERATION_TIMEOUT`.  
- Inspect Perplexity’s UI if selectors break due to UI changes and update the XPath strings accordingly.

---

## Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to fork the repo and submit pull requests for:

- Additional browser support (Chrome, Edge)  
- Clipboard image upload  
- Enhanced error handling  
- Headless mode enhancements  
- Multi-prompt batch automation

---

## License

MIT License © 2025 Akash Kumar (Aryan Kumar)
For help, open an issue or contact the maintainer on GitHub.

---
