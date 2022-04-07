<script setup>
    import ChatWindow from './components/ChatWindow.vue'
    import SettingsButton from './components/SettingsButton.vue';
    import SettingsModal from './components/SettingsModal.vue';
</script>

<template>

    <SettingsButton @show-settings-modal="showSettingsModal"/>
    <ChatWindow/>
    <SettingsModal ref='settingsModal'/>
</template>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif; 
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 20px;
        margin-left: 3rem;
        width: 90%;
    }
    body{
        background:#eceff1 !important;
    }
</style>

<script>
    export default {
        methods: {
            showSettingsModal(){
                this.$refs.settingsModal.showModal();
            }
        }
    };
</script>

