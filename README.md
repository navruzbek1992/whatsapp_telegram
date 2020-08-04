## Send whatsapp data through  telegram 

Simple script downloads data from whatsapp and sends to telegram channel/group.

## Getting Started


### Prerequisites

Script assumes that user has Whatsapp application installed.

Also user should get telegram api keys from [my.telegram.org](https://my.telegram.org/auth).

Script works smoothly for windows system.
Linux users may face problems since each python library requires the user to install its dependencies.

### Installing

Say what the step will be

```bash
pip install -r requirements.txt
```

Pyautogui needs pictures of whatsapp's button. 
User can make exact copy of pics by using PrintScreen key.

Example png files are shown in the repo. 
Since user's screen size is different and pyautogui library finds keys pixel by pixel.

## Deployment

```bash
python wa_tg.py
```

User does not need to use mouse for 2 - 3 minutes. Pyautogui takes control of mouse and downloads data from whatsapp.

## Authors

[Navruz](https://github.com/navruzbek1992)

