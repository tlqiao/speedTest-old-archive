import openai
import os
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from webui.prompts import generate_locator_prompt, generate_step_function_prompt

openai.api_key = os.environ.get("OPENAI_API_KEY")


def write_locators_for_web_ui(test_tool, web_page):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    write_webui_locator_chain = LLMChain(
        llm=chat, prompt=generate_locator_prompt, output_key="web_page_locators")
    web_page_locators = write_webui_locator_chain.run(
        test_tool=test_tool, web_page=web_page)
    return web_page_locators


def write_step_function_for_web_ui(test_tool, locators, step_scenario):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    write_webui_function_chain = LLMChain(
        llm=chat, prompt=generate_step_function_prompt, output_key="web_step_function")
    web_step_function = write_webui_function_chain.run(
        test_tool=test_tool, page_locators=locators, test_step_description=step_scenario)
    return web_step_function
