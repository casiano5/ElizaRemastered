
<template>
  <div class="modal fade" ref="settingsModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Settings</h5>
          <button type="button" class="btn-close" @click="modal.hide()" aria-label="Close"></button>
        </div>

        <div class="modal-body">
          <div style="position: relative;">
            <div style="position:absolute;left: 20px">
              <LanguageSelect></LanguageSelect>
            </div>
            <div style="position:absolute;left: 180px">
              <DarkMode></DarkMode>
            </div>
            <div style="position:absolute;left: 300px">
              <TextToSpeechButton></TextToSpeechButton>
            </div>
          </div>  

        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .modal-body {
    position: relative;
    flex: 1 1 auto;
    padding: 3rem;
}
.button.btn.btn-primary.a {
    padding: .375rem .6rem;
}
</style>

<script>
    import { Modal } from 'bootstrap';
    import TextToSpeechButton from "./TextToSpeechButton.vue";
    import LanguageSelect from "./LanguageSelect.vue";
    import DarkMode from "./DarkMode.vue";
    export default {
    data: () => ({
        modal: null
    }),
    mounted() {
        this.modal = new Modal(this.$refs.settingsModal);
    },
    methods: {
        showModal() {
            this.modal.show();
        },
        saveSettings() {
            //Save and reload eliconfig
        },
    },
    components: { TextToSpeechButton, LanguageSelect, DarkMode }
};
</script>