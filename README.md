# py-folkets-lexikon-api
A Flask-based API for accessing and searching the Swedish-English _Folkets Lexikon_ (People's Dictionary).

## Configuration & Setup

### Initial setup

#### Dependencies
1. `python -m venv ENV`
2. Varies based on platform. For Windows (including most terminal emulators): `ENV\Scripts\activate.bat`. 
3. (for local development) `pip install --no-cache-dir -r requirements\dev.txt`

#### App Data

Settings are sourced from `config.ini`. A default configuration is available via the provided `config.ini.template`. You can easily create your own copy by running the command `cp config.ini.template config.ini`.

#### Running the app

On Windows:
```
set FLASK_APP=folkets_lexikon_api
set FLASK_ENV=development
flask run
```

On Windows, you can also use the included [set-debug.bat](./set-debug.bat) script to set the needed variables.

See: https://stackoverflow.com/a/17322636

### Data configuration
The app is intended as an API for searching an existing copy of the _Folkets Lexikon_, and, as such, requires a local copy be available.

By default, it will look for the dictionary under `./data/folkets_en_sv_public.xdxf`.

Be sure to update the path in `config.ini` if you are using a different location.