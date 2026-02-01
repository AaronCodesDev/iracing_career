import json
from pathlib import Path

class Translator:
    def __init__(self, lang="en"):
        self.lang = lang
        self.translations = {}
        self.load_translations()

    def load_translations(self):
        path = Path("locales") / f"{self.lang}.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                self.translations = json.load(f)
        else:
            self.translations = {}

    def t(self, key):
        return self.translations.get(key, key)  # Si no encuentra, devuelve la clave

    def set_lang(self, lang):
        self.lang = lang
        self.load_translations()
