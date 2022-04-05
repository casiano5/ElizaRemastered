<template>
  <div class="modal fade" ref="settingsModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Settings</h5>
          <button type="button" class="btn-close" @click="modal.hide()" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            This is where we would put individual settings that can be changed
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="modal.hide()">Close</button>
          <button type="button" class="btn btn-primary" @click="saveSettings">Save</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    import { Modal } from 'bootstrap';
    export default {
        data: () => ({
            modal: null
        }),
        mounted(){
            this.modal = new Modal(this.$refs.settingsModal)
        },
        methods: {
            showModal(){
                this.modal.show();
            },
            saveSettings(){
                //Save and reload eliconfig
            },
        }
    };
</script>