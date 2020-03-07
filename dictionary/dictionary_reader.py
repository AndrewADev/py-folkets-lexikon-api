from random import randrange
from lxml import etree


# Reads a dictionary
class DictionaryReader(object):
  def __init__(self, file_path):
    self.__file_path = file_path
    self.__tree = etree.parse(file_path)

  def __get_entries(self):
    return self.__tree.find('.//lexicon')
  
  def get_random_entry(self):
    count = self.get_entry_count()
    entry_idx = randrange(count)
    return etree.tostring(self.__get_entries().getchildren()[entry_idx])

  def get_meta_info(self):
    meta_info = self.__tree.find('.//meta_info')
    return etree.tostring(meta_info)

  def get_entry_count(self):
    lexikon_el = self.__get_entries()
    return len(lexikon_el.getchildren())

  
