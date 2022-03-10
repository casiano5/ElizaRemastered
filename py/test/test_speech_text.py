# Test Speech to Text
import pytest
import os

@pytest.mark.parametrize(
    "filepath,text", [
        ("d1.wav","I have two cats"),
        ("d2.wav","the kitchen is red"),
        pytest.param("d3.wav","since the age of nine I traveled to 89 countries I love to travel", marks=pytest.mark.xfail(reason="'ed' not enunciated")),
        ("d4.wav","hey Eliza I don't feel well"),
        ("d5.wav","hey Eliza I remember when inflation wasn't so high"),
        ("j1.wav","I have two cats"),
        ("j2.wav","the kitchen is red"),
        pytest.param("j3.wav","since the age of nine, I traveled to 89 countries I love to travel", marks=pytest.mark.xfail(reason="'eighty' not enunciated")),
        ("j4.wav","hey Eliza I don't feel well"),
        pytest.param("j5.wav","hey Eliza I remember when inflation wasn't so high", marks=pytest.mark.xfail(reason="'E' in Eliza hard to hear, blur with e in hey?")),
        ("n1.wav","my head's been bothering me lately"),
        pytest.param("n2.wav","I hate doing leetcode", marks=pytest.mark.xfail(reason="leetcode not in dictionary")),
        ("n3.wav","my wife just said she hates my cooking"),
        ("n4.wav","I lost my car keys"),
        ("n5.wav","I need a doctor"),
        ("s1.wav","I'm in pain"),
        ("s2.wav","I spend too much money on computers"),
        ("s3.wav","please recognize this statement accurately"),
        ("s4.wav","why does your output not include punctuation"),
        ("s5.wav","how many hours of sleep is normal"),
        ("t1.wav","I don't have any problems"),
        ("t2.wav","I'm fine how are you"),
        ("t3.wav","I have a headache"),
        ("t4.wav","what do you think about AI"),
        ("t5.wav","I'm feeling stressed about an upcoming project")
    ]
)
def test_stt(filepath, text):
    stream = os.popen("python py/speech_text.py " + "\"" + "py/test/.SttTestFiles/" + filepath + "\" " + "\"" + "en" + "\"")
    stt_out = stream.read().strip()
    assert stt_out == text