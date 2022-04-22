const child_process = require("child_process");
const path = require("path");
const global = require('./globals');

let eliza;

if (!global.config.pythonLibsInstalled) {
    //MacOS
    if (global.basePathMacOS != undefined){
        global.readConfig();
        child_process.exec("pip3 install -r " + path.join(global.basePathMacOS, "requirements.txt"));
        global.config.pythonLibsInstalled = true;
        global.writeConfig();
        console.log("I am installing the python stuff on MacOS")
    } 
    //Everyone Else
    else if (process.env.NODE_ENV === 'production'){
        global.readConfig();
        child_process.exec("pip install -r requirements.txt");
        global.config.pythonLibsInstalled = true;
        global.writeConfig();
        console.log("I am installing the python stuff on Windows")
    }
}

//Python files to function, default case (Windows, dev builds <npm run electron:serve>)
const loadEliza = (callback) => {
    eliza = child_process.spawn('python', ['-i', 'python/eliza.py']);
    eliza.stdout.on('data', (data) => {
        callback(data.toString().replace(/(\r\n|\n|\r)/gm, ""));
    });
    eliza.stderr.on('data', (data) => {
        console.error(data.toString().replace(/(\r\n|\n|\r)/gm, ""));
    })
}
exports.loadEliza = loadEliza;

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

const speechToText = (file="empty", language = "en") => {
    return child_process.execSync('python python/runnerSpeechToText.py "' + file + '" "' + language + '" ').toString().replace(/(\r\n|\n|\r)/gm, "");
}
exports.speechToText = speechToText;

const textToSpeech = (input, language = "en") => {
    child_process.execSync('python python/runnerTextToSpeech.py "' + input + '" "' + language + '" ');
}
exports.textToSpeech = textToSpeech;

//MacOS Production Functions
const loadElizaMacOS = (callback) => {
    eliza = child_process.spawn('python3', ['-i', "python/eliza.py"], {cwd: global.basePathMacOS});
    eliza.stdout.on('data', (data) => {
        callback(data.toString().replace(/(\r\n|\n|\r)/gm, ""));
    });
    eliza.stderr.on('data', (data) => {
        console.error(data.toString().replace(/(\r\n|\n|\r)/gm, ""));
    })
}
if (global.basePathMacOS != undefined) exports.loadEliza = loadElizaMacOS;

const translateMacOS = (text, language = "en") => {
    return child_process.execSync('python3 -X utf8 python/runnerTranslate.py "' + text + '" "' + language + '" ', {cwd: global.basePathMacOS}).toString().replace(/(\r\n|\n|\r)/gm, "");
}
if (global.basePathMacOS != undefined) exports.translate = translateMacOS;

const speechToTextMacOS = (file="empty", language = "en") => {
    return child_process.execSync('python3 python/runnerSpeechToText.py "' + file + '" "' + language + '" ', {cwd: global.basePathMacOS}).toString().replace(/(\r\n|\n|\r)/gm, "");
}
if (global.basePathMacOS != undefined) exports.speechToText = speechToTextMacOS;

const textToSpeechMacOS = (input, language = "en") => {
    child_process.execSync('python3 python/runnerTextToSpeech.py "' + input + '" "' + language + '" ', {cwd: global.basePathMacOS});
}
if (global.basePathMacOS != undefined) exports.textToSpeech = textToSpeechMacOS;