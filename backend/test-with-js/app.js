import express from 'express';
import {generateApiCallCode, sendTemplateFile} from './generateCallApiCode.js'
import bodyParser from "body-parser";
import {generateProject} from './createProject.js'
import {generateCaseCode} from "./generateCaseCode.js";

const app = express();
const port = 9090;
app.use(bodyParser.json());

// Endpoint to trigger the init project zip file download
app.get('/api/js/generateProject', (req, res) => {
    const type = req.query.type;
    const foldersToCopy = [];
    foldersToCopy[0]=`${type}`;
    return generateProject(req, res, foldersToCopy)
})

app.post('/api/js/generateApiCallCode', async (req, res) => {
    const {apiName, apiUrl, apiMethod, parameterizedFields, apiRequestBody} = req.body;
    const code = await generateApiCallCode(apiName, apiUrl, apiMethod, apiRequestBody, parameterizedFields)
    let result = {};
    result.code = code;
    res.send(result);
});

app.get('/api/js/sendTemplateFile', async (req, res) => {
    return await sendTemplateFile(req, res)
})

app.post('/api/js/generateCaseCode', async (req, res) => {
    const {apiName, parameterizedFields} = req.body;
    const code = await generateCaseCode(apiName, parameterizedFields);
    let result = {};
    result.code = code;
    res.send(result);
})

app.get('/health-check',()=> {
    return "Hello,this is test-with-js server"
})
// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
