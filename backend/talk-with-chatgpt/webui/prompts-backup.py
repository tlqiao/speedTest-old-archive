from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITE_WEB_LOCATOR = """
Write reasonable locator with {test_tool} for every element in the page base on web page body, follow LOCATOR TEMPLATE format, do not write explanatory information.

===LOCATOR METHOD
cy.get(selector)
cy.get(selector).contains(content)
cy.get(selector).eq(index)
cy.get(selector).filter(selector)
cy.get(selector).find(selector)
cy.get(selector).first()
cy.get(selector).first(selector)
cy.get(selector).last()
cy.get(selector).last(selector)
cy.get(selector).next(selector)
cy.get(selector).parent()
cy.get(selector).parent(selector)
cy.get(selector).slibings()
cy.get(selector).slibings(selector)
cy.get(selector).shadow()
cy.get(selector).shadow(shadow)
===END OF LOCATOR METHOD

===WEB PAGE BODY
{web_page}
===END OF WEB PAGE BODY

===LOCATOR TEMPLATE
locatorName = locator
===END OF LOCATOR TMMPLATE

Write reasonable web element locators, Use following format:

Thought: You should always analyze the web page to determine how many elements are unique and then analyze which locator method should be used to locate each page element.
Question: the question to ask to decide locator method
Answer: the answer I responded to the question
... (this Thought/Question/Answer can repeat N times)
Thought: I know enough to write all the element locators base on given web page body

Tasks: Write all the element locators based on the given web page body, following the locator template format. Please note that it is necessary to provide a locator for each element on the page.
"""
template = "You are an ui auto test expert,write reasonable locator with {test_tool} base on web page body."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_WEB_LOCATOR
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_locator_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

WRITE_WEB_STEP_FUNCTION = """
Write test step function with {test_tool} base on test step description, use provide page locators,do not generate page locator by yourself.
===PAGE LOCATOR
{page_locators}
===END OF PAGE LOCATOR

===TEST STEP DESCRIPTION
{test_step_description}
===END OF TEST STEP DESCRIPTION
"""
template = "You are an ui auto test expert,write test step function with {test_tool} base on page locators and test step description."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_WEB_STEP_FUNCTION
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_step_function_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
