<script setup>
    const global = require('../js/globals');
</script>

<template>
    <select @change="changeLanguage($event)" v-model="selectedLanguage">
        <option :value="propertyName" v-for="(value, propertyName) in global.config.naturalSoundingLanguages" v-bind:key="propertyName">{{value}}</option>
    </select>
</template>

<script>
    const global = require('../js/globals');
    export default {
        methods: {
            changeLanguage(event){
                global.config.language = event.target.value;
                global.writeConfig();
            }
        },
        created(){
            this.selectedLanguage = global.config.language;
        }
    }
</script>

