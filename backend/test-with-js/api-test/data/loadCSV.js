import fs from 'fs';
import csv from 'csv-parser';
import {createObjectCsvWriter} from 'csv-writer';

export async function readCSV(dataFileName, columnName = '', filterValue = '') {
    const env = process.env["env"] ? process.env["env"] : "dev";
    const filePath = './data/' + env + '/' + dataFileName
    try {
        return new Promise((resolve, reject) => {
            const results = [];
            const stream = fs.createReadStream(filePath).pipe(csv());
            stream.on('data', (row) => {
                if (!columnName || row[columnName] === filterValue) {
                    results.push(row);
                }
            });

            stream.on('end', () => resolve(results));
            stream.on('error', (error) => reject(error));
        });
    } catch (error) {
        console.log('Error:', error);
    }
}

export async function writeCSV(datafileName, data, isAppend) {
    const env = process.env["env"] ? process.env["env"] : "dev";
    const filePath = './data/' + env + '/' + datafileName
    try {
        const csvWriter = createObjectCsvWriter({
            path: filePath,
            header: Object.keys(data[0]).map((key) => ({id: key, title: key})),
            append: isAppend,
        });
        return csvWriter.writeRecords(data);
    } catch (error) {
        console.log('Error: ', error)
    }
}


