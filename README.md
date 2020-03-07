# py-folkets-lexikon-api
A Flask-based API for accessing and searching the Swedish-English _Folkets Lexikon_ (People's Dictionary).

## Configuration & Setup

### Initial setup
Settings are sourced from `config.ini`. A default configuration is available via the provided `config.ini.template`. You can easily create your own copy by running the command `cp config.ini.template config.ini`.

### Data configuration
The app is intended as an API for searching an existing copy of the _Folkets Lexikon_, and, as such, requires a local copy be available.

By default, it will look for the dictionary under `./data/folkets_en_sv_public.xdxf`.

Be sure to update the path in `config.ini` if you are using a different location.