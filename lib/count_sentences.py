#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    # init method initializes the class with a default value and sets the_value attribute to none initially then sets the value using the value property setter 
    # self._value = None #Private Attribute
    self.value = value 

  @property
  def value(self):
    # ._ indicates that the atttribute is intended to be private 
    return self._value 

  @value.setter
  def value(self, new_value):
    if isinstance(new_value, str):
      self._value = new_value
    else:
      print("The value must be a string.")  


  def is_sentence(self):
    return self.value.endswith('.')  

  def  is_question(self):
    return self.value.endswith('?') 

  def is_exclamation(self):
    return self.value.endswith('!')  

  def count_sentences(self):
    if not self.value:
      return 0
    sentences = [sentence for sentence in self.value.replace('!', '.').replace('?', '.').split('.')if sentence.strip()] 
    return len(sentences)    

