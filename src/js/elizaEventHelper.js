global.elizaEvent = document.createElement("eliza-event");
global.elizaEvent.addEventListener('elizaResponded', (e) => {
    console.log(e.detail.response)
});