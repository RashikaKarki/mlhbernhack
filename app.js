const express = require('express');
const app = express();

const path = require('path');
const fs = require('fs');

app.use(express.static('static'));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send("HELLOW WORLD");
});
app.post('/processImage',async (req,res)=>{
    

    // let runPy = new Promise(function(success, nosuccess) {

    //     const img = req.files[0];
    //     const spawn = require('child_process').spawn;
    //     const pythonProcess = spawn('python',["preprocess.py",img]);
    //     pythonProcess.stdout.on('data', function(data) {
            
    //         success(data);
    //     });
    
    //     pythonProcess.stderr.on('data', (data) => {
    
    //         nosuccess(data);
    //     });
    // });
    
    // runPy.then((data)=>{
    //     result = JSON.parse(data.toString())
    //     res.json(result)
     
    // }
    // ).catch(err=>console.log(err));

   
    let img = req.body.img;
    res.json(img);
    
});


app.listen(3000, console.log("Server started!"));