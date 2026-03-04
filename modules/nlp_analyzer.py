import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Fallback or instruction to download
    print("Downloading 'en_core_web_sm' model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def analyze_text(text):
    """
    Analyzes the text to extract entities and key phrases.
    Returns a dictionary with entities and tokens.
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    # Basic keyword extraction (nouns and proper nouns)
    keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop]
    
    return {
        "entities": entities,
        "keywords": list(set(keywords)),
        "summary": text[:200] + "..." if len(text) > 200 else text
    }
