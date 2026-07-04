import torch
import os
import gradio as gr

#from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub

from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

#######------------- WatsonX Credentials -------------####

my_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
}

#######------------- Model Parameters -------------####

params = {
    GenParams.MAX_NEW_TOKENS: 800,   # Maximum number of tokens the model can generate.
    GenParams.TEMPERATURE: 0.1,      # Lower temperature = more deterministic output.
}

#######------------- LLM -------------####

# Initialize IBM Granite model (updated model supported by WatsonX)

LLAMA2_model = Model(
    model_id="ibm/granite-4-h-small",
    credentials=my_credentials,
    params=params,
    project_id="skills-network",
)

# Create LangChain LLM wrapper

llm = WatsonxLLM(LLAMA2_model)

#######------------- Prompt Template -------------####

# Prompt template for Granite model

temp = """
You are an AI meeting assistant.

Read the following meeting transcript and produce:

1. A concise summary.
2. The key discussion points.
3. Any action items or decisions made.

Transcript:
{context}
"""

pt = PromptTemplate(
    input_variables=["context"],
    template=temp
)

prompt_to_LLAMA2 = LLMChain(
    llm=llm,
    prompt=pt
)

#######------------- Speech2Text -------------####

def transcript_audio(audio_file):

    # Initialize the speech recognition pipeline
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )

    # Transcribe the audio file
    transcript_txt = pipe(
        audio_file,
        batch_size=8
    )["text"]

    # Send transcript to WatsonX LLM
    result = prompt_to_LLAMA2.run(transcript_txt)

    return result

#######------------- Gradio UI -------------####

audio_input = gr.Audio(
    sources="upload",
    type="filepath",
    label="Upload Audio (.mp3)"
)

output_text = gr.Textbox(
    label="Meeting Summary",
    lines=20
)

# Create the Gradio interface

iface = gr.Interface(
    fn=transcript_audio,
    inputs=audio_input,
    outputs=output_text,
    title="Business AI Meeting Companion",
    description="Upload a meeting recording. Whisper transcribes the audio, and IBM Granite summarizes the meeting and extracts key points."
)

iface.launch(
    server_name="0.0.0.0",
    server_port=7860
)