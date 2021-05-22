const sio = io();

sio.on('connect', ()=>{
    console.log("Connected");
    sio.emit('sum', {numbers: [1, 2]}, (result)=>{
        console.log(result);
    });
});

sio.on('disconnect', ()=>{
    console.log("Disconnected");
});

sio.on('mult', (data, cb)=>{
    const result = data.numbers[0] * data.numbers[1];
    cb(result);
})