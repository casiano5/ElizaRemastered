<template>
    <p class="user-tag m-0 ps-3" style="text-align: right; padding-right: 4%;">User</p>
    <div class="user messages">
        <div class="message last" :class="mode" >
            {{msg}}
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            msg: String
        },
        data () {
            return {
                mode: require('../js/globals').config.darkModeEnable ? "dark1   " : ""
            }
        }
    }
</script>

<style scoped>
    body {
        font-family: helvetica;
        display: flex ;
        flex-direction: column;
        align-items: center;
    }

    .messages {
        margin-top: -5px;
        display: flex;
        flex-direction: column;
        margin-right: 3%;
    }

    .message {
        border-radius: 20px;
        padding: 8px 15px;
        margin-top: 5px;
        margin-bottom: 5px;
        display: inline-block;
    }


    .user {
        align-items: flex-end;
    }

    .user .message {
        color: #636c70;
        margin-left: 25%;
        background: #ffffff;
        background-attachment: fixed;
        position: relative;
    }
</style>
