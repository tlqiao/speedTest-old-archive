import {callApiWithToken} from '../client.js';
import handlebars from "handlebars";

export async function getArticle() {
    let option = {
        method: "GET",
        url: '/api/get/articles'
    }
    return await callApiWithToken(option)
}

export async function addArticle(title) {
    const template = '{\n' +
        '    "article": {\n' +
        '    "tagList": [],\n' +
        '        "title": "{{title}}",\n' +
        '        "description": "test summary",\n' +
        '        "body": "this is a test article"\n' +
        '}\n' +
        '}'
    const compiledTemplate = handlebars.compile(template);
    const requestBody = compiledTemplate({
        title: title || 'defaultTitle'
    })
    let option = {
        method: "POST",
        url: '/api/articles',
        body: requestBody
    }
    return await callApiWithToken(option)
}



