# jsonconfig

Python module for storing application settings in JSON format on disk and accessing them in a dictionary-like manner.

## Usage

Works like a dictionary that gets initialized with a `json.load()` from the specified file and stored with `json.dump()` on every change (by default).

    >>> from jsonconfig import JSONConfig
    >>> conf = JSONConfig("settings.json")
    >>> conf["url"]
    'http://google.com'
	>>> conf["username"] = "test"
	>>> del conf["password"]
	>>> 

Define your own reset method on the JSONConfig class to initialize the settings file as needed:

    class Settings(JSONConfig):
    	def reset(self):
    			self.store = {"url": "", "username": "", "password": ""}
    
	Settings = Settings("settings.json")

Then you can also reset your config back to defaults by calling `.reset()` yourself.

If you don't want automatic saving on every change, you can disable that during initialization:

    >>> conf = JSONConfig("settings.json", True)
