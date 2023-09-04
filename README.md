**项目代码目录结构介绍**  

项目包括backend和frontend两部分,frontend由js编写,backend目录包括talk-with-chatgpt,test-with-js,test-with-python  

* talk-with-chatgpt: 使用langchain和提示工程调用chatgpt接口生成测试用例和测试代码
* test-with-js:使用低代码平台的思路自动生成API接口测试代码，技术栈是js
* test-with-python:使用低代码平台的思路自动生成API接口测试代码，技术栈是python，还未完全弄完，in-progress中

**testdata目录是用于使用工具的测试数据**  

testdata/others.txt里面是一个接口的request body和response body，在生成接口测试、契约测试、mock server的mapping文件时，需要输入接口相关信息，可以使用这里的测试数据


**本地启动应用**
* 拉取代码
* cd frontend, node ./app.js,frontend应用监听在3000端口
* cd test-with-js, node ./app.js, test-with-js应用监听在9090端口
* cd talk-with-chatgpt, python ./app.py, talk-with-chatgpt应用监听在8090端口


**Docker方式在本地部署**
***pull image***
* docker pull tlqiao/speedtest-backend-js:v0.3
* docker pull tlqiao/speedtest-frontend:v0.2
* docker pull tlqiao/speedtest-backend-chatgpt:v0.2

***创建自定义网络***
* 创建自定义网络，create network my-network

***启动backend-js后端服务**
* 启动backend-js后端服务，docker run --name backend-js-server -d -p 9090:9090 --network my-network tlqiao/speedtest-backend-js:v0.2
* check backend-js服务是否部署成功，curl http://localhost:9090/health-check

***启动backend-chatgpt后端服务***
* 启动backend-chatgpt后端服务,chatgpt中需要通过环境变量传入OPENAI_API_KEY，服务使用的是gpt3.5的api-key
* docker run --name backend-chatgpt-server -d -p 8090:8090 -e OPENAI_API_KEY=your openai api key --network my-network tlqiao/speedtest-backend-chatgpt:v0.2
* check backend-chatgpt服务是否部署成功，curl http://localhost:8090/health-check

***启动frontend服务***
* 启动frontend服务，在启动frontend服务时，通过环境变量方式，指定后端服务地址。 
* docker run --name frontend -d -p 3000:3000 -e BACKEND_SERVER=backend-js-server -e AICHAT_SERVER=backend-chatgpt-server --network my-network tlqiao/speedtest-frontend:v0.3
