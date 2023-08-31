from typing import List, Tuple, Callable

from langchain.chains.base import Chain


class Conversation:
    def __init__(self, chain: Chain):
        self.chain = chain

    def __call__(self, message: str, history: List[Tuple[str, str]]):
        response = self.chain.run(input=message)
        history.append((message, response))
        return "", history


class TemplatedConversation:

    def __init__(self, chain: Chain, message: str, template: Callable):
        self.chain = chain
        self.template = template
        self.message = message

    def __call__(self, message: str, history: List[Tuple[str, str]], *args: str):
        response = self.chain.run(self.template(message, *args))
        history.append((self.message, response))
        return "", history
