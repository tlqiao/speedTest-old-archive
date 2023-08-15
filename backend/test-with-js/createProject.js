import {fileURLToPath} from "url";
import fs from 'fs';
import archiver from 'archiver';
import {dirname} from 'path';
import path from 'path';

export function generateProject(req,res,foldersToCopy) {
    const {projectName} = req.query;
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = dirname(__filename);
    const templateName = projectName;
    const templatePath = path.join(__dirname, templateName);
    const zipFilePath = path.join(__dirname, `${templateName}.zip`);

    if (fs.existsSync(templatePath)) {
        fs.unlinkSync(templatePath)
    }
    fs.mkdirSync(templatePath);

    for (const folder of foldersToCopy) {
        const sourcePath = path.join(__dirname, folder);
        const targetPath = path.join(templatePath, folder);
        copyFolderRecursiveSync(sourcePath, targetPath);
    }
    const output = fs.createWriteStream(zipFilePath);
    const archive = archiver('zip', {
        zlib: {level: 9}
    });
    archive.pipe(output);
    archive.directory(templatePath, false); // Update the destination path
    archive.finalize();
    res.attachment(`${templateName}.zip`);
    output.on('close', () => {
        res.sendFile(zipFilePath, {}, (err) => {
            if (err) {
                console.error('Error sending zip file: ' + err);
            }
            deleteFolderRecursive(templatePath);
            fs.unlinkSync(zipFilePath);
        });
    });
};

function copyFolderRecursiveSync(source, target) {
    if (!fs.existsSync(target)) {
        fs.mkdirSync(target);
    }

    if (fs.lstatSync(source).isDirectory()) {
        const files = fs.readdirSync(source);
        files.forEach((file) => {
            const curSource = path.join(source, file);
            const curTarget = path.join(target, file);
            if (fs.lstatSync(curSource).isDirectory()) {
                copyFolderRecursiveSync(curSource, curTarget);
            } else {
                fs.copyFileSync(curSource, curTarget);
            }
        });
    }
}

// Function to delete folders recursively
function deleteFolderRecursive(folderPath) {
    if (fs.existsSync(folderPath)) {
        fs.readdirSync(folderPath).forEach((file) => {
            const curPath = path.join(folderPath, file);
            if (fs.lstatSync(curPath).isDirectory()) {
                deleteFolderRecursive(curPath);
            } else {
                fs.unlinkSync(curPath);
            }
        });
        fs.rmdirSync(folderPath);
    }
}
