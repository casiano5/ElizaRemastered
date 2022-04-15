<script>
</script>

<template>
    <button type="button" class="btn btn-primary" @click="toggleDarkMode();">
        <img :src = "imagePath">
    </button>
</template>

<script>
    const global = require('../js/globals')
    export default { 
        methods: {
            toggleDarkMode(){
                global.config.darkModeEnable = !global.config.darkModeEnable;
                global.writeConfig();
                if(this.imagePath === require("../assets/Lightbulb.svg")){
                    this.imagePath = require("../assets/LightbulbFill.svg");
                }
                else {
                    this.imagePath = require("../assets/Lightbulb.svg");
                }
                this.$emit("change-theme");
            },
        },
        data () {
            return {
                imagePath: require("../assets/LightbulbFill.svg")
            }
        }

    }
</script>

<style>
</style>