const fs = require('fs');
const path = require('path');

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

let basePathMacOS = undefined;
exports.basePathMacOS = basePathMacOS;

if (process.platform == 'darwin'){
    if (process.env.NODE_ENV === 'production'){
        basePathMacOS = path.resolve(path.join(__dirname, "..", ".."));
        exports.basePathMacOS = basePathMacOS + '/';
    }
}

const readConfig = () => {
    if (fs.existsSync('src/assets/eliconfig.json')) config = JSON.parse(fs.readFileSync('src/assets/eliconfig.json'));
    else {writeConfig();}
    exports.config = config;
}
exports.readConfig = readConfig; 

const writeConfig = () => {
    fs.writeFileSync('src/assets/eliconfig.json', JSON.stringify(config));
    readConfig();
}
exports.writeConfig = writeConfig;
