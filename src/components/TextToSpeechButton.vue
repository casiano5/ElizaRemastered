<script>
</script>

<template>
    <div class="form-check form-switch" >
        <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" v-bind:checked="TTSEnable" @click="toggleSpeechToText">
        <label class="form-check-label" for="flexSwitchCheckDefault">TTS</label>
    </div>
</template>

<script>
    const global = require('../js/globals')
    export default {
        methods: {
            toggleSpeechToText(){
                global.config.textToSpeechEnable = !global.config.textToSpeechEnable;
                global.writeConfig();
                if(this.imagePath === require("../assets/SpeakerOffIcon.svg")){
                    this.imagePath = require("../assets/SpeakerIcon.svg");
                }
                else{
                    this.imagePath = require("../assets/SpeakerOffIcon.svg");
                }
            }
        },
        data() {
            return{
                imagePath: require("../assets/SpeakerIcon.svg"),
                TTSEnable: global.config.textToSpeechEnable,
            }
        }
    }
</script>

<style>
</style>