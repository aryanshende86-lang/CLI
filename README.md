# AI- Powered Study Assistant CLI
A lightweight Command Line Interface (CLI) application built with Python and the Gemini API that generates structured study plans for any topic and allows interactive follow-up questions in a persistent chat loop.

# FEATURES
<b> a.Structured Study Plans: <b> Enter a topic to get immediate, organized subtopics, recommended study order, and concise descriptions.

<img width="1059" height="847" alt="image" src="https://github.com/user-attachments/assets/9242adb7-7216-4601-ac16-7e3e436bd958" />

<img width="1061" height="844" alt="image" src="https://github.com/user-attachments/assets/f9b5efaa-67e1-4fa7-a6c6-49f030377b55" />

<img width="1045" height="839" alt="image" src="https://github.com/user-attachments/assets/025a067c-1170-43b5-ba07-f4c00a9f72ce" />

<img width="1052" height="708" alt="image" src="https://github.com/user-attachments/assets/787cbd60-c0b3-4d0c-8539-16a94c6f8eb0" />

<b> b.Context-Aware Chat: <b> Ask deep-dive follow-up questions about any part of the study plan.


<b> c.Session Summary: <b> Automatically logs and displays your session statistics upon typing exit or quit.

# PROMPT ENGINEER WRITEUP

<b> 1. What role did you assign in your system prompt, and why did you choose that framing? <b>
I assigned the role of highly academic syllabus designer and personal tutor ,beacuse By combining an "academic syllabus designer" with a "personal tutor," the model is primed to deliver a highly organized, curriculum-based roadmap initially, while remaining equipped to provide supportive, digestible breakdowns during the subsequent interactive Q&A chat loop.

<b> ​2. What format did you specify for the study plan output, and how did you enforce it in the prompt? <b>
Specified Format:
The prompt specifies an "important and concise study plan" that strictly avoids conversational filler. For subsequent doubts, it explicitly demands a "short explanation with comprehensive paragraph and bullet points."
​How it is enforced:
It is enforced using direct behavioral constraints and negative constraints within the SYSTEM_INSTRUCTION string (lines 17–18):
​Negative Constraint: "DO NOT use overly casual language or include unnecessary conversational filler."
​Direct Instruction: "keep your explanation short with comprehensive paragraph and bullet points."

​<b> 3. What happens if you remove the system prompt entirely - how does the output change? <b>
​If the SYSTEM_INSTRUCTION is removed from the config object :
​<b>Loss of Professional Structure:<b> The model will lose its persona as a structured syllabus designer, likely yielding loose text blocks rather than a clean, step-by-step roadmap.
​<b>Inclusion of Filler Text:<b> The model will lapse into default conversational tendencies, generating standard introductory and concluding pleasantries (e.g., "Sure! I can help you learn that topic..."), which breaks the clean look of the CLI output headers.
​<b>Unpredictable Length:<b> Follow-up answers in the chat session will become longer and more verbose, ignoring the requirement to keep explanations short and structured cleanly with paragraphs and bullets.

# SETUP AND INSTALLATION

<b> Clone the repository <b>
git clone https://github.com/aryanshende86-lang/AI- Powered Study Assistant CLI.git
cd your-repo-name

<b> Install dependencies <b>
pip install google-genai python-dotenv

<b> Environmental Configuration <b>
GEMINI_API_KEY=YOUR_ACTUAL_API_KEY_HERE

# RUN THE APPLICATION
python main.py

