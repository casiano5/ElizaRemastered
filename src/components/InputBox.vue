<script setup>
    import SettingsButton from './SettingsButton.vue';
</script>

<template>
    <div class="input-group input-group-sm">
        <SettingsButton @show-settings-modal="showSettingsModal"/>
        <button type="button" class="btn btn-primary" @click="toggleSpeechToText"><img src="../assets/mic.svg"></button>
        <input type="text" class="form-control" v-model="message" @keyup.enter="sendMessageToEliza">
        <button type="button" class="btn btn-primary" @click="sendMessageToEliza">Send</button>
    </div>
</template>

<script>
    const pyConnector = require('../js/pyConnector');
    const global = require('../js/globals.js');
    export default {
        methods: {
            showSettingsModal(){
                this.$emit("show-settings-modal");
            },
            sendMessageToEliza(){
                if (this.message != ""){
                    this.$emit('message-sent' ,{
                        message: this.message
                    });
                    this.message = "";
                    this.$forceUpdate();
                }

            },
            toggleSpeechToText(){
                if (this.message != undefined){
                    this.message = this.message + " " + pyConnector.speechToText(undefined, global.config.language);
                }
                else{
                    this.message = pyConnector.speechToText(undefined, global.config.language);
                }
                this.$forceUpdate();
            }
        },
    }
</script>

<style>
    button.btn.btn-primary {
        font-size: 1rem;
        padding: 0.375rem 0.75rem;
    }
    .input-group.input-group-sm {
        margin-left: 3%;
        width: 94%;
        margin-top: 2rem;
    }
</style>