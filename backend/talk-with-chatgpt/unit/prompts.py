from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITE_UNIT_TEST = """
Write unit test with {test_tool} base on SOURCR CODE,language is {language}, use {mock_tool} to mock the object, use {assert_tool} to assert.

===SOURCE CODE===
{source_code}
===END OF SOURCE CODE===
Write reasonable unit test with following format:

1: Analysis the code, use Boundary Value Analysis and Equivalence Partitioning to analysis which unit test case should be added, please note do not have repetition, redundancy, and omission.
2:Analysis the code, if  the source code is controller code, use spring @mockbean to mock object, otherwise, use @Mock and @InjectMock to mock the object.
3:Analysis the code, if the soruce code is controller code, use spring @WebMvcTest to add unit test for controller code.
4:If test_tool is junit5, use @ParameterizedTest and @ValueSource to write unit test.

Tasks: Write unit test on above thought.
"""


WRITE_INTEGRATION_TEST = """
Write integration test with {test_tool}  base on source code, language is {language}, use {mock_tool} to mock object, use {assert_tool} to assert.

===SOURCE CODE===
{source_code}
===END OF SOURCE CODE===
Write reasonable integration test with following format:

1: Analysis the code, use Boundary Value Analysis and Equivalence Partitioning to analysis which integration test case should be added, please note do not have repetition, redundancy, and omission.
2:Analysis the code, if the source code is controller code, use the Spring @SpringBootTest.
3:Analysis the code, if the source code is repository code, analysis the DB, if DB is mongo, use spring @DataMongoTest to add integration test for source code.
4:Analysis the code, if the source code is repository code, if use JPA, use spring @DataJpaTest to add integration test for source code.
5:Analysis the code, if the source code call third party api, use @RestClientTest to add integration test for source code.
6:If test_tool is junit5, use @ParameterizedTest and @ValueSource to write unit test.

Tasks: Write reasonable integration test base on above thought.
"""
template = "You are an {language} unit and integration test expert,wite unit test base on source code"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_UNIT_TEST
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_unit_test_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

human_template = WRITE_INTEGRATION_TEST
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_integration_test_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
