from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITE_CONTRACT_TEST = """
===API DETAILS===
API URL: {api_url}
API METHOD: {api_method}
API REQUEST BODY: {api_request}
API RESPONSE:{api_response}
===END OF API DETAILS===

===MATCH RULE===
like
eachLike
atLeastOneLike
atLeastLike
atMostLike
boolean
integer
decimal	
number
string
timestamp
time
date
includes
===END OF MATCH RULE===
Write reasonable contract test base on api details with following format:

1.Analyze the API request body and response to determine the appropriate match rule to be used,do not use somethingLike,make sure only use above listed match rule.
2.Write consumer contract test with {test_tool}
3.Assump the contract file uploaded in pact-broker, write provider test, include pact-broker setting, provider baseUrl and so on.
"""
template = "You are an wiremock expert,wite contract test with {test_tool}"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_CONTRACT_TEST
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_contract_test_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
