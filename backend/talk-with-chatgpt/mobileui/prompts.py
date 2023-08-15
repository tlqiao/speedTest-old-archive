from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITE_MOBILE_LOCATOR = """
I plan to write mobile ui auto test with {client_tool}, you help to write reasonable locator for {platform} base on mobile screen layout, follow LOCATOR TEMPLATE format when you write locator,write all locator together, do not write explanatory information.

===LOCATOR TEMPLATE===
locatorName = locator
===END OF LOCATOR TMMPLATE===

===MOBILE SCREEN LAYOUT===
{layout}
===END OF MOBILE SCREEN LAYOUT===
"""

template = "You are an mobile ui auto test expert,write reasonable locator base on screen layout."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_MOBILE_LOCATOR
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
mobileui_locator_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

WRITE_MOBILE_STEP_FUNCTION = """
Write test step function with {client_tool} base on test step description, use provide page locators,do not generate page locator by yourself.
===PAGE LOCATOR
{locators}
===END OF PAGE LOCATOR

===TEST STEP DESCRIPTION
{test_step_description}
===END OF TEST STEP DESCRIPTION
"""
template = "You are an mobile ui auto test expert,write test step function with {client_tool} base on page locators and test step description."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_MOBILE_STEP_FUNCTION
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
mobileui_step_function_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
