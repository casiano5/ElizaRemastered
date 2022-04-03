const child_process = require("child_process")
const global = require('./globals');

let eliza;

const loadEliza = (callback) => {
    eliza = child_process.spawn('python',['-i', 'python/eliza.py']);
    eliza.stdout.on('data', (data) => {
        callback(data.toString().replace(/(\r\n|\n|\r)/gm, ""));
    });
}
exports.loadEliza = loadEliza;

const loadElizaMacOS = (callback) => {
    let spawnPath = global.basePathMacOS + 'python/eliza.py'
    eliza = child_process.spawn('python3',['-i', spawnPath]);
    eliza.stdout.on('data', (data) => {
        callback(data.toString().replace(/(\r\n|\n|\r)/gm, ""));
    });
}
if (global.basePathMacOS != undefined) exports.loadEliza = loadElizaMacOS;

const sendEliza = (text) => {
    eliza.stdin.write(text + "\n");
}
exports.sendEliza = sendEliza;

const killEliza = () => {
    eliza.stdin.end();
}
exports.killEliza = killEliza;

const translate = (text, language = "en") => {
    return child_process.execSync('python -X utf8 python/runnerTranslate.py "' + text + '" "' + language + '" ').toString().replace(/(\r\n|\n|\r)/gm, "");
}
exports.translate = translate;

const translateMacOS = (text, language = "en") => {
    return child_process.execSync('python3 -X utf8 ' + global.basePathMacOS + 'python/runnerTranslate.py "' + text + '" "' + language + '" ').toString().replace(/(\r\n|\n|\r)/gm, "");
}
if (global.basePathMacOS != undefined) exports.translate = translateMacOS;

const speechToText = (file="empty", language = "en") => {
    return child_process.execSync('python python/runnerSpeechToText.py "' + file + '" "' + language + '" ').toString().replace(/(\r\n|\n|\r)/gm, "");
}
exports.speechToText = speechToText;

const speechToTextMacOS = (file="empty", language = "en") => {
    return child_process.execSync('python3 ' + global.basePathMacOS + 'python/runnerSpeechToText.py "' + file + '" "' + language + '" ').toString().replace(/(\r\n|\n|\r)/gm, "");
}
if (global.basePathMacOS != undefined) exports.speechToText = speechToTextMacOS;

const textToSpeech = (input, language = "en") => {
    child_process.execSync('python python/runnerTestToSpeech.py "' + input + '" "' + language + '" ');
}
exports.textToSpeech = textToSpeech;

const textToSpeechMacOS = (input, language = "en") => {
    child_process.execSync('python3 ' + global.basePathMacOS + 'python/runnerTestToSpeech.py "' + input + '" "' + language + '" ');
}
if (global.basePathMacOS != undefined) exports.textToSpeech = textToSpeechMacOS;