<script>
</script>

<template>
    <div class="form-check form-switch">
        <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" v-bind:checked="darkEnabled" @click="toggleDarkMode();">
        <label class="form-check-label" for="flexSwitchCheckDefault">Change Theme</label>
    </div>
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
                imagePath: require("../assets/LightbulbFill.svg"),
                darkEnabled: global.config.darkModeEnable,
            }
        }
    }
</script>

<style>
</style>