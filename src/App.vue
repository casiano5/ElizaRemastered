<script setup>
    import ChatWindow from './components/ChatWindow.vue'
    import SettingsButton from './components/SettingsButton.vue';
    import SettingsModal from './components/SettingsModal.vue';
    import DarkMode from './components/DarkMode.vue';
</script>

<template>
    <div class="app" :class="mode">
        <DarkMode @change-theme=changeTheme></DarkMode>
        <SettingsButton @show-settings-modal="showSettingsModal" @change-theme="changeTheme"/>
        <ChatWindow/>
        <SettingsModal ref='settingsModal'/>
    </div>
</template>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif; 
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-left: 0rem;
        width: 100%;
        height: 100vh;
        background-color: #15202B;
    }
    body{
        /*background:#eceff1 !important;*/
        color: #15202B;
    }
    
    .light{
        background: #eceff1
    }
    .dark{
        background: #15202B !important;
        background-color: #15202B !important;
        color:#eceff1;
    }
</style>

<script>
    export default {
        methods: {
            showSettingsModal(){
                this.$refs.settingsModal.showModal();
            },
            changeTheme(){
                if(this.mode==="dark"){
                    this.mode="light";
                }
                else{
                    this.mode="dark";
                }
            }
        },
        data () {
            return {
                mode: require('./js/globals').config.darkModeEnable ? "dark" : "light"
            }
        }
    };
</script>

