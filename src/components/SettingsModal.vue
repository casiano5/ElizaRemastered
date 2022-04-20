<template>
  <div class="modal fade" ref="settingsModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content" :class="mode">
        <div class="modal-header">
          <h5 style="color: black" class="modal-title">Settings</h5>
          <button type="button" class="btn-close" @click="modal.hide()" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div style="position: relative;">
            <div style="position: absolute; left: 20px; top 20px">
              <LanguageSelect></LanguageSelect>
            </div>
            <div style="position: absolute; left: 34%; color:black" >
              <DarkMode @change-theme="changeTheme"/>
            </div>
            <div style="position: absolute; left: 75%; color:black">
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
      changeTheme(){
        console.log("change from button");
        this.$emit("change-theme");
      }
    },
    components: { TextToSpeechButton, LanguageSelect, DarkMode }
  };
</script>