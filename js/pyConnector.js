const { execSync } = require("child_process");

const child_process = require("child_process")

const loadEliza = () => {

}

const sendEliza = () => {

}

const killEliza = () => {
    
}

const translate = (text, language = "en") => {
    return child_process.execSync('python py/translate.py "' + text + '" "' + language + '" ').toString();
}
exports.translate = translate;

const speechToText = (file="empty", language = "en") => {
    return child_process.execSync('python py/speech_text.py "' + file + '" "' + language + '" ').toString();
}
exports.speechToText = speechToText;

const textToSpeech = (input, language = "en") => {
    child_process.execSync('python py/speech.py "' + input + '" "' + language + '" ');
}
exports.textToSpeech = textToSpeech;