from flask import Flask, jsonify
import configparser
from dictionary.dictionary_reader import DictionaryReader

PATHS='paths'
DICTIONARY_KEY='dictionary'
config = configparser.ConfigParser()
config.read("config.ini")


app = Flask(__name__)

reader = DictionaryReader(config[PATHS][DICTIONARY_KEY])


@app.route('/entries/count')
def get_entries():
  # TODO: Actual json
  return jsonify(reader.get_entry_count())

@app.route('/entries/random')
def get_random_entry():
  # TODO: Actual json
  return reader.get_random_entry()

@app.route('/meta')
def get_meta():
  # TODO: Actual json
  return reader.get_meta_info()

