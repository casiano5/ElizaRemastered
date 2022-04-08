<script setup>
    import ChatWindow from './components/ChatWindow.vue'
    import SettingsButton from './components/SettingsButton.vue';
    import SettingsModal from './components/SettingsModal.vue';
    import DarkMode from './components/DarkMode.vue';
</script>

<template>
    <div id="app" :class="mode">
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
        margin-left: 0rem;
        width: 100%;
        height: 100vh;  
    }
    body{
        color: #35383e;
    }
    
    .light{
        background: #eceff1
    }
    .dark{
        background-color: #35383e !important;
        background: #35383e !important;
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

