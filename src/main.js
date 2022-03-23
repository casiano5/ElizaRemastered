import { createApp } from 'vue'
import App from './App.vue'
const pyConnector = require('../js/pyConnector');
const global = require('../js/globals');
global.readConfig();

pyConnector.loadEliza();

createApp(App).mount('#app')
