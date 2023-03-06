# t-fastapi-react-mongodb

youtube link: https://www.youtube.com/watch?v=SORiTsvnU28
github repository: https://github.com/ArjanCodes/2023-fastapi

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

