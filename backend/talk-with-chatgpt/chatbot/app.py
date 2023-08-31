import gradio as gr

from requirement.domain_event_ui import generate_domain_event

with open('chatbot/documents/project_management_system.md', 'r') as file:
    business_context = file.read()

with gr.Blocks() as ui:
    context_memory = generate_domain_event(business_context)

ui.launch(debug=True)
