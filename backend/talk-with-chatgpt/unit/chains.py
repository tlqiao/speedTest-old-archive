import openai
import os
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from unit.prompts import generate_unit_test_prompt, generate_integration_test_prompt

openai.api_key = os.environ.get("OPENAI_API_KEY")


def write_unit_test(test_tool, language, mock_tool, test_type, assert_tool, source_code):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    if test_type == "unit_test":
        write_unit_test_chain = LLMChain(
            llm=chat, prompt=generate_unit_test_prompt, output_key="unit_test")
    else:
        write_unit_test_chain = LLMChain(
            llm=chat, prompt=generate_integration_test_prompt, output_key="unit_test")

    unit_test = write_unit_test_chain.run(
        test_tool=test_tool, language=language, mock_tool=mock_tool, assert_tool=assert_tool, source_code=source_code)
    return unit_test
