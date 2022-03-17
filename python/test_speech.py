# Test Text to Speech (These are manual, require review in output folder)
import os
import pytest
from pathlib import Path
import shutil
import speech

@pytest.mark.parametrize(
    "input, lang", [
        ("This is a test of text to speech functionality.", "en"),
        ("Twee dingen zijn oneindig: het universum en de menselijke domheid; en ik ben niet zeker van het universum.", "nl"),
        ("In drei worten kann ich alles zusammenfassen, was ich über das leben gelernt habe: es geht weiter.", "de"),
        ("Esta es una prueba de la funcionalidad de texto a voz.", "es"),
        ("Duas coisas são infinitas: o universo e a estupidez humana; e não tenho certeza sobre o universo.", "pt"),
        ("In tre parole posso riassumere tutto ciò che ho imparato sulla vita: va avanti.", "it"),
        ("Ceci est un test de la fonctionnalité de synthèse vocale.", "fr"),
        ("두 가지는 무한합니다. 우주와 인간의 어리석음입니다. 그리고 나는 우주에 대해 잘 모릅니다.", "ko"),
        ("3つの言葉で私は人生について学んだすべてを要約することができます:それは続きます。", "ja"),
        ("这是对文本到语音功能的测试。", "zh"),
        ("दो चीजें अनंत हैं: ब्रह्मांड और मानव मूर्खता; और मैं ब्रह्मांड के बारे में निश्चित नहीं हूं।", "hi")
    ]
)
def test_tts(input, lang):
    try:
        speech.speech(input, lang)
    except Exception as exc:
        pytest.fail(exc, pytrace=True)
