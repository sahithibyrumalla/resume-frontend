import gradio as gr
import requests
backend_url="http://localhost:8000/resume"

def resumerequest(skills):
    response = requests.post(backend_url,json={"skills": skills})
    if response.status_code == 200:
        return response.json()["resume"]
    else:
        return "Error connecting to backend."

demo = gr.Interface(fn=resumerequest,inputs=gr.Textbox(label="Enter Skills", lines=5),outputs=gr.Textbox(label="Generated Resume", lines=20))
demo.launch()