import openai
import os
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from cases.prompts import chat_prompt, chat_prompt_chinese

openai.api_key = os.environ.get("OPENAI_API_KEY")


def write_test_case(language, requirements):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    if language == "Chinese":
        write_case_chain = LLMChain(
            llm=chat, prompt=chat_prompt_chinese, output_key="cases")
    else:
        write_case_chain = LLMChain(
            llm=chat, prompt=chat_prompt, output_key="cases")
    answer = write_case_chain.run(requirements=requirements)
    return answer
