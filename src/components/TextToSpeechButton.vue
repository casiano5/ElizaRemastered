<script>
</script>

<template>
    <button type="button" class="btn btn-primary" @click="toggleSpeechToText">
        <img src="../assets/SpeakerIcon.svg">
    </button>
</template>


<script>
const global = require('../js/globals')
export default {
        methods: {
            toggleSpeechToText(){
                global.config.textToSpeechEnable = !global.config.textToSpeechEnable;
                global.writeConfig();
            }
        }
}
</script>
<style>
</style>