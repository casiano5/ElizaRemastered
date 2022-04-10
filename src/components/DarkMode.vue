<script>
</script>

<template>
    <button type="button" class="btn btn-primary" @click="toggleDarkMode">
        <img src="../assets/Lightbulb.svg">
    </button>
</template>

<script>
    const global = require('../js/globals')
    export default { 
        methods: {
            toggleDarkMode(){
                global.config.darkModeEnable = !global.config.darkModeEnable;
                global.writeConfig();
                this.$emit("change-theme");
            },
        }
    }
</script>

<style>
</style>