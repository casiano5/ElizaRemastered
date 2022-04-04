<script setup>
</script>

<template>
    <nav class="vertical-nav bg-light" id="sidebar">  
        <button type="button" class="btn btn-primary" ><img src="../assets/setting.svg"></button>    
    </nav>
</template>

<style>
    .vertical-nav {
        min-width: 3rem;
        width: 3rem;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
        transition: all 0.4s;
    }
</style>