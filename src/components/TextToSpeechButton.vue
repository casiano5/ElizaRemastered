<script>
</script>

<template>
    <button type="button" class="btn btn-primary" @click="toggleSpeechToText">
        <img :src = "imagePath">
    </button>
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
                imagePath: require("../assets/SpeakerIcon.svg")
            }
        }
}
</script>
<style>
</style>