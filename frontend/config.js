const config = {
    backendUrl: {
        testWithJsUrl: "http://localhost:9090/api/js",
        testWithPythonUrl: "http://localhost:9091/api/python",
        chatWithGPTServerUrl: "http://localhost:8090/chatWithGPT"
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


