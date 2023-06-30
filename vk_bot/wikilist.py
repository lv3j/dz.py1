import wikipedia

def get_wiki(art):
    wikipedia.set_lang("ru")
    try:
        return f"{wikipedia.summary(art)}"
    except Exception:
        return f"Нет такой"