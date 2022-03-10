const { execSync } = require("child_process");

const child_process = require("child_process")

const loadEliza = () => {

}

const sendEliza = () => {

}

const killEliza = () => {
    
}

const translate = (text, language = "en") => {
    return child_process.execSync('python -X utf8 python/runnerTranslate.py "' + text + '" "' + language + '" ').toString().replace(/(\r\n|\n|\r)/gm, "");
}
exports.translate = translate;

const speechToText = (file="empty", language = "en") => {
    return child_process.execSync('python python/runnerSpeechToText.py "' + file + '" "' + language + '" ').toString().replace(/(\r\n|\n|\r)/gm, "");
}
exports.speechToText = speechToText;

const textToSpeech = (input, language = "en") => {
    child_process.execSync('python python/runnerTestToSpeech.py "' + input + '" "' + language + '" ').replace(/(\r\n|\n|\r)/gm, "");
}
exports.textToSpeech = textToSpeech;