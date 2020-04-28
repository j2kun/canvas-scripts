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
CANVAS_TOKEN="<add secret here>"
```

Go to https://developers.google.com/drive/api/v3/quickstart/python
and follow Step 1 to create a new Cloud Platform project and enable the Drive API.

Save the file credentials.json to your working directory. 


## Download all gradebooks and upload each to your Drive account:

Run

```bash
python download_gradebook.py
```
