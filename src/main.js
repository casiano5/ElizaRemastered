import { createApp } from 'vue'
import App from './App.vue'
const global = require('../js/globals');
global.readConfig();

createApp(App).mount('#app')
