const fs = require('fs');

let config = {
    "naturalSoundingLanguages": {
        "en": "English", 
        "fr": "French", 
        "it": "Italian", 
        "ja": "Japanese", 
        "nl": "Dutch", 
        "es": "Spanish", 
        "ko": "Korean", 
        "pt": "Portugese", 
        "zh-CN": "Chinese", 
        "hi": "Hindi", 
        "de": "German"
    }, 
    "textToSpeechEnable": false, 
    "speechToTextEnable": false, 
    "speakerIconPath": "disSpeaker_Icon.png", 
    "micIconPath": "disMic.png", 
    "language": "en"
};
exports.config = config;

const readConfig = () => {
    if (fs.existsSync('res/eliconfig.json')) config = JSON.parse(fs.readFileSync('res/eliconfig.json'));
    else {writeConfig();}
    exports.config = config;
}
exports.readConfig = readConfig; 

const writeConfig = () => {
    fs.writeFileSync('res/eliconfig.json', JSON.stringify(config));
    readConfig();
}
exports.writeConfig = writeConfig;
