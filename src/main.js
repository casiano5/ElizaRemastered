import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css';

require('./js/globals').readConfig();
createApp(App).mount('#app')
