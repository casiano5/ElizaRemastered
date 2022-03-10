//This file contains some examples of how to use pyConnector and global config
//Responses in BrowserWindow console.

//using eliza...
pyConnector.sendEliza("Hello Eliza");
//note that output is handleded in elizaEventHelper.js


//Translate using default value (en)
console.log("Translate Out: " + pyConnector.translate("Het werkt"));

//Translate using no default values
console.log("Translate Out: " + pyConnector.translate("This also works", "de"));

//Text to speech (no lang)
pyConnector.textToSpeech("This is a test of text to speech");

//Text to speech (with lang)
pyConnector.textToSpeech("Dit is een test van tekst naar spraak", "nl");

//Speech to text using file (no lang)
console.log("STT File Out: " + pyConnector.speechToText("python/.SttTestFiles/d1.wav"));

//Speech to text using mic
console.log("Start speaking in 2 seconds.");
console.log("STT Mic Out: " + pyConnector.speechToText(undefined, "en"));

//To edit the config file
global.config = {"hello": "This is good"};

//or by object ref:
global.config.language = "nl";

//To dereference:
global.config.speakerIconPath;

//To read the config to the file
global.readConfig();

//To write current config var to file
global.writeConfig();