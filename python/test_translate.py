# Test Translate
import pytest
import translate

# detect to english
@pytest.mark.parametrize(
    "text, expected", [
        ("Dit is een test van de vertaalfunctionaliteit in onze applicatie","This is a test of translation functionality in our application"),
        ("Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung","This is a test of translation functionality in our application"),
        ("Esta es una prueba de la funcionalidad de traducción en nuestra aplicación","This is a test of the translation functionality in our application"),
        ("Este é um teste da funcionalidade de tradução em nosso aplicativo","This is a test of translation functionality in our application"),
        ("Questo è un test della funzionalità di traduzione nella nostra applicazione","This is a test of the translation feature in our application"),
        ("Ceci est un test de fonctionnalité de traduction dans notre application","This is a translation functionality test in our application"),
        ("이것은 우리 응용 프로그램의 번역 테스트입니다","This is the translation test of our application"),
        ("これは、アプリケーションの翻訳機能のテストです","This is a test of the application translation function"),
        ("这是对我们应用程序中翻译功能的测试","This is a test of the translation function in our application."),
        ("यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है","This is the test of translation functionality in our application"),
    ]
)
def test_english(text, expected):
    assert translate.translate(text) == expected

@pytest.mark.parametrize(
    "text, expected", [
        ("This is a test of translation functionality in our application","Dit is een test van vertaalfunctionaliteit in onze applicatie"), #replace with eng
        ("Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung","Dit is een test van vertaalfunctionaliteit in onze applicatie"),
        ("Esta es una prueba de la funcionalidad de traducción en nuestra aplicación","Dit is een test van de vertaalfunctionaliteit in onze applicatie"),
        ("Este é um teste da funcionalidade de tradução em nosso aplicativo","Dit is een test van vertaalfunctionaliteit in onze applicatie"),
        ("Questo è un test della funzionalità di traduzione nella nostra applicazione","Dit is een test van de vertaalfunctie in onze applicatie"),
        ("Ceci est un test de fonctionnalité de traduction dans notre application","Dit is een vertaalfunctionaliteitstest in onze applicatie"),
        ("이것은 우리 응용 프로그램의 번역 테스트입니다","Dit is de vertaaltest van onze applicatie"),
        ("これは、アプリケーションの翻訳機能のテストです","Dit is een test van de functie voor het oplossen van applicaties"),
        ("这是对我们应用程序中翻译功能的测试","Dit is een test van de vertaalfunctie in onze applicatie."),
        ("यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है","Dit is de test van de vertaalfunctionaliteit in onze toepassing"),
    ]
)
def test_dutch(text, expected):
    assert translate.translate(text, "nl") == expected

@pytest.mark.parametrize(
    "text, expected", [
        ("Dit is een test van de vertaalfunctionaliteit in onze applicatie","Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung"),
        ("This is a test of translation functionality in our application","Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung"),
        ("Esta es una prueba de la funcionalidad de traducción en nuestra aplicación","Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung"),
        ("Este é um teste da funcionalidade de tradução em nosso aplicativo","Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung"),
        ("Questo è un test della funzionalità di traduzione nella nostra applicazione","Dies ist ein Test der Übersetzungsfunktion in unserer Anwendung"),
        ("Ceci est un test de fonctionnalité de traduction dans notre application","Dies ist ein Übersetzungsfunktionstest in unserer Anwendung"),
        ("이것은 우리 응용 프로그램의 번역 테스트입니다","Dies ist der Übersetzungstest unserer Anwendung"),
        ("これは、アプリケーションの翻訳機能のテストです","Dies ist ein Test der Anwendungsübersetzungsfunktion"),
        ("这是对我们应用程序中翻译功能的测试","Dies ist ein Test der Übersetzungsfunktion in unserer Anwendung."),
        ("यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है","Dies ist der Test der Übersetzungsfunktionalität in unserer Anwendung"),
    ]
)
def test_german(text, expected):
    assert translate.translate(text, "de") == expected

@pytest.mark.parametrize(
    "text, expected", [
        ("Dit is een test van de vertaalfunctionaliteit in onze applicatie","Esta es una prueba de funcionalidad de traducción en nuestra aplicación."),
        ("Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung","Esta es una prueba de funcionalidad de traducción en nuestra aplicación."),
        ("This is a test of translation functionality in our application","Esta es una prueba de funcionalidad de traducción en nuestra aplicación."),
        ("Este é um teste da funcionalidade de tradução em nosso aplicativo","Esta es una prueba de funcionalidad de traducción en nuestra aplicación."),
        ("Questo è un test della funzionalità di traduzione nella nostra applicazione","Esta es una prueba de la característica de traducción en nuestra aplicación."),
        ("Ceci est un test de fonctionnalité de traduction dans notre application","Esta es una prueba de funcionalidad de traducción en nuestra aplicación."),
        ("이것은 우리 응용 프로그램의 번역 테스트입니다","Esta es la prueba de traducción de nuestra aplicación."),
        ("これは、アプリケーションの翻訳機能のテストです","Esta es una prueba de la función de traducción de aplicaciones."),
        ("这是对我们应用程序中翻译功能的测试","Esta es una prueba de la función de traducción en nuestra aplicación."),
        ("यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है","Esta es la prueba de la funcionalidad de traducción en nuestra aplicación."),
    ]
)
def test_spanish(text, expected):
    assert translate.translate(text, "es") == expected

