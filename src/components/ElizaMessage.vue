<template>
    <p class="eliza-tag m-0 ps-3">Eliza</p>
    <div class="eli message">
        <div class="message last">
            {{msg}}
        </div>
    </div>
</template>

<script>
    export default {
        mounted(){
            setTimeout(() => {
                require('../js/pyConnector').textToSpeech("hello")
            }, 10);
        },
        props: {
            msg: String
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
        margin-top: 30px;
        display: flex;
        flex-direction: column;
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

    .eli .message.last:before {
        content: "";
        position: absolute;
        z-index: 0;
        bottom: 0;
        left: -7px;
        height: 20px;
        width: 20px;
        background: #0d6efd;
        border-bottom-right-radius: 15px;
    }

    .eli .message.last:after {
        content: "";
        position: absolute;
        z-index: 1;
        bottom: 0;
        left: -10px;
        width: 10px;
        height: 20px;
        background: #eceff1;
        border-bottom-right-radius: 10px;
    }

    .eliza-tag{
        text-align: left;
    }
</style>
