# Initialization

Create a python virtual environment with
```bash
python3 -m venv .venv
python3 -m pip install -r requirements.txt
```


# To run

## Linux
First check that you have the virtual environment active
```bash
source .venv/bin/activate
```

Then run
```bash
flask --app main run --debug
```
## Windows

```bash
python3 -m flask -m main run --debug
```
