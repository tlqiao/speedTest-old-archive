import {getBackendServerUrl} from "../config.js";
import axios from "axios";
import express from "express";
import Joi from "joi";

export const apiTestRouter = express.Router();
let backendUrl;
apiTestRouter.post('/api/generateApiCallCode', async(req, res) => {
    const requestBodySchema = Joi.object({
        apiInfo: Joi.object({
            apiName: Joi.string().required(),
            apiMethod: Joi.string().required(),
            apiUrl: Joi.string().required(),
            parameterizedFields: Joi.array().required(),
            apiRequestBody: Joi.object().required()
        }).required(),
        testType: Joi.string().valid('api').required(),
        language: Joi.string().required()
    });
    const {error} = requestBodySchema.validate(req.body);
    if (error) {
        return res.status(400).send({error: 'Invalid request'});
    }
    backendUrl = getBackendServerUrl(req.body.language);
    console.log(backendUrl)
    await axios.post(`${backendUrl}/generateApiCallCode`, req.body.apiInfo)
        .then(response => {
            return res.send(response.data)
        }).catch(error => {
            console.error('Error occurred:', error);
            return res.status(500).send({error: 'Internal Server Error'});
        }
    )
})
apiTestRouter.get('/api/sendTemplateFile', async (req, res) => {
    const {apiName, testType, language} = req.query
    if (!apiName || !testType || !language || apiName === "" || testType !== 'api' || language === "") {
        return res.status(400).send({error: 'Invalid request'});
    }
    backendUrl = getBackendServerUrl(language);
    return await axios
        .get(`${backendUrl}/sendTemplateFile`, {params: {apiName: apiName}})
        .then(response => {
            const filename = `${apiName}ReqTemplate.hbs`;
            res.setHeader('Content-Disposition', 'attachment; filename=' + filename);
            res.send(response.data)
        })
        .catch(error => {
            console.log('Error occurred:', error)
            res.status(500).send({error: 'Internal Server Error'});
        });
})
apiTestRouter.post('/api/generateCaseCode', async (req, res) => {
    const requestBodySchema = Joi.object({
        testType: Joi.string().valid('api').required(),
        language: Joi.string().required(),
        apiInfo: Joi.object({
            apiName: Joi.string().required(),
            parameterizedFields: Joi.array().required(),
        }).required(),
    });
    const {error} = requestBodySchema.validate(req.body);
    if (error) {
        return res.status(400).send({error: 'Invalid request'});
    }
    backendUrl = getBackendServerUrl(req.body.language);
    await axios.post(`${backendUrl}/generateCaseCode`, req.body.apiInfo)
        .then(response => {
            return res.send(response.data)
        }).catch(error => {
            console.error('Error occurred:', error);
            return res.status(500).send({error: 'Internal Server Error'});
        }
    )
});
apiTestRouter.get('/api/generateProject', async (req, res) => {
    const {projectName, type, language} = req.query;
    if (!projectName || !type || !language || projectName === "" || type === "" || language === "") {
        return res.status(400).send({error: 'Invalid request'});
    }
    backendUrl = getBackendServerUrl(language);
     return await axios
        .get(`${backendUrl}/generateProject`, {
            params: {projectName: projectName, type: type},
            responseType: 'arraybuffer'
        })
        .then(response => {
            const filename = `${projectName}.zip`
            res.setHeader('Content-Disposition', 'attachment; filename=' + filename);
            res.removeHeader('Content-Type')
            res.setHeader('Content-Type', 'application/zip');
            res.send(response.data)
        })
        .catch(error => {
            console.error('Error occurred:', error);
            res.status(500).send({error: 'Internal Server Error'});
        });
});
