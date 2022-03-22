<script setup>
</script>

<template>
    <div class="input-group input-group-sm">
        <span class="input-group-text" id='inputGroup-sizing-sm'>Message</span>
        <input type="text" class="form-control" v-model="message">
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
                console.log("Event Thrower: " + this.message);
                this.message="";
                this.$forceUpdate();
            }

        }
    },
}
</script>

<style scoped>
</style>