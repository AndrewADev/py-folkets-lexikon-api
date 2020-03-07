# py_folkets_api
A Flask-based API for searching the Swedish _Folkets Lexikon_ (People's Dictionary)

## Configuration & Setup
The app is intended as an API for searching an existing copy of the _Folkets Lexikon_, and, as such, requires a local copy be available.

By default, it will look for the dictionary under `./data/folkets_en_sv_public.xdxf`.

Be sure to update the path in `config.ini` if you are using a different location.