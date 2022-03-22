<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import HelloWorld from './components/HelloWorld.vue'
import Message from './components/UserMesage.vue';
import ElizaMessage from './components/ElizaMessage.vue';
</script>

<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <Message msg="This is a test user message"/>
  <ElizaMessage msg="This is a message 'from Eliza'"/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
