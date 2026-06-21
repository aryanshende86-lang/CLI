# AI- Powered Study Assistant CLI
A lightweight Command Line Interface (CLI) application built with Python and the Gemini API that generates structured study plans for any topic and allows interactive follow-up questions in a persistent chat loop.

# FEATURES
### a.Structured Study Plans: 
Enter a topic to get immediate, organized subtopics, recommended study order, and concise descriptions.

<img width="1015" height="663" alt="image" src="https://github.com/user-attachments/assets/4d77f9f7-7c9d-4560-b1f6-80779edf4b89" />

### b.Context-Aware Chat: 
Ask deep-dive follow-up questions about any part of the study plan.

<img width="998" height="853" alt="image" src="https://github.com/user-attachments/assets/bae1feea-48b1-4462-ba35-28b6bec26370" />

### c.Session Summary: 
Automatically logs and displays your session statistics upon typing exit or quit.

<img width="475" height="222" alt="image" src="https://github.com/user-attachments/assets/8aae5285-fa83-4a26-8cd7-6da4e6a98f2a" />


# PROMPT ENGINEER WRITEUP

### 1. What role did you assign in your system prompt, and why did you choose that framing?

I assigned the role of highly academic syllabus designer and personal tutor ,beacuse By combining an "academic syllabus designer" with a "personal tutor," the model is primed to deliver a highly organized, curriculum-based roadmap initially, while remaining equipped to provide supportive, digestible breakdowns during the subsequent interactive Q&A chat loop.

### ​2. What format did you specify for the study plan output, and how did you enforce it in the prompt? 

Specified Format: The prompt specifies an "important and concise study plan" that strictly avoids conversational filler. For subsequent doubts, it explicitly demands a "short explanation with comprehensive paragraph and bullet points."
​How it is enforced:
It is enforced using direct behavioral constraints and negative constraints within the SYSTEM_INSTRUCTION string (lines 17–18):
​Negative Constraint: "DO NOT use overly casual language or include unnecessary conversational filler."
​Direct Instruction: "keep your explanation short with comprehensive paragraph and bullet points."

### 3.What happens if you remove the system prompt entirely - how does the output change? 

​If the SYSTEM_INSTRUCTION is removed from the config object :
​Loss of Professional Structure: The model will lose its persona as a structured syllabus designer, likely yielding loose text blocks rather than a clean, step-by-step roadmap.
​Inclusion of Filler Text: The model will lapse into default conversational tendencies, generating standard introductory and concluding pleasantries (e.g., "Sure! I can help you learn that topic..."), which breaks the clean look of the CLI output headers.
​Unpredictable Length: Follow-up answers in the chat session will become longer and more verbose, ignoring the requirement to keep explanations short and structured cleanly with paragraphs and bullets.

# SETUP AND INSTALLATION

 Clone the repository
git clone https://github.com/aryanshende86-lang/AI- Powered Study Assistant CLI.git
cd your-repo-name

 Install dependencies 
pip install google-genai python-dotenv

 Environmental Configuration 
GEMINI_API_KEY=YOUR_ACTUAL_API_KEY_HERE

# RUN THE APPLICATION
python main.py

