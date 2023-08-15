import fs from 'fs';

export function readJSONFile() {
    try {
        const jsonData = fs.readFileSync(getConfigFilePath(), 'utf-8');
        const data = JSON.parse(jsonData);
        return data;
    } catch (error) {
        console.error('Error reading JSON file:', error);
        return null;
    }
}

export function writeJSONFile( data) {
    try {
        const jsonData = JSON.stringify(data, null, 2);
        fs.writeFileSync(getConfigFilePath(), jsonData, 'utf-8');
        console.log('JSON file has been written successfully.');
    } catch (error) {
        console.error('Error writing JSON file:', error);
    }
}

function getConfigFilePath() {
    const env = process.env["env"] ? process.env["env"] : "dev";
    return './config/config_' + env + '.json'
}
