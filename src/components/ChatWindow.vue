<script setup>
    import ElizaMessage from './ElizaMessage.vue';
    import UserMessage from './UserMessage.vue';
    import InputBox from './InputBox.vue';
    import LanguageSelect from './LanguageSelect.vue';
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
    <LanguageSelect></LanguageSelect>

</template>

<script>
    const pyConnector = require("../js/pyConnector");
    const global = require("../js/globals");
    global.elizaEvent = document.createElement("eliza-event");
    global.elizaEvent.addEventListener('elizaResponded', (e) => {
        messages.value.push({
            counter: messageCount.value++,
            sender: "eliza",
            message: global.config.language == "en" ? e.detail.response : pyConnector.translate(e.detail.response, global.config.language)
        });
    });
    const messageCount = ref(0);
    const messages = ref([]);
    export default {
        updated() {
            this.$nextTick(() => this.scrollToEnd());
        },
        methods: {
            createNewSentMessage(event){
                messages.value.push({
                    counter: messageCount.value++,
                    sender: "user",
                    message: event.message,
                });

                pyConnector.sendEliza(global.config.language == "en" ? event.message : pyConnector.translate(event.message, "en"));              
            },
            scrollToEnd(){
                document.getElementById('all-messages').scrollTo(0, Number.MAX_SAFE_INTEGER);
            }
        }
    }
</script>

<style>
    .scrollable {
        height: 65vh;
        width: 20rem;
        overflow-y: auto;
        overflow-x: auto;
        text-align: left;
        scroll-behavior: auto;
    }
</style>