@pytest.mark.parametrize(
    "text, expected", [
        ("Dit is een test van de vertaalfunctionaliteit in onze applicatie","Este é um teste de funcionalidade de tradução em nossa aplicação"),
        ("Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung","Este é um teste de funcionalidade de tradução em nossa aplicação"),
        ("Esta es una prueba de la funcionalidad de traducción en nuestra aplicación","Este é um teste da funcionalidade de tradução em nossa aplicação"),
        ("This is a test of translation functionality in our application","Este é um teste de funcionalidade de tradução em nossa aplicação"),
        ("Questo è un test della funzionalità di traduzione nella nostra applicazione","Este é um teste do recurso de tradução em nosso aplicativo"),
        ("Ceci est un test de fonctionnalité de traduction dans notre application","Este é um teste de funcionalidade de tradução em nosso aplicativo"),
        ("이것은 우리 응용 프로그램의 번역 테스트입니다","Este é o teste de tradução de nossa aplicação"),
        ("これは、アプリケーションの翻訳機能のテストです","Este é um teste da função de tradução de aplicativos"),
        ("这是对我们应用程序中翻译功能的测试","Este é um teste da função de tradução em nosso aplicativo."),
        ("यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है","Este é o teste de funcionalidade de tradução em nossa aplicação"),
    ]
)
def test_portuguese(text, expected):
    assert translate.translate(text, "pt") == expected

@pytest.mark.parametrize(
    "text, expected", [
        ("Dit is een test van de vertaalfunctionaliteit in onze applicatie","Questa è una prova di funzionalità di traduzione nella nostra applicazione"),
        ("Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung","Questa è una prova di funzionalità di traduzione nella nostra applicazione"),
        ("Esta es una prueba de la funcionalidad de traducción en nuestra aplicación","Questo è un test della funzionalità di traduzione nella nostra applicazione"),
        ("Este é um teste da funcionalidade de tradução em nosso aplicativo","Questa è una prova di funzionalità di traduzione nella nostra applicazione"),
        ("This is a test of translation functionality in our application","Questa è una prova di funzionalità di traduzione nella nostra applicazione"),
        ("Ceci est un test de fonctionnalité de traduction dans notre application","Questo è un test di funzionalità di traduzione nella nostra applicazione"),
        ("이것은 우리 응용 프로그램의 번역 테스트입니다","Questo è il test di traduzione della nostra applicazione"),
        ("これは、アプリケーションの翻訳機能のテストです","Questo è un test della funzione di traduzione dell'applicazione"),
        ("这是对我们应用程序中翻译功能的测试","Questo è un test della funzione di traduzione nella nostra applicazione."),
        ("यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है","Questo è il test della funzionalità di traduzione nella nostra applicazione"),
    ]
)
def test_italian(text, expected):
    assert translate.translate(text, "it") == expected

@pytest.mark.parametrize(
    "text, expected", [
        ("Dit is een test van de vertaalfunctionaliteit in onze applicatie","Ceci est un test de fonctionnalité de traduction dans notre application"),
        ("Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung","Ceci est un test de fonctionnalité de traduction dans notre application"),
        ("Esta es una prueba de la funcionalidad de traducción en nuestra aplicación","Ceci est un test de la fonctionnalité de traduction dans notre application"),
        ("Este é um teste da funcionalidade de tradução em nosso aplicativo","Ceci est un test de fonctionnalité de traduction dans notre application"),
        ("Questo è un test della funzionalità di traduzione nella nostra applicazione","Ceci est un test de la fonctionnalité de traduction dans notre application"),
        ("This is a test of translation functionality in our application","Ceci est un test de fonctionnalité de traduction dans notre application"),
        ("이것은 우리 응용 프로그램의 번역 테스트입니다","C'est le test de traduction de notre application"),
        ("これは、アプリケーションの翻訳機能のテストです","Ceci est un test de la fonction de traduction de l'application"),
        ("这是对我们应用程序中翻译功能的测试","Ceci est un test de la fonction de traduction dans notre application."),
        ("यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है","Ceci est le test de la fonctionnalité de traduction dans notre application"),
    ]
)
def test_french(text, expected):
    assert translate.translate(text, "fr") == expected

