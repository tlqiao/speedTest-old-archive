import { Client } from 'pg'
import {readJSONFile} from "../config/loadConfig.js";

const configs = readJSONFile().postgresql;
const client = new Client({
    user: configs.user,
    password: configs.password,
    host: configs.host,
    database: configs.database,
    port: configs.port
});

async function queryDataFromPostgreSQL(query) {
    try {
        await client.connect();
        const result = await client.query(query);
        return result.rows;
    } catch (err) {
        console.error('Error querying data from PostgreSQL: ' + err);
        throw err;
    } finally {
        await client.end();
    }
}

// Example usage
async function getDataFromPostgreSQL() {
    try {
        const query = 'SELECT * FROM your_table';
        const result = await queryDataFromPostgreSQL(query);
        console.log('Query result:', result);
        return result;
    } catch (err) {
        console.error('Error getting query data from PostgreSQL: ' + err);
    }
}
await getDataFromPostgreSQL();
