<script setup>
    import ElizaMessage from './ElizaMessage.vue';
    import UserMessage from './UserMessage.vue';
    import InputBox from './InputBox.vue';
    import { ref } from 'vue';
</script>

<template>
<div id="all-messages" class="scrollable">
    <div v-for="message in messages" :key="message.counter">
        <UserMessage v-if="message.sender === 'user'" :msg="message.message"/>
        <ElizaMessage v-if="message.sender === 'eliza'" :msg="message.message"/>
    </div>
</div>
    
    <InputBox @message-sent="createNewSentMessage"/>
</template>

<script>
    const pyConnector = require("../js/pyConnector");
    const global = require("../js/globals");
    global.elizaEvent = document.createElement("eliza-event");
    global.elizaEvent.addEventListener('elizaResponded', (e) => {
        messages.value.push({
            counter: messageCount.value++,
            sender: "eliza",
            message: e.detail.response 
        });
    });
    const messageCount = ref(0);
    const messages = ref([]);
    export default {
        methods: {
            createNewSentMessage(event){
                messages.value.push({
                    counter: messageCount.value++,
                    sender: "user",
                    message: event.message 
                });
                pyConnector.sendEliza(event.message);              
            },
        }
    }
</script>

<style>

.scrollable {
                height: 100px;
                overflow-y: auto;
                text-align:justify;
                scroll-behavior: auto;
            }
</style>
