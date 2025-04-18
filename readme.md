# Speech‑to‑Summary App

A simple web application that lets you speak, see the raw transcript in your browser, and get back a neat, structured summary powered by any LLM (OpenAI, Gemini, Claude, etc.).

---

## 📋 Table of Contents

1. [Features](#features)  
2. [High‑Level Architecture](#high‑level-architecture)  
3. [Live Demo](#live-demo)  
4. [Getting Started (Local Testing)](#getting-started-local-testing)  
5. [Usage](#usage)  

---

## Features

- **Client‑side transcription**  
  Uses your browser’s speech API to capture audio and produce a live transcript.  
- **Backend summarization**  
  Sends the transcript to a server that calls an LLM and returns a concise, structured summary.  
- **Markdown → HTML**  
  Renders the AI‑generated summary in the browser with a lightweight JS library.  
- **Side‑by‑side display**  
  Shows both the raw transcript and the formatted summary for easy comparison.  

---

## High‑Level Architecture

1. **Front‑End**  
   - Request mic permission  
   - Capture and transcribe speech in real time  
   - Send final transcript to the backend  
2. **Back‑End**  
   - Receive transcript payload  
   - Forward to chosen LLM provider with a “summarize this” prompt  
   - Return the output (usually Markdown)  
3. **Front‑End (continued)**  
   - Convert Markdown summary to HTML  
   - Update the UI with both transcript and summary  

---

## Live Demo

Try it out instantly—no setup required:  
🔗 https://audiotonotes.space

---

## Getting Started (Local Testing)

### Prerequisites

- **Python** (v3.8+)  
- **google-genai**  
- **flask**  
- (other packages listed in `requirements.txt`)  
- A modern browser that supports the Web Speech API  

### Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/RitikDutta/ai_engineer_pre_work.git
   cd speech‑to‑summary
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Note:** The `.env` file is already populated with the API key and tracked in this repo for testing purposes.

4. If u want to add .env yourself u can add .env file in root dir of project and add the variable 
    Gemini_api_key=<API_KEY>


### Running the App

1. **Start the back end**  
   ```bash
   python app.py
   ```

2. **Open** your browser at the Flask‑provided URL, grant mic access, and click **Record**.

---

## Usage

1. Click **Record**.  
2. Speak naturally into your mic (or paste/type a transcript).  
3. When you stop, the raw transcript appears instantly.  
4. A few seconds later, a clean, structured summary shows up next to it.  
5. Review, copy, or start another recording.  

---

## Documentation

These files are located in the `docs/` folder:

- [Requirements & Planning](docs/Requirements%20%26%20Planning.md) – Contains user stories and the overall project planning.  
- [High‑Level Design (HLD)](docs/HLD.pdf) – Outlines the major system components and their interactions.  
- [Low‑Level Design (LLD)](docs/LLD.pdf) – Details module-level designs, APIs, and data structures.  
- [Architecture Diagram](docs/Architecture.pdf) – Visual overview of the end-to-end application workflow.  
