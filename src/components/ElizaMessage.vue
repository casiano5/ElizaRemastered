<template>
    <p class="eliza-tag m-0" style="padding-left: 4%;">Eliza</p>
    <div class="eli messages">
        <div class="message last" :class="mode">
            {{msg}}
        </div>
    </div>
</template>

<script>
    const global = require("../js/globals")
    export default {
        mounted(){
            if(global.config.textToSpeechEnable){
            setTimeout(() => {
                require('../js/pyConnector').textToSpeech(this.msg, require("../js/globals").config.language)
            }, 20)
            }
        },
        props: {
            msg: String
        },
        data (){
            return {
                mode: require('../js/globals').config.darkModeEnable ? "dark1": ""
            }
        }
    }
</script>


<style>
    body {
        font-family: helvetica;
        display: flex ;
        flex-direction: column;
        align-items: center;
    }

    .chat {
        width: 300px;
        border: solid 1px #EEE;
        display: flex;
        flex-direction: column;
        padding: 10px;
    }

    .messages {
        margin-top: 5px;
        display: flex;
        flex-direction: column;
        margin-left: 3%;
    }

    .message {
        border-radius: 20px;
        padding: 8px 15px;
        margin-top: -5px;
        margin-bottom: 5px;
        display: inline-block;
    }

    .eli {
        align-items: flex-start;
    }

    .eli .message {
        color: #e2e8f3;
        margin-right: 25%;
        background-color: #0d6efd;
        position: relative;
    }

    .eliza-tag{
        text-align: left;
    }
</style>
