# Test Text to Speech (These are manual, require review in output folder)
import os
import pytest
from pathlib import Path
import shutil
import speech

def test_tts_folder():
    dirpath = Path("test_tts_manual")
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)
    os.makedirs("test_tts_manual")

@pytest.mark.parametrize("input,filename", [("This is a test of text to speech functionality","0"),("Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.","1"),("In three words I can sum up everything I've learned about life: it goes on.","3")])
def test_tts(input, filename):
    with open("test_tts_manual/"+filename+".txt", "w") as f:
        f.write(input)
    try:
        speech.speech(input)
    except Exception as exc:
        pytest.fail(exc, pytrace=True)
