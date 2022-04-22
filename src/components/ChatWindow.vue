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
    <div id="background-input">
        <InputBox id="input-box" @message-sent="createNewSentMessage" @show-settings-modal="showSettingsModal"/>
    </div>

</template>

<script>
    const pyConnector = require("../js/pyConnector");
    const global = require("../js/globals");

    pyConnector.loadEliza((response) => {
        messages.value.push({
            counter: messageCount.value++,
            sender: "eliza",
            message: global.config.language == "en" ? response : pyConnector.translate(response, global.config.language)
        });
    });

    const messageCount = ref(0);
    const messages = ref([]);
    
    export default {
        updated() {
            this.$nextTick(() => this.scrollToEnd());
        },
        methods: {
            showSettingsModal(){
                this.$emit("show-settings-modal");
            },
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
        height: 100%;
        width: 100%;
        overflow-y: auto;
        overflow-x: auto;
        text-align: left;
        scroll-behavior: auto;
        padding-bottom: 80px;
    }
    #background-input{
        background: inherit;
        width: 100%;
        padding: 1%;
        padding-top: 0;
        margin-top: 0;
        position: absolute;
        margin: 0;
        top: 100%;
        left: 50%;
        transform: translate(-50%, -100%);
    }
    #input-box{
        margin-top: 1.33%;
    }
</style>
