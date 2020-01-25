const express = require('express');


const app = express();

const cors = require('cors');
// import {PythonShell} from 'python-shell';

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

app.post('/preprocessImage', async (req, res) => {

    let image = req.body;
    console.log(req.body)
    // image = JSON.parse(image);
    let s = image.image;
    s = s.substring(23)

    var json = JSON.stringify({'image':s});
    console.log(json)
    fs.writeFile('myjsonfile.json', json, 'utf8', () => {
        let result = ''
        const spawn = require('child_process').spawn;
        const pythonProcess = spawn('python', ["preprocess.py"]);
        pythonProcess.stdout.on('data', function (data) {
            try {
                result += data.toString()
            } catch (error) {
                console.log("ERROR:" + error);

            }
        });

        pythonProcess.stderr.on('data', (data) => {

            console.log('Errorrrr: '+ data)
        });
        pythonProcess.stdout.on('end', () => {
            try {
                // If JSON handle the data
                res.json(JSON.parse(result));
            } catch (e) {
                // Otherwise treat as a log entry
                res.json({result: 'Errrorr'});
            }
        });


    });

    // let options = {
    //     mode: 'json',
    //     pythonPath: 'python',
    //     pythonOptions: ['-u'], // get print results in real-time
    //     scriptPath: './',
    //     args: [image]
    //   };

    //   PythonShell.run('test.py', options, function (err, results) {
    //     if (err) throw err;
    //     // results is an array consisting of messages collected during execution
    //     console.log('results: %j', results);
    //   });


    // runPy.then((data) => {
    //     // result = JSON.parse(data.toString())
    //     // res.json(result)
    //     console.log("DATA:" + data.toString())
    // }
    // ).catch(err => console.log("ERROR" + err));



});



app.listen(3000, console.log("Server started!"));

