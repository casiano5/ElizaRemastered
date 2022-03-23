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

            }
        },
    }
</script>
