## Random Password Generator
## Requirements
- Python 3.10 or higher
- Tkinter installed
- pyperclip installed
## Features
- Generates Password between the range of 3 to 14
- By default, uses lower case alphabets are password
- Option to include
  - Special Characters
  - Upper case
  - Numbers
- Option to exclude characters
- Button to copy the generated password
## Limitations/Bugs
- Password generated will sometimes not include selected character set (e.g. Upper case characters are not included in password even after selecting it)
- Password may sometimes take longer to generate cause of multiple recursions
- Excluding too many characters can affect the program and become unresponsive
- Could not add an option to sperately include lower case alphabets
