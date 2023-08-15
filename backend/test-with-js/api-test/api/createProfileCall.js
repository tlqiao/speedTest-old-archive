
import {callApiWithToken} from './client.js';
import handlebars from "handlebars";
import fs from 'fs';
import { jsonrepair } from 'jsonrepair';
import path  from 'path';
import {fileURLToPath} from "url";

export async function createProfileCall (fullName) {
    let requestBody='';
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    try {
        const templateContent = await fs.promises.readFile(path.join(__dirname,'./reqFile/createProfileReqTemplate.hbs'), 'utf8');
        const compiledTemplate = handlebars.compile(templateContent);
        const body = compiledTemplate(
            {fullName: fullName || 'defaultFullName'}
        );
        requestBody = jsonrepair(body);
    } catch (err) {
        console.error('Error compiling the template:', err);
    }
    let option = {
        method: "POST",
        url: '/api/create/profile',
        body: requestBody
    }
    return await callApiWithToken(option);
}
