import axios from "axios";
import express from "express";
import {getBackendServerUrl} from '../config.js'

export const chatWithGPTRouter = express.Router();
let backendUrl = getBackendServerUrl("chatGPT");

chatWithGPTRouter.post('/api/writeCase', async (req, res) => {
    if (!req.body || !req.body.requirements || req.body.requirements=== "") {
        return res.status(403).send({ error: 'Invalid request' });
    }
    try {
        const response = await axios.post(`${backendUrl}/writeCase`, req.body);
        return res.send(response.data);
    } catch (error) {
        console.error('Error occurred:', error);
        return res.status(500).send({ error: 'Internal Server Error' });
    }
});

chatWithGPTRouter.post('/api/writeWebLocator', (req, res) => {
    const {testTool,page} = req.body;
    if (!req.body || !testTool || !page || testTool==="" || page==="") {
        return res.status(403).send({ error: 'Invalid request' });
    }
    axios.post(`${backendUrl}/writeWebLocator`, req.body)
        .then(response => {
            return res.send(response.data)
        }).catch(error => {
        console.error('Error occurred:', error);
        return res.status(500).send({ error: 'Internal Server Error' });
        }
    )
})

chatWithGPTRouter.post('/api/writeWebStepFunction', (req, res) => {
    const {testTool,locators, stepDesc} = req.body;
    if (!req.body || !testTool || !locators || !stepDesc || testTool==="" || locators==="" || stepDesc ==="") {
        return res.status(403).send({ error: 'Invalid request' });
    }
    axios.post(`${backendUrl}/writeWebStepFunction`, req.body)
        .then(response => {
            return res.send(response.data)
        }).catch(error => {
        console.error('Error occurred:', error);
        return res.status(500).send({ error: 'Internal Server Error' });
        }
    )
})

chatWithGPTRouter.post('/api/writeMobileLocator', (req, res) => {
    const {clientTool,platform, layout} = req.body;
    if (!req.body || !clientTool || !platform || !layout || clientTool==="" || platform==="" || layout ==="") {
        return res.status(403).send({ error: 'Invalid request' });
    }
    axios.post(`${backendUrl}/writeMobileLocator`, req.body)
        .then(response => {
            return res.send(response.data)
        }).catch(error => {
        console.error('Error occurred:', error);
        return res.status(500).send({ error: 'Internal Server Error' });
        }
    )
})

chatWithGPTRouter.post('/api/writeMobileStepFunction', (req, res) => {
    const {clientTool,locators, stepDesc} = req.body;
    if (!req.body || !clientTool || !locators || !stepDesc || clientTool==="" || locators==="" || stepDesc ==="") {
        return res.status(403).send({ error: 'Invalid request' });
    }
    axios.post(`${backendUrl}/writeMobileStepFunction`, req.body)
        .then(response => {
            return res.send(response.data)
        }).catch(error => {
        console.error('Error occurred:', error);
        return res.status(500).send({ error: 'Internal Server Error' });
        }
    )
})

chatWithGPTRouter.post('/api/writeMappingFile', (req, res) => {
    const {isMapHeader,isMapCookie, isUseRegex,apiDetails} = req.body;
    if (!req.body || !apiDetails || isMapHeader==="" || isMapCookie==="" || isUseRegex ==="" || apiDetails ==="") {
        return res.status(403).send({ error: 'Invalid request' });
    }
    axios.post(`${backendUrl}/writeMappingFile`, req.body)
        .then(response => {
            return res.send(response.data)
        }).catch(error => {
            console.error('Error occurred:', error);
            return res.status(500).send({ error: 'Internal Server Error' });
        }
    )
})

chatWithGPTRouter.post('/api/generateContractTest', (req, res) => {
    const {testTool,apiDetails} = req.body;
    if (!req.body || !testTool || !apiDetails || testTool==="" || apiDetails ==="") {
        return res.status(403).send({ error: 'Invalid request' });
    }
    axios.post(`${backendUrl}/writeContractTest`, req.body)
        .then(response => {
            return res.send(response.data)
        }).catch(error => {
            console.error('Error occurred:', error);
            return res.status(500).send({ error: 'Internal Server Error' });
        }
    )
})

chatWithGPTRouter.post('/api/generateUnitTest', (req, res) => {
    const {testTool,language,mockTool,assertTool,testType,sourceCode} = req.body;
    if (testTool==="" || language ==="" || mockTool==="" || assertTool ==="" || testType==="" || sourceCode==="") {
        return res.status(403).send({ error: 'Invalid request' });
    }
    axios.post(`${backendUrl}/writeUnitTest`, req.body)
        .then(response => {
            return res.send(response.data)
        }).catch(error => {
            console.error('Error occurred:', error);
            return res.status(500).send({ error: 'Internal Server Error' });
        }
    )
})

