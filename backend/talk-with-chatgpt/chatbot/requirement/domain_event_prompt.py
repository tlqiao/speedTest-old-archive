from langchain import PromptTemplate

DOMAIN_EVENT = """
You are a DDD expert who is familiar with identify domain event by example.  I'm business expert who is familar with requirment context.
===REQUIREMENT CONTEXT
{context}
===END OF REQUIREMENT CONTEXT

===EXAMPLE OF DOMAIN EVENT
Domain Event: Employee Assigned -> Requirement Rule Detail: The accumulated estimated workload for one person does not exceed 100%.
===END OF EXAMPLE OF DOMAIN EVENT

===DOMAIN EVENT
In software development, Domain-Driven Design (DDD), and Event-Driven Architecture, the term 'domain events' typically refers to representations of significant occurrences or state changes within a specific domain. Examples include 'order created,' 'payment completed,' 'user registered,' and so on. These events document changes in the domain's state and can be used to notify other components or modules for the purpose of updating data or performing other actions.
===END OF DOMAIN EVENT

Identify domain events, Use following format:

Thought: You should always think what is still uncertain about the requirement context. 
Question: the question to ask to clarify the requirement and details of the rules
Answer: the answer I responded to the question
... (this Thought/Question/Answer can repeat at least 3 times, at most 10 times)
Thought: I know enough to write all the domain events.
DomainEvent: List all possible domain event, follow the example of domain event.
{history}
{input}"""

CONVERSATION = """
You are a DDD expert who is familiar with identify domain event by example.  I'm business expert who is familar with requirment context.
===CONTEXT
{context}
===END OF CONTEXT
current conversations:
{history}
Human:{input}
AI:"""

domain_event_template = PromptTemplate(
    input_variables=["context", "history", "input"],
    template=DOMAIN_EVENT
)

conversation_template = PromptTemplate(
    input_variables=["context", "history", "input"],
    template=CONVERSATION
)
