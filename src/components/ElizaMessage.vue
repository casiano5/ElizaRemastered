<script setup>
    import { ref } from 'vue'

    defineProps({
        msg: String
    })
</script>

<template>
    <p class="eliza-tag fw-bold m-0 ps-3">Eliza</p>
    <div class="eli message">
        <div class="message last">
            ELIZA: {{msg}}
         </div>
    </div>
</template>

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
        margin-top: 5px;
        margin-bottom: 5px;
        display: inline-block;
    }

    .eli {
        align-items: flex-start;
    }

    .eli .message {
        margin-right: 25%;
        background-color: #eee;
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
        background: #eee;
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
        background: white;
        border-bottom-right-radius: 10px;
    }

    .eliza-tag{
        text-align: left;
        font-size: smaller;
    }
</style>
