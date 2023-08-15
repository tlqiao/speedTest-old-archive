import openai
import os
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from mockserver.prompts import generate_mapping_file_prompt, generate_mapping_file_with_regex_prompt

openai.api_key = os.environ.get("OPENAI_API_KEY")


def write_mapping_file(is_use_regex, is_map_header, is_map_cookie, api_details):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    if is_use_regex:
        write_mapping_file_chain = LLMChain(
            llm=chat, prompt=generate_mapping_file_with_regex_prompt, output_key="mapping_file")
    else:
        write_mapping_file_chain = LLMChain(
            llm=chat, prompt=generate_mapping_file_prompt, output_key="mapping_file")

    mapping_file = write_mapping_file_chain.run(
        is_map_cookie=is_map_cookie, is_map_header=is_map_header, api_url=api_details.get("url"), api_method=api_details.get("method"), api_request=api_details.get("request"), api_response=api_details.get("response"))
    return mapping_file
