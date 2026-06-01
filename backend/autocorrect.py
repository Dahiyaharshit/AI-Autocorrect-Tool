from textblob import TextBlob
import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def correct_text(text):

    spell_corrected = str(TextBlob(text).correct())

    matches = tool.check(spell_corrected)

    final_text = language_tool_python.utils.correct(
        spell_corrected,
        matches
    )

    return final_text