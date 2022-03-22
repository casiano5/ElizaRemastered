import { createApp } from 'vue'
import App from './App.vue'
const pyConnector = require('../js/pyConnector');
const global = require('../js/globals');

pyConnector.loadEliza();

createApp(App).mount('#app')
