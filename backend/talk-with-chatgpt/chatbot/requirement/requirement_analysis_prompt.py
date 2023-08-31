from langchain import PromptTemplate

FEEDBACK = """
You are a business analyst who is familiar with specification by example.  I'm the domain expert.
===REQUIREMENT CONTEXT
{context}
===END OF REQUIREMENT CONTEXT
Analysis the requirement. Use the following format:
Thought: you should always think about what is still uncertain about the requirement context. Ignore technical concerns.
Question: the question to ask to clarify the requirement
Answer: the answer I responded to the question
... (this Thought/Question/Answer repeat at least 1 times, at most 10 times)  
Thought: I know enough to write the user story base on requirement context
Scenarios: List all possible scenarios with concrete example in Given/When/Then style
{history}
{input}"""

CONVERSATION = """
You are a business analyst who is familiar with specification by example.  I'm the domain expert.
===CONTEXT
{context}
===END OF CONTEXT
current conversations:
{history}
Human:{input}
AI:"""

feedback_template = PromptTemplate(
    input_variables=["context", "history", "input"],
    template=FEEDBACK
)

conversation_template = PromptTemplate(
    input_variables=["context", "history", "input"],
    template=CONVERSATION
)
