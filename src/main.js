import { createApp } from 'vue'
import App from './App.vue'
const pyConnector = require('../js/pyConnector');
const global = require('../js/globals');

pyConnector.loadEliza();

//Event if Eliza Responds
global.elizaEvent = document.createElement("eliza-event");
global.elizaEvent.addEventListener('elizaResponded', (e) => {
    console.log(e.detail.response)
});

createApp(App).mount('#app')
