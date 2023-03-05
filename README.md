# t-fastapi-react-mongodb

Ha nincs venv létre kell hozni a projekt könyvtárában:
```bash
$ python3 -m venv venv

# activate
$ source venv/bin/activate

# deactivate
$ deactivate
```

Csomagok telepítése venv-be:

```bash
$ pip install -r requirements.txt
```

Uvicorn szerver futtatása:

```bash
$ uvicorn main:app --reload
```

Minden szükséges csomag mentése

```bash
$ pipreqs . --force
```