@pytest.mark.parametrize(
    "text, expected", [
        ("Dit is een test van de vertaalfunctionaliteit in onze applicatie","이것은 우리의 응용 프로그램에서 번역 기능의 테스트입니다."),
        ("Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung","이것은 우리의 응용 프로그램에서 번역 기능의 테스트입니다."),
        ("Esta es una prueba de la funcionalidad de traducción en nuestra aplicación","이것은 우리의 응용 프로그램에서 번역 기능의 테스트입니다."),
        ("Este é um teste da funcionalidade de tradução em nosso aplicativo","이것은 우리의 응용 프로그램에서 번역 기능의 테스트입니다."),
        ("Questo è un test della funzionalità di traduzione nella nostra applicazione","이것은 우리의 응용 프로그램에서 번역 기능의 테스트입니다."),
        ("Ceci est un test de fonctionnalité de traduction dans notre application","이것은 우리의 응용 프로그램에서 번역 기능 테스트입니다"),
        ("This is a test of translation functionality in our application","이것은 우리의 응용 프로그램에서 번역 기능의 테스트입니다."),
        ("これは、アプリケーションの翻訳機能のテストです","이것은 응용 프로그램 번역 기능의 테스트입니다"),
        ("这是对我们应用程序中翻译功能的测试","이것은 우리의 응용 프로그램에서 번역 기능의 테스트입니다."),
        ("यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है","이것은 응용 프로그램에서 번역 기능의 테스트입니다."),
    ]
)
def test_korean(text, expected):
    assert translate.translate(text, "ko") == expected

@pytest.mark.parametrize(
    "text, expected", [
        ("Dit is een test van de vertaalfunctionaliteit in onze applicatie","これは私たちのアプリケーションの翻訳機能のテストです。"),
        ("Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung","これは私たちのアプリケーションの翻訳機能のテストです。"),
        ("Esta es una prueba de la funcionalidad de traducción en nuestra aplicación","これは私たちのアプリケーションの翻訳機能のテストです。"),
        ("Este é um teste da funcionalidade de tradução em nosso aplicativo","これは私たちのアプリケーションの翻訳機能のテストです。"),
        ("Questo è un test della funzionalità di traduzione nella nostra applicazione","これは私たちのアプリケーションの翻訳機能のテストです。"),
        ("Ceci est un test de fonctionnalité de traduction dans notre application","これは私たちのアプリケーションの翻訳機能テストです"),
        ("이것은 우리 응용 프로그램의 번역 테스트입니다","これは私たちのアプリケーションの翻訳テストです"),
        ("This is a test of translation functionality in our application","これは私たちのアプリケーションの翻訳機能のテストです。"),
        ("这是对我们应用程序中翻译功能的测试","これは私たちのアプリケーションの翻訳機能のテストです。"),
        ("यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है","これは私たちのアプリケーションにおける翻訳機能のテストです"),
    ]
)
def test_japanese(text, expected):
    assert translate.translate(text, "ja") == expected

@pytest.mark.parametrize(
    "text, expected", [
        ("Dit is een test van de vertaalfunctionaliteit in onze applicatie","这是我们申请中的翻译功能的测试"),
        ("Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung","这是我们申请中的翻译功能的测试"),
        ("Esta es una prueba de la funcionalidad de traducción en nuestra aplicación","这是我们申请中的翻译功能的测试"),
        ("Este é um teste da funcionalidade de tradução em nosso aplicativo","这是我们申请中的翻译功能的测试"),
        ("Questo è un test della funzionalità di traduzione nella nostra applicazione","这是我们申请中翻译功能的测试"),
        ("Ceci est un test de fonctionnalité de traduction dans notre application","这是我们应用中的翻译功能测试"),
        ("이것은 우리 응용 프로그램의 번역 테스트입니다","这是我们申请的翻译测试"),
        ("これは、アプリケーションの翻訳機能のテストです","这是应用翻译功能的测试"),
        ("This is a test of translation functionality in our application","这是我们申请中的翻译功能的测试"),
        ("यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है","这是我们申请中翻译功能的测试"),
    ]
)
def test_chinese_simplified(text, expected):
    assert translate.translate(text, "zh-CN") == expected

@pytest.mark.parametrize(
    "text, expected", [
        ("Dit is een test van de vertaalfunctionaliteit in onze applicatie","यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है"),
        ("Dies ist ein Test der Übersetzungsfunktionalität in unserer Anwendung","यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है"),
        ("Esta es una prueba de la funcionalidad de traducción en nuestra aplicación","यह हमारे आवेदन में अनुवाद कार्यक्षमता का एक परीक्षण है"),
        ("Este é um teste da funcionalidade de tradução em nosso aplicativo","यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है"),
        ("Questo è un test della funzionalità di traduzione nella nostra applicazione","यह हमारे आवेदन में अनुवाद सुविधा का एक परीक्षण है"),
        ("Ceci est un test de fonctionnalité de traduction dans notre application","यह हमारे आवेदन में एक अनुवाद कार्यक्षमता परीक्षण है"),
        ("이것은 우리 응용 프로그램의 번역 테스트입니다","यह हमारे आवेदन का अनुवाद परीक्षण है"),
        ("これは、アプリケーションの翻訳機能のテストです","यह एप्लिकेशन अनुवाद फ़ंक्शन का एक परीक्षण है"),
        ("这是对我们应用程序中翻译功能的测试","यह हमारे आवेदन में अनुवाद फ़ंक्शन का एक परीक्षण है।"),
        ("This is a test of translation functionality in our application","यह हमारे आवेदन में अनुवाद कार्यक्षमता का परीक्षण है"),
    ]
)
def test_hindi(text, expected):
    assert translate.translate(text, "hi") == expected
