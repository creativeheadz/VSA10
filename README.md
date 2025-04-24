# VSA 10 API Tool

This tool provides a set of Python scripts to interact with the VSA 10 API. It allows you to automate various tasks, such as retrieving device information, managing groups, and running automation workflows.

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

The tool consists of several Python scripts, each designed to perform a specific task. You can run these scripts from the command line:

```bash
python main.py <script_name> [arguments]
```

For example, to get all devices, you would run:

```bash
python main.py get_all_devices
```

Refer to the individual script documentation for specific usage instructions and available arguments.

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

