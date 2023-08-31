from typing import Dict, Any, List

from langchain.memory.chat_memory import BaseChatMemory
from langchain.schema import BaseMemory

CONTEXT_MEMORY_KEYS = ['context',  'scenarios', ]


class ContextMemory(BaseMemory):
    memories: Dict[str, Any] = dict()

    @property
    def memory_variables(self) -> List[str]:
        return CONTEXT_MEMORY_KEYS

    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        return self.memories

    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        self.memories.update(
            {k: v for k, v in inputs.items() if k in CONTEXT_MEMORY_KEYS and k in inputs})

    def clear(self) -> None:
        self.memories.clear()


class MemoryView(BaseMemory):
    memory: BaseMemory
    variables: List[str] = []

    @property
    def memory_variables(self) -> List[str]:
        return [x for x in self.variables if x in self.memory.memory_variables]

    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        variables = self.memory.load_memory_variables(inputs)
        return {k: v for k, v in variables.items() if k in self.variables}

    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        self.memory.save_context(inputs, outputs)

    def clear(self) -> None:
        self.memory.clear()


class HumanFeedbackBufferMemory(BaseChatMemory):
    memory_key: str = "history"

    @property
    def buffer(self) -> Any:
        if self.return_messages:
            return self.chat_memory.messages
        else:
            string_messages = list(
                map(lambda m: f"{m.content}", self.chat_memory.messages))
            return "\n".join(string_messages)

    @property
    def memory_variables(self) -> List[str]:
        return [self.memory_key]

    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return {self.memory_key: self.buffer}
