# Password Manager

A simple and secure password manager application built with Python and Tkinter. This application helps you generate and store passwords for different websites and services.

## Features

- Generate strong, random passwords
- Store website credentials (website, email/username, password)
- Search functionality to quickly find saved credentials
- Copy generated passwords to clipboard automatically
- Simple and intuitive user interface
- Data stored locally in JSON format for better organization
- Automatic website name capitalization
- Improved error handling and user feedback

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- pyperclip library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Adnan27v/My-Password-Manager.git
```

2. Install the required package:
```bash
pip install pyperclip
```

3. Run the application:
```bash
python main.py
```

## Usage

1. Enter the website name
2. Enter your email/username
3. Either enter your password manually or click "Generate Password" to create a strong random password
4. Click "Add" to save the credentials
5. The password will be automatically copied to your clipboard
6. Use the "Search" button to quickly find saved credentials for any website

## Data Storage

- All credentials are stored in a local `data.json` file
- Data is organized in a structured JSON format for better readability and maintenance
- Website names are automatically capitalized for consistency
- Each website entry contains email and password information

## Security Note

This is a simple password manager for demonstration purposes. For production use, consider:
- Using encryption for stored passwords
- Implementing a master password
- Using a secure database instead of a JSON file
- Adding additional security features

## License

This project is open source and available under the MIT License. 