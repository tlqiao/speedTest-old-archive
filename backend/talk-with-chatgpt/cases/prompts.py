from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITECASES = """
You are a test expert, you need to write test case base requirement with test case design methods.

===TEST CASE DESIGN METHODS===
Boundary Value Analysis
Equivalence Partitioning
Cause-Effect Graphing
State Transition Testing
Decision Table Testing
Combinatorial Testing
Error Guessing
Random Testing
===END OF TEST CASE DESIGN METHODS===

===REQUIREMENTS===
{requirements}
===END OF REQUIREMENTS===

Write reasonable test cases, Use following format:

Thought: You should always think the requirements and analyze which test case design methods should be used to design the test cases. After confirming the test case design methods, you should evaluate whether the test cases are sufficient and cover both negative and positive scenarios.
Question: the question to ask to clarify the requirement and test case design method
Answer: the answer I responded to the question
... (this Thought/Question/Answer can repeat at least 3 times, at most 10 times)
Thought: I know enough to write all test cases

Tasks: write test cases with CASE NAME GIVEN/WHEN/THEN table format.
"""
template = "You are a test expert, you need to write test case base requirement with test case design methods."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITECASES
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

template_chinese = "你是一个测试专家,用中文编写基于需求的测试用例以及测试用例设计方法"
WRITECASES_CHINESE = """
你是一个测试专家，用中文编写基于需求的测试用例，并使用测试用例设计方法。

===测试用例设计方法===
边界值分析
等价类划分
因果图法
状态转换测试
决策表测试
组合测试
错误猜测
随机测试
===测试用例设计方法结束===

===需求===
{requirements}
===需求结束===

编写合理的测试用例，使用以下格式：

编写合理的测试用例，使用以下格式：

思路：你应该始终考虑需求并分析应该使用哪种测试用例设计方法来设计测试用例。在确认测试用例设计方法后，你应该评估测试用例是否足够并涵盖了正面和负面情况。
问题：用于澄清需求和测试用例设计方法的问题
回答：我对问题的回答
...（这种思路/问题/回答可以重复至少3次,最多10次)
思路：我已经掌握足够的信息来编写所有的测试用例

任务:使用CASE NAME GIVEN/WHEN/THEN表格格式编写测试用例.
"""
system_message_prompt = SystemMessagePromptTemplate.from_template(
    template_chinese)
human_template = WRITECASES_CHINESE
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt_chinese = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
