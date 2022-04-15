<script setup>
    const globals = require('../js/globals');
</script>

<template>
    <select @change="changeLanguage($event)" v-model="selectedLanguage">
        <option :value="propertyName" v-for="(value, propertyName) in globals.config.naturalSoundingLanguages" v-bind:key="propertyName">{{value}}</option>
    </select>
</template>

<script>
    const globalsLocal = require('../js/globals');
    export default {
        methods: {
            changeLanguage(event){
                globalsLocal.config.language = event.target.value;
                globalsLocal.writeConfig();
            }
        },
        created(){
            this.selectedLanguage = globalsLocal.config.language;
        }
    }
</script>

