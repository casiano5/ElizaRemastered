# coding=utf-8
# Test Speech to Text
import pytest
import speech_text

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
    stt_out = speech_text.STT(".SttTestFiles/" + filepath)
    assert stt_out == text

@pytest.mark.parametrize(
    "filepath, language, text", [
        ("dja1.wav","ja","到着しました 大臣"),
        ("dja2.wav","ja","猿は何ですか"),
        ("jfr1.wav","fr","je pense que j'ai mal à la tête"),
        ("jfr2.wav","fr","j'ai perdu mon chapeau hier"),
        ("nzh1.wav","zh-CN","我有两只猫"),
        ("nzh2.wav","zh-CN","早上好中国现在我有冰淇淋"),
        ("nzh3.wav","zh-CN","我最近工作压力很大"),
        ("tzh1.wav","zh-CN","我没有任何问题"),
        ("tzh2.wav","zh-CN","我的头有点疼"),
        ("snl1.wav","nl","het werkt ook op zijn Nederlands"),
        ("snl2.wav","nl","Ik kan niet wachten totdat ik project Eindelijk klaar is"),
        ("sde1.wav","de","es funktioniert auch auf deutsch"),
        ("sde2.wav","de","wir haben viele Test"),
        ("ses1.wav","es","también funciona en español"),
        ("ses2.wav","es","solo unas pocas semanas más"),
        ("skr1.wav","ko","한국어로도 작동합니다"),
        ("skr2.wav","ko","마지막 하나")
    ]
)

def test_mlstt(filepath, language, text):
    stt_out = speech_text.STT(".SttTestFiles/" + filepath, language)
    assert stt_out == text