const sio = io();

sio.on('connect', ()=>{
    console.log("Connected");
});

sio.on('disconnect', ()=>{
    console.log("Disconnected");
});

