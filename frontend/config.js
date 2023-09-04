const backendServer = process.env.BACKEND_SERVER || 'localhost';
const aiServer = process.env.AICHAT_SERVER || 'localhost';
const config = {
    backendUrl: {
        testWithJsUrl: `http://${backendServer}:9090/api/js`,
        testWithPythonUrl: `http://${backendServer}:9091/api/python`,
        chatWithGPTServerUrl: `http://${aiServer}:8090/chatWithGPT`
    }
}

export function getBackendServerUrl(type) {
    const valueMap = {
        "javascript": config.backendUrl.testWithJsUrl,
        "python": config.backendUrl.testWithPythonUrl,
        "chatGPT": config.backendUrl.chatWithGPTServerUrl
    };
    return valueMap[type] || "Invalid input";
}


