from utils.translation import Translator

translator = Translator(lang="en")  # por defecto inglés

def home_view():
    from flet import Column, Text
    return Column([
        Text(translator.t("home_title")),
        Text(translator.t("money_earned") + ": $100")
    ])
