# Test Text to Speech (These are manual, require review in output folder)
import os
import pytest
from pathlib import Path
import shutil
import os

@pytest.mark.parametrize(
    "input", [
        ("This is a test of text to speech functionality"),
        ("Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."),
        ("In three words I can sum up everything I've learned about life: it goes on.")
    ]
)
def test_tts(input):
    try:
        os.system("python py/speech.py " + "\"" + input + "\" " + "\"en\"")
    except Exception as exc:
        pytest.fail(exc, pytrace=True)
