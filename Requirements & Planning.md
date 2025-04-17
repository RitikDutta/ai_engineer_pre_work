# Requirements

## Client Story
#### As a user i want to have an application that will be used to transcribe(converts my voice to text) my conversations, that could be meetings
#### After Transcription the application should summarize the conversations(transcriptions) in a nice an systematic way
### after the summerization i should see both raw transcriptions and summarized text
#### thers is a similar app availeble called NotePen.


# Brainstorming/Planning

#### simple description

-we need a application that take notes transcribe it and give summarize the text. 

things we can use 

## Framework Selection
### for the application we can use Flask, FastAPI, or Django
#### we will use flask for this application , as it has enough developer controls (which fast api lacks) and is not over overly complex unlike django , which may be a overkill for a simple app.

## Transcription
#### we can use whisper for that task , it is free and work in client side, with javascript
#### we are using browser based javascript speech to text library


## Summerization 
#### we can use gemini 2.5 here , as it is the best model out there which can take longer token size for the entire meeting of transcriptions and is also currently free.

## Frontend
#### we can use reactjs here but is not necessary for a small application but  we can shift to react anytime , for this project we can stick to html css and js we can use libraries like bootstrap , gsap(for animations), etc... 

## Backend 
#### here we will use python as backend which works best connecting with most of the LLMs and works great with Flask
