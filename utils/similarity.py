from difflib import SequenceMatcher

def calculate_similarity(text1, text2):
    similarity = SequenceMatcher(None, text1, text2).ratio()
    return round(similarity * 100, 2)