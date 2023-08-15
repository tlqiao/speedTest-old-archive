import {createClient} from 'redis';
import {readJSONFile} from "../config/loadConfig.js";

const client = createClient(
    {
        url: getRedisUrl()
    }
);

client.on('error', err => console.log('Redis Client Error', err));

export async function readValue(key) {
    await client.connect();
    const value = await client.get(key);
    await client.disconnect();

}

export async function writeValue(key, value) {
    await client.connect();
    await client.set(key, value);
    await client.disconnect();
}

function getRedisUrl() {
    const configs = readJSONFile().redis
    const redisUrl = 'redis://' + configs.user + ':' + configs.password + '@' + configs.host + ':' + configs.port + '/' + configs.db;
    return redisUrl;
}

