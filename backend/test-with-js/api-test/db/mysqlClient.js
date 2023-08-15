import mysql from 'mysql2';

const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: 'root123456',
    database: 'testdb',
    waitForConnections: true,
    connectionLimit: 10,
    maxIdle: 10,
    idleTimeout: 60000,
    queueLimit: 0,
    enableKeepAlive: true,
    keepAliveInitialDelay: 0
});

function executeQuery(query) {
    return new Promise((resolve, reject) => {
        pool.getConnection((err, connection) => {
            if (err) {
                console.error('Error getting database connection: ' + err);
                return reject(err);
            }
            connection.query(query, (err, rows) => {
                connection.release();
                if (err) {
                    console.error('Error executing query: ' + err);
                    return reject(err);
                }
                resolve(rows);
            });
        });
    });
}
async function getDataFromDatabaseExample() {
    try {
        const query = 'SELECT * FROM posts';
        const result = await executeQuery(query);
        return result;
    } catch (err) {
        console.error('Error executing query: ' + err);
        throw err;
    }
}
const result = await getDataFromDatabaseExample()
console.log(result[0].title)


