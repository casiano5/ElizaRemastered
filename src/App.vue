<script setup>
    import ChatWindow from './components/ChatWindow.vue'
    import NavBar from './components/NavBar.vue';
    import LanguageSelect from './components/LanguageSelect.vue';
    import BackgroundColor from './components/BackgroundColor.vue';
</script>

<template>
    <NavBar/>
    <BackgroundColor/>
    <LanguageSelect/>
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
    }
</style>
