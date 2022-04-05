<script setup>
    import ChatWindow from './components/ChatWindow.vue'
    import NavBar from './components/NavBar.vue';
</script>

<template>
    <NavBar/>
    <ChatWindow/>
</template>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif; 
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
        width: 90%;
    }
    body{
        background:#eceff1 !important;
    }
</style>
