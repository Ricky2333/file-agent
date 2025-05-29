# Simple File Agent

## Overview

Simple File Agent is a command-line based file management assistant that uses AI technology to understand and execute various file operation commands. This tool allows users to manage their file system through natural language instructions, including creating, deleting, moving, and renaming files and folders.



## Features

- **File Operations**: Create, delete, rename, and move files
- **Folder Operations**: Create folders and list folder contents
- **Content Management**: View file content and append content to files
- **Natural Language Interaction**: Execute complex file operations through simple natural language commands
- **Interactive Interface**: Clean command-line interaction

## Technology Stack

- Python
- pydantic-ai
- OpenAI API (supporting multiple providers like DeepSeek and Qwen (DashScope))



## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/simple-file-agent.git
cd file-agent
```


2. Create and activate a virtual environment
```
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up API access

   Depending on the model you intend to use (configured in `main.py`), you'll need to set up the corresponding API key:

   - **For DeepSeek (if `MODEL = 'DEEPSEEK'`)**:
     - Visit [DeepSeek Platform](https://platform.deepseek.com/api_keys)
     - Sign up for an account if you haven't already
     - Go to API settings in your dashboard
     - Generate a new API key
     - Copy your API key

   - **For Qwen (DashScope) (if `MODEL = 'QWEN'`)**:
     - Visit [Alibaba Cloud DashScope Console](https://dashscope.console.aliyun.com/)
     - Log in or sign up for an Alibaba Cloud account.
     - Navigate to the API Key management section (usually under your account settings or a specific service like "Model Service R&D Platform").
     - Create or retrieve your API key.

5. Configure environment variables.
   Create a `.env` file in the root directory of the project. Add the API key corresponding to the model you plan to use.

   - If using DeepSeek:
     ```bash
     echo "DEEPSEEK_API_KEY=your_deepseek_api_key_here" > .env
     ```
   - If using Qwen (DashScope):
     ```bash
     echo "DASHSCOPE_API_KEY=your_dashscope_api_key_here" > .env
     ```
   You can also add both keys if you plan to switch between models, but `main.py` will only use the one relevant to the `MODEL` variable setting.

## Usage

Run the main program:

```
python main.py
```

Then, you can input commands in natural language. Here are some example commands from our test prompts:

### Basic File Operations
- Create files: "Create a file named 'config.json' with the content: {"key": "value"}"
- Delete files: "Delete a file named 'unwanted.txt' from the 'temp' folder"
- Rename files: "Rename a file named 'file5.txt' to 'file0.txt' in 'documents' folder"
- Move files: "Move a file named 'e' from the 'data' folder to the 'temp' folder"
### Content Management
- View content: "Display the content of a file named 'readme.md'"
- Append content: "Append the text 'Additional content.' to an existing file named 'file4.txt' from 'documents' folder"
- Create with content: "Create a file named 'story.txt' and write a story into it"
### Folder Operations
- List contents: "List all the files in the 'prompts' folder"
- Create folders: "Create a folder named 'backup' and copy all files from the 'data' folder into it"
- Complex operations: "Create a new folder named 'program'. Within this folder, create 6 files that are written in 6 programming languages like Python, C++, etc., each containing a 'Hello, World!' program"
### Advanced Operations
- File Analysis: "For each file in the data folder, read the source code and generate a brief report describing the programming language used, code purpose, and notable features. Save reports as .txt files in a new 'reports' folder"
- Selective File Management: "In the trash folder, delete all files except those with .pdf extension, then rename the remaining .pdf files to doc1.pdf, doc2.pdf, etc."
- Batch File Creation: "Create a folder named trash with at least 6 files in various formats (.txt, .md, .log, .csv, .pdf) containing simple placeholder content"

Type "exit" to quit the program.