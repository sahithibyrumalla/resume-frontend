import gradio as gr
import requests

backend_url = "https://resume-2-yn01.onrender.com/resume"

def resumerequest(skills):
    response = requests.post(
        backend_url,
        json={"skills": skills}
    )

    if response.status_code == 200:
        return response.json()["resume"]
    else:
        return f"Error {response.status_code}: {response.text}"

demo = gr.Interface(
    fn=resumerequest,
    inputs=gr.Textbox(label="Enter Skills", lines=5),
    outputs=gr.Textbox(label="Generated Resume", lines=20),
    title="AI Resume Generator"
)

demo.launch()
