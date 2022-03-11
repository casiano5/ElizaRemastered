import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { dirname } from 'path';
const path = require('path');

//Develop on windows they said, itll be fun they said
let basePath = path.resolve(__dirname, "./dist");
if (process.platform === 'win32'){
  basePath = basePath.replace(/[A-Z](:)/g, '');
  basePath = basePath.replace(/\\/g, '/');
}


// https://vitejs.dev/config/
export default defineConfig({
  base: basePath,
  plugins: [vue()]
})
