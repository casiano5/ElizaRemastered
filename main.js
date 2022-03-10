const { app, BrowserWindow } = require('electron');
const global = require('./js/globals');
const pyConnector = require('./js/pyConnector');

//read config on startup (if exists)
global.readConfig();

const createWindow = () => {
    const window = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
          nodeIntegration: true,
          contextIsolation: false
        }
    });
    window.loadFile('html/index.html');
}

app.whenReady().then(() => {
    createWindow();
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});

//Examples (please remove when no longer needed) 

//Translate using default value (en)
console.log("Translate Out: " + pyConnector.translate("Het werkt"));

//Translate using no default values
console.log("Translate Out: " + pyConnector.translate("This also works", "de"));

//Text to speech (no lang)
pyConnector.textToSpeech("This is a test of text to speech");

//Text to speech (with lang)
pyConnector.textToSpeech("Dit is een test van tekst naar spraak", "nl");

//Speech to text using file (no lang)
console.log("STT Out: " + pyConnector.speechToText("py/test/.SttTestFiles/d1.wav"));

//Speech to text using mic
console.log("Translate Out: " + pyConnector.speechToText(undefined, "en"));

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
