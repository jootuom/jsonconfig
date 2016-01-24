#!/usr/bin/env python3

import json

class JSONConfig(object):
	"""
	This class implements mechanisms for key-value storage in a dictionary-like
	manner and also stores the data persistently on disk in JSON format
	"""
	def __init__(self, filename=None, lazysave=False):
		"""
		Load settings from [filename] to initialize state.
		If [lazysave] is set to True, only save when explicitly called.
		"""
		if not filename: raise IOError("No filename given!")
		
		self.filename = filename
		self.lazysave = lazysave
		self.store = {}
		
		try:
			self.load()
		except FileNotFoundError as e:
			self.reset()
			self.save()
	
	def __repr__(self):
		"""
		Return representation of internal dictionary
		"""
		return repr(self.store)
		
	def __contains__(self, item):
		"""
		Return True if internal dictionary contains [item],
		else False
		"""
		if item in self.store: return True
		else: return False
	
	def __len__(self):
		"""
		Return length of internal dictionary
		"""
		return len(self.store)
	
	def __iter__(self):
		"""
		Iterate over keys of internal dictionary
		"""
		for k in self.store.keys(): yield k
		
	def __delitem__(self, key):
		"""
		Delete [key] from internal dictionary and save 
		unless lazy saving is enabled.
		"""
		del self.store[key]
		if not self.lazysave: self.save()
	
	def __getitem__(self, key):
		"""
		Return [key's] value from internal dictionary
		"""
		return self.store[key]
	
	def __setitem__(self, key, value):
		"""
		Set [key] to [value] in internal dictionary
		"""
		self.store[key] = value
		if not self.lazysave: self.save()
	
	def load(self):
		"""
		Load internal dictionary state from JSON file
		"""
		with open(self.filename, "r") as jsonf:
			self.store = json.load(jsonf)
	
	def save(self):
		"""
		Export internal dictionary state to JSON file
		"""
		with open(self.filename, "w") as jsonf:
			json.dump(self.store, jsonf, indent=4, sort_keys=True)
	
	def clear(self):
		"""
		Clear internal dictionary and save unless lazy saving is enabled
		"""
		self.store = {}
		if not self.lazysave: self.save()
	
	def reset(self):
		"""
		Override this to add default settings for your application
		"""
		pass
	
	def get(self, key):
		"""
		Redirect call to __getitem__
		"""
		return self.__getitem__(key)
	
	def set(self, key, value):
		"""
		Redirect call to __setitem__
		"""
		self.__setitem__(key, value)

	def update(self, iterable):
		"""
		Update internal dictionary from [iterable]
		"""
		self.store.update(iterable)
		if not self.lazysave: self.save()
