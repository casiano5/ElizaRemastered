<script setup>
    import ElizaMessage from './ElizaMessage.vue';
    import UserMessage from './UserMessage.vue';
    import InputBox from './InputBox.vue';
    import { ref } from 'vue';
</script>

<template>
    <div v-for="message in messages" :key="message.counter">
        <UserMessage v-if="message.sender === 'user'" :msg="message.message"/>
        <ElizaMessage v-if="message.sender === 'eliza'" :msg="message.message"/>
    </div>
    <InputBox @message-sent="createNewSentMessage"/>
</template>

<script>
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
                //implement a call to pyConnector.sendEliza() here
            }
        }
    }
</script>
