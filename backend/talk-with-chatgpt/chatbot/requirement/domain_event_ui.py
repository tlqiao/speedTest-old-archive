import gradio as gr

from requirement.domain_event_chain import create_chain
from memories import ContextMemory


def generate_domain_event(business_context):
    context_memory = ContextMemory()
    with gr.Tab("Identify Domain Event"):
        with gr.Row():
            with gr.Column(scale=0.5):
                scenarios_chatbot = gr.Chatbot(
                    label="Assistant").style(height=600)
                message = gr.Textbox(label="Clarification")
            with gr.Column(scale=0.5):
                context = gr.Code(business_context, language="markdown", interactive=True, lines=29,
                                  label="Requirement Context")
                examples = gr.Button("Start")

        chain = create_chain(context_memory)

        def start(context: str):
            nonlocal chain
            chain.memory.clear()
            chain = create_chain(context_memory)
            context_memory.save_context(
                {'context': context}, {})
            response = chain.run('')
            return "", [("Let's clarify requirement,then generate domain event base requirement", response)]

        def chat(message: str, history):
            response = chain.run(message)
            history.append((message, response))
            return "", history

        examples.click(start, [context],
                       [message, scenarios_chatbot])
        message.submit(chat, [message, scenarios_chatbot], [
                       message, scenarios_chatbot])
    return context_memory
