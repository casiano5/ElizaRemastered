<script setup>
    const global = require('../js/globals');
</script>

<template>
    <select>
        <option :value="propertyName" v-for="(value, propertyName) in global.config.naturalSoundingLanguages" v-bind:key="propertyName">{{value}}</option>
    </select>
</template>
