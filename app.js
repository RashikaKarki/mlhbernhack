const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors());
app.options('*', cors());

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

    console.log(req.body);
    // let img = req.body.img;
    // res.json(img);
    res.send().status(200);
    
});


app.listen(3000, console.log("Server started!"));