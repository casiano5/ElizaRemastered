<template>
    <p class="user-tag m-0 ps-3" style="text-align: right; padding-right: 5px;">User</p>
    <div class="user messages">
        <div class="message last">
            {{msg}}
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            msg: String
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

    .user .message.last:before {
        content: "";
        position: absolute;
        z-index: 0;
        bottom: 0;
        right: -8px;
        height: 20px;
        width: 20px;
        background: white;
        background-attachment: fixed;
        border-bottom-left-radius: 15px;
    }

    .user .message.last:after {
        content: "";
        position: absolute;
        z-index: 1;
        bottom: 0;
        right: -10px;
        width: 10px;
        height: 20px;
        background: #eceff1;
        border-bottom-left-radius: 10px;
    }
</style>
