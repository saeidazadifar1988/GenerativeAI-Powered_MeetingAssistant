# GenerativeAI-Powered_MeetingAssistant


An AI-powered meeting assistant that automatically transcribes meeting audio and generates concise summaries, key discussion points, and action items.

The application combines **OpenAI Whisper** for speech-to-text transcription with **IBM watsonx.ai Foundation Models** for intelligent summarization, all wrapped inside an interactive **Gradio** web interface.

---

##  Features

-  Upload meeting audio files (.mp3)
-  Automatic speech-to-text transcription using OpenAI Whisper
-  AI-generated meeting summaries
-  Extraction of key discussion points
-  Identification of action items and decisions
-  Interactive web interface built with Gradio
-  Ready for deployment using IBM Code Engine

---

##  Project Architecture

```
                Audio File
                    │
                    ▼
        OpenAI Whisper (ASR)
                    │
                    ▼
          Meeting Transcript
                    │
                    ▼
         Prompt Template (LangChain)
                    │
                    ▼
 IBM watsonx.ai Foundation Model
      (Granite / Llama Models)
                    │
                    ▼
      Summary + Key Points + Actions
                    │
                    ▼
             Gradio Web Interface
```

---

##  Project Structure

```
Business-AI-Meeting-Companion/
│
├── speech_analyzer.py
├── requirements.txt
├── README.md
├── Dockerfile
└── assets/
```

---

##  Technologies Used

- Python 3.10
- Gradio
- OpenAI Whisper
- Hugging Face Transformers
- LangChain
- IBM watsonx.ai
- IBM Foundation Models
- Torch

---

##  Installation

Clone the repository

```bash
git clone https://github.com/your-username/business-ai-meeting-companion.git

cd business-ai-meeting-companion
```

Create a virtual environment

```bash
python -m venv my_env
```

Activate it

Linux / macOS

```bash
source my_env/bin/activate
```

Windows

```bash
my_env\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📸 Demo

Upload an audio recording of a meeting.

The application will:

1. Convert speech into text.
2. Generate a concise meeting summary.
3. Extract important discussion points.
4. Identify action items.

---

##  Example Output

### Summary

The meeting focused on project planning, timeline updates, and task allocation.

### Key Points

- Project milestones were reviewed.
- Budget constraints were discussed.
- Team responsibilities were assigned.

### Action Items

- Complete prototype by next Friday.
- Schedule follow-up meeting.
- Prepare budget report.

---

##  Future Improvements

- Support multiple languages
- Speaker diarization
- Real-time meeting transcription
- PDF meeting reports
- Chat with meeting transcript (RAG)
- Meeting history database

---

##  License

This project is intended for educational and research purposes.

---

##  Author

**Saeid Azadifar**

Data Scientist / ML, Gen AI Engineer, Postdoctoral Researcher  
University of Oulu

GitHub: https://github.com/saeidazadifar1988
LinkedIn: www.linkedin.com/in/saeidazadifar


---

##  Acknowledgements

- OpenAI Whisper
- IBM watsonx.ai
- Hugging Face
- LangChain
- Gradio