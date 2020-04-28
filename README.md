# Canvas scripts

Helpful scripts for working with Canvas.

## Setup

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a file called `.env`

```
CANVAS_URL="<Canvas url here>"
CANVAS_TOKEN="<add secret here>"
```

Go to https://developers.google.com/drive/api/v3/quickstart/python

Follow Step 1 to create a new Cloud Platform project and enable the Drive API.

Save the file `credentials.json` to your working directory. 


## Download all gradebooks and upload each to your Drive account:

Run

```bash
python download_gradebook.py
```

If it's your first time running this script, you will be asked to log in 
to your Google account to authorize Google Drive Api to access and modify your Drive account.

Run the script a second time after authorizing to upload the gradebook to your Drive.
