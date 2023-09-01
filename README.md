**项目包括backend和frontend两部分,frontend由js编写，backend目录包括talk-with-chatgpt,test-with-js,test-with-python**
* talk-with-chatgpt: 使用langchain和提示工程调用chatgpt接口生成测试用例和测试代码
* test-with-js:使用低代码平台的思路自动生成API接口测试代码，技术栈是js
* test-with-python:使用低代码平台的思路自动生成API接口测试代码，技术栈是python，还未完全弄完，in-progress中

**testdata目录是用于使用工具的测试数据**
others里面是一个接口的request body和response body，在生成接口测试、契约测试、mock server的mapping文件时，需要输入接口相关信息，可以使用这里的测试数据
