import {callApi} from '../client.js';
import handlebars from 'handlebars';

export async function login(email, password) {
    const template = '{"user":{"email":"{{email}}","password":"{{password}}"}}';
    const compiledTemplate = handlebars.compile(template);
    const requestBody = compiledTemplate({
        email: email || 'defaultEmail',
        password: password || 'defaultPassword'
    });
    let option = {
        method: "POST",
        url: "/api/users/login",
        body: requestBody
    }
    const response = await callApi(option)
    return response

}
