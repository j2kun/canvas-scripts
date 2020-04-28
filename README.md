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


## Download all gradebooks

Run

```bash
python download_gradebook.py
```
