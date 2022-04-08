<script setup>
</script>

<template>
    <div class="input-group input-group-sm">
        <button type="button" class="btn btn-primary" @click="toggleSpeechToText"><img src="../assets/mic.svg"></button>
        <input type="text" class="form-control" v-model="message" @keyup.enter="sendMessageToEliza">
        <button type="button" class="btn btn-primary" @click="sendMessageToEliza">Send</button>
    </div>
</template>

<script>
    const pyConnector = require('../js/pyConnector')
    export default {
        methods: {
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
                    this.message = this.message + " " + pyConnector.speechToText(undefined, "en");
                }
                else{
                    this.message = pyConnector.speechToText(undefined, "en");
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
</style>