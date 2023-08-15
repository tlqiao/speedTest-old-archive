import express from 'express';
import bodyParser from "body-parser";
import path from 'path';
import {fileURLToPath} from 'url';
import {apiTestRouter} from "./interface/apitest.js";
import {chatWithGPTRouter} from "./interface/chatWithGPT.js"

const app = express();
app.use(express.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static('static'));
app.use(apiTestRouter);
app.use(chatWithGPTRouter);

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
// Render the different pages
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/static/html/index.html');
});

app.get('/testcase', (req, res) => {
    res.sendFile(__dirname + '/static/html/testcase.html')
})

app.get('/api', (req, res) => {
    res.sendFile(__dirname + '/static/html/api.html');
});

app.get('/webui', (req, res) => {
    res.sendFile(__dirname + '/static/html/webui.html');
});

app.get('/mobileui', (req, res) => {
    res.sendFile(__dirname + '/static/html/mobileui.html');
});

app.get('/mockserver', (req, res) => {
    res.sendFile(__dirname + '/static/html/mockserver.html');
});

app.get('/contract', (req, res) => {
    res.sendFile(__dirname + '/static/html/contract.html');
});

app.get('/unit', (req, res) => {
    res.sendFile(__dirname + '/static/html/unit.html');
});

// Start the server
app.listen(3000, () => {
    console.log('Server running on port 3000');
});
