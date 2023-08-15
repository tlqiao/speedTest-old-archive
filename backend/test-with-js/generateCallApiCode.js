import fs from 'fs';
import path, {dirname} from "path";
import {fileURLToPath} from "url";

async function deleteExistFile(filePath) {
    try {
        await fs.promises.access(filePath, fs.constants.F_OK);
        await fs.promises.unlink(filePath);
        console.log('Delete old template file successfully.');
    } catch (err) {
        if (err.code === 'ENOENT') {
            console.log('template file does not exist,do not delete it.');
        } else {
            console.error('Error deleting the file:', err);
        }
    }
}

async function generateHandlebarsTemplate(apiName, requestBody, parameterizeFields) {
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = dirname(__filename);
    const templateFileName = `${apiName}ReqTemplate.hbs`;
    const templateFilePath = path.resolve(__dirname, templateFileName);
    await deleteExistFile(templateFilePath);
    const templateContent = await generateTemplateContent(requestBody, parameterizeFields);
    await fs.promises.writeFile(templateFilePath, templateContent, 'utf8');
    return templateFileName;
}

async function generateTemplateContent(requestBody, parameterizeFields) {
    const convertToHandlebars = (obj) => {
        for (const key in obj) {
            if (obj.hasOwnProperty(key)) {
                if ((typeof obj[key] === 'object' && !Array.isArray(obj[key])) || (Array.isArray(obj[key]) && typeof obj[key][0] === 'object')) {
                    convertToHandlebars(obj[key]);
                } else if (parameterizeFields.includes(key)) {
                    if (Array.isArray(obj[key])) {
                        obj[key] = obj[key].map( item => `{{${key}}}`);
                    } else {
                        obj[key] = `{{${key}}}`;
                    }
                }
            }
        }
    };
    convertToHandlebars(requestBody);
    return JSON.stringify(requestBody, null, 2);
}

async function generateCompiledTemplateContent(parameterizeFields) {
    let content = '';
    parameterizeFields.forEach((field) => {
        const value = `${field} || 'default${field[0].toUpperCase() + field.slice(1)}'`;
        content = content + `${field}: ` + value + ',' + '\n';
    });
    content = content.substring(0, content.length - 2);
    return '{' + content + '}'

}

export async function generateApiCallCode(apiName, apiUrl, apiMethod, apiRequestBody, parameterizeFields) {
    const templateFileName = await generateHandlebarsTemplate(apiName, apiRequestBody, parameterizeFields);
    const compileContent = await generateCompiledTemplateContent(parameterizeFields);
    let generateContent = `
    import {callApiWithToken} from './client.js';
    import handlebars from "handlebars";
    import fs from 'fs';
    import { jsonrepair } from 'jsonrepair';
    import path  from 'path';
    import {fileURLToPath} from "url";
    
    export async function ${apiName}Call (${parameterizeFields}) {
    let requestBody='';
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
      try {
        const templateContent = await fs.promises.readFile(path.join(__dirname,'./reqFile/${templateFileName}'), 'utf8');
        const compiledTemplate = handlebars.compile(templateContent);
        const body = compiledTemplate(
        ${compileContent}
        );
        requestBody = jsonrepair(body);
    } catch (err) {
        console.error('Error compiling the template:', err);
    }
      let option = {
        method: "${apiMethod}",
        url: '${apiUrl}',
        body: requestBody
    }
    return await callApiWithToken(option);
    }
    `
    return generateContent
}

export async function sendTemplateFile(req,res) {
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = dirname(__filename);
    try {
        const apiName = req.query.apiName;
        if (!apiName) {
            return res.status(400).send('apiName parameter is missing');
        }
        const templateFileName = `${apiName}ReqTemplate.hbs`;
        const templateFilePath = path.resolve(__dirname, templateFileName);
        fs.access(templateFilePath, fs.constants.R_OK, (err) => {
            if (err) {
                console.error('Error accessing template file: ' + err);
                return res.status(404).send('Template file not found');
            }
            res.setHeader('Content-Disposition', `attachment;filename=${templateFileName}`);
            res.sendFile(templateFilePath, (err) => {
                if (err) {
                    console.error('Error sending template file: ' + err);
                }
                fs.unlinkSync(templateFilePath)
            });
        });
    } catch (err) {
        console.error('Error:', err);
        res.status(500).send('Internal server error');
    }
}
