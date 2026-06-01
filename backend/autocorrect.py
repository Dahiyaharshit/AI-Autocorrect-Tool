from textblob import TextBlob

def correct_text(text):

    corrected_text = str(TextBlob(text).correct())

    return corrected_text