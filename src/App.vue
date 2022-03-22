<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import HelloWorld from './components/HelloWorld.vue'
import Message from './components/UserMessage.vue';
import ElizaMessage from './components/ElizaMessage.vue';
import InputBox from './components/InputBox.vue';
import UserMessage from './components/UserMessage.vue';
</script>

<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <div v-for="message in this.messages" :key="message.counter"> <!-- Loop through messages array defined in data(), key in this case just needs to be some unique id picked count, will incremement on send (see createNewSentMessage function) -->
    <UserMessage v-if="message.sender === 'user'" :msg="message.message"/> <!-- if the user sent it, make a SentMessage -->
    <ElizaMessage v-if="message.sender === 'eliza'" :msg="message.message"/> <!-- if eliza sent it, make a ElizaMessage, note that passing props by var requires : notation (see msg prop) -->
  </div>
  <InputBox @message-sent="createNewSentMessage"/>

</template>

<script>
export default {
  data() {
    return {
      messages: [], //This will contain objects with 3 vars, counter (message number), sender (user or eliza), and message (contains the actual string user sent)
      messageCount: 0
    }
  },
  methods: {
    createNewSentMessage(event){
      let newMessage = { //here you can see the structure of each element in the messages array
        counter: this.messageCount++, //need a key to loop (thats what :key="message.counter is doing in the div that loops through the array), this key increments the messageCount variable (works a lot like the count button in the vue template did)
        sender: "user", //who sent this (for this event, this is always the user)
        message: event.message //what did they send
      }
      console.log("Event Listener: " + "\n[counter] => " + newMessage.counter + "\n[sender] => " + newMessage.sender + "\n[message] => " + newMessage.message);
      this.messages.push(newMessage); //adds the message to the above defined messages array
      console.log("messages: " + this.messages);
      //implement a call to pyConnector.sendEliza() here
      //I will likely need to modify the event return for eliza (its currently in src/main.js in ElizaRemastered but its a document call right now, itll probably be replaced with a callback function implemented here)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
