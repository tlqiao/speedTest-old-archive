import openai
import os
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from contract.prompts import generate_contract_test_prompt

openai.api_key = os.environ.get("OPENAI_API_KEY")


def write_contract_test(test_tool, api_details):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    write_contract_test_chain = LLMChain(
        llm=chat, prompt=generate_contract_test_prompt, output_key="contract_test")

    contract_test = write_contract_test_chain.run(
        test_tool=test_tool, api_url=api_details.get("url"), api_method=api_details.get("method"), api_request=api_details.get("request"), api_response=api_details.get("response"))
    return contract_test
