import openai
import os
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from mobileui.prompts import mobileui_locator_prompt, mobileui_step_function_prompt

openai.api_key = os.environ.get("OPENAI_API_KEY")


def write_locator_for_mobile_ui(client_tool, platform, layout):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    write_case_chain = LLMChain(
        llm=chat, prompt=mobileui_locator_prompt, output_key="locators")
    locators = write_case_chain.run(
        client_tool=client_tool, platform=platform, layout=layout)
    return locators


def write_step_function_for_mobile_ui(client_tool, locators, step_desc):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    write_step_function_chain = LLMChain(
        llm=chat, prompt=write_step_function_for_mobile_ui, output_key="step_function")
    step_function = write_step_function_chain.run(
        client_tool=client_tool, locators=locators, test_step_description=step_desc)
    return step_function
