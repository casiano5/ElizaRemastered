<script setup>
</script>

<template>
        <button type="button" class="btn btn-secondary" @click="this.$emit('show-settings-modal')">
            <img src="../assets/setting.svg">
        </button>
</template>

<style>
    button.btn.btn-secondary {
        font-size: 1rem;
        padding: 0.375rem 0.75rem;
    }
</style>