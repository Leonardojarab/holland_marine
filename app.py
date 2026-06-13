"""Gradio interface for HMAS — Holland Marine Assistant System.

Thin UI layer: all the logic lives in the `implementation` package
(config, ingest, answer). If the vector store does not exist yet, it is built
automatically on startup.
"""

import base64
from pathlib import Path

import gradio as gr

from implementation import ingest
from implementation.answer import answer_question
from implementation.config import COMPANY_NAME, DB_PATH

_LOGO = Path(__file__).parent / "hms.jpg"


def respond(message: str, history: list) -> tuple[str, list]:
    if not message.strip():
        return "", history
    reply = answer_question(message, history)
    history = history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": reply},
    ]
    return "", history


def build_ui() -> gr.Blocks:
    with gr.Blocks(title=f"{COMPANY_NAME} — HMAS") as demo:
        with gr.Row():
            with gr.Column(scale=1, min_width=200):
                if _LOGO.exists():
                    _logo_b64 = base64.b64encode(_LOGO.read_bytes()).decode()
                    gr.HTML(
                        f'<div style="display:flex;flex-direction:column;align-items:center;'
                        f'justify-content:center;height:100%;padding:16px;gap:12px;">'
                        f'<img src="data:image/jpeg;base64,{_logo_b64}" '
                        f'style="width:180px;height:180px;border-radius:50%;'
                        f'object-fit:cover;border:3px solid #e0e0e0;">'
                        f'<span style="font-weight:700;font-size:1.1rem;text-align:center;">{COMPANY_NAME}</span>'
                        f"</div>"
                    )
                else:
                    gr.Markdown(f"### {COMPANY_NAME}\n**HMAS**\nAssistant System")

            with gr.Column(scale=4):
                gr.Markdown(
                    "### HMAS — Holland Marine Assistant System\n"
                    "Technical assistant for marine vessel systems and equipment."
                )
                chat = gr.Chatbot(height=500, label="HMAS")
                msg = gr.Textbox(
                    placeholder="e.g. How do I configure the basic network layout on the Operator Work Station?",
                    label="Ask a technical question",
                    lines=2,
                )
                with gr.Row():
                    send = gr.Button("Send", variant="primary")
                    clear = gr.Button("Clear")

        send.click(respond, inputs=[msg, chat], outputs=[msg, chat])
        msg.submit(respond, inputs=[msg, chat], outputs=[msg, chat])
        clear.click(lambda: ([], ""), outputs=[chat, msg])

    return demo


if __name__ == "__main__":
    if not DB_PATH.exists():
        print("[app] No vector store; running initial ingestion...")
        ingest.main()
    build_ui().launch(theme=gr.themes.Soft(), share=True)
