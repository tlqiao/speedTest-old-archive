import request from "request";
import {readJSONFile} from "../config/loadConfig.js";
import handlebars from "handlebars";
import {readCSV} from "../data/loadCSV.js";

export async function callApi(option) {
    const configs = readJSONFile();
    if(option.url == null || !option.url) {
        console.log('Must input api url')
        return;
    }
    const options = {
        url:  configs.url + option.url,
        method: option.method ? option.method : 'GET',
        headers: option.headers ? {...configs.headers, ...option.headers}: configs.headers,
    };
    if ((option.method == "POST" || option.method=="PUT") && option.body !==null)
    {
        options.body=option.body;
    }
    try {
        return new Promise((resolve, reject) => {
            request(options, (error, response) => {
                if (error) {
                    console.error('API Error:', error);
                    reject(error);
                } else {
                    if (response.statusCode >= 200 && response.statusCode < 300) {
                        resolve(response);
                    } else {
                        console.log('API call failed:');
                        console.log('Request Url:', options.url);
                        console.log('Request method:', options.method);
                        console.log('Request header:', options.headers);
                        if(options.body) {
                            console.log('Request Body:', options.body);
                        }
                        console.log('Response Body:', response.body);
                        resolve(response);
                    }
                }
            });
        });
    } catch (error) {
        console.error('API Error:', error);
        return null;
    }
}
//get token from login api, replace to your system login api
async function getTokenFromLogin() {
    const template = '{"user":{"email":"{{email}}","password":"{{password}}"}}';
    const userData = await readCSV('login_user_data.csv','role','admin')
    const compiledTemplate = await handlebars.compile(template);
    const loginBody = compiledTemplate({
        email: userData[0].email || 'defaultEmail',
        password: userData[0].password || 'defaultPassword'
    });
    const option = {
        method: "POST",
        url: "/api/users/login",
        body: loginBody
    }
    const response = await callApi(option);
    const token = "Token " + JSON.parse(response.body).user.token;
    return token;
}
//example to call api with login token
export async function callApiWithToken(option) {
    option['headers']= {'Authorization': await getTokenFromLogin()}
    return await callApi(option)
}
