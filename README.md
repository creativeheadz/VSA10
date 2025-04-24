# VSA 10 API Tool

This tool provides a set of Python scripts to interact with the VSA 10 API. It allows you to execute various tasks, such as retrieving device information, managing groups, and running automation workflows. It is primarily meant to allow you to conveniently explore the VSA 10 API without the need of setting up Postman or overcomplicating things.

## Prerequisites

*   Python 3.6 or higher
*   `pip` package installer
*   API credentials

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd VSA10
    ```

2.  Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  If a `.env` file does not exist in the root directory of the project, `main.py` will create one.

2.  Add the following variables to the `.env` file, replacing the placeholders with your actual API credentials:

    ```properties
    ENDPOINT=https://oldforge.vsax.net/api/v3/
    TOKEN_ID=your_token_id
    TOKEN_SECRET=your_token_secret
    ```

    **Note:** It is crucial to keep your `.env` file secure and avoid committing it to version control. This repository is configured to ignore the `.env` file.

## Usage

The tool features an interactive navigation system through `main.py` that makes it easy to discover and execute available functions:

### Interactive Navigation

Run the main script to start the interactive navigator:

```bash
python main.py
```

The script will:
1. Scan the project directory for available functions and subfolders
2. Present them as numbered options in a menu interface
3. Allow you to navigate and execute functions using number keys

### Navigation Controls

* Enter the corresponding number to select a folder or function
* Press `0` or `b` to go back to the previous level
* Press `q` to quit the application

### Example Navigation Flow

When you run `main.py`, you'll see something like:

```
════════════════════════════════════════════════════════════
               VSAx API Tool - Directory Menu
════════════════════════════════════════════════════════════

[01] Audit Logs
[02] Automation Scripts
[03] Automation Tasks
[04] Automation Workflows
[05] Custom Fields
[06] Device Assets
[07] Devices
[08] Endpoint Protection
[09] Environment
[10] Groups
[11] Notification Webhook
[12] Notifications
[13] Organisations
[14] Patch Management
[15] Scopes
[16] Sites
[17] Exit

✓ Connected to API: oldforge.vsax.net
Customer: Andrei Trimbitas / oldforge
Version: 10.17.0 build 4800 release 353, US

────────────────────────────────────────────────────────────
Enter your choice:
```

Selecting option `01` would navigate into the Audit Logs folder:

```
════════════════════════════════════════════════════════════
                  Scripts in 'Audit Logs'
════════════════════════════════════════════════════════════

[01] Get All Audit Log Entries
[02] Back to Directory Menu

────────────────────────────────────────────────────────────
Enter your choice:


```

### Executing Functions

When you select a function, the script will:
1. Execute the function directly if it requires no arguments
2. Prompt you for any required arguments
3. Display the results
4. Return to the navigation menu

For direct command-line execution of a specific function:

```bash
python main.py <full_path_to_function> [arguments]
```

For example:
```bash
python main.py devices/get_device_info ABC123
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

MIT License

Copyright (c) 2025 Andrei Trimbitas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

