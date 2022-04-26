from dotenv import load_dotenv
from random import choice
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()
session_prompt = "The following is a conversation with an AI assistant. \
      The assistant is helpful, creative, clever, and very friendly.\
          \n\nHuman: Hello, who are you?\
          \nTricky: I am an AI created by Tricky. How can I help you today?\
          \nUser: How much is twitter stock worth?\
          \nTricky: Twitter stock is currently worth $20.48 per share.\
          \nUser: What is the speed of light in a vacuum?\
          \nTricky: \
          \n\nThe speed of light in a vacuum is 186,282 miles per second.\
          \nUser: "

start_sequence = "\nTricky: "
restart_sequence = "\nUser: "


def ask(question, chat_log=None):
    """
    Ask a question to the user and return the response.

    Parameters:
    -----------
                question: str - The question to ask Tricky.
                chat_log: list - The chat log to append the question to.

    Returns:
    --------
                response: str - The response from Tricky.
    """
    prompt_text = f"{chat_log}{restart_sequence}: {question}{start_sequence}"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["User:", "Tricky:"]
    )

    story = response['choices'][0]['text']
    return str(story)


def append_to_chat_log(question, answer, chat_log=None):
    """
    Append a question and answer to the chat log.

    Parameters:
    -----------
                question: str - The question to append to the chat log.
                answer: str - The answer to append to the chat log.
                chat_log: list - The chat log to append the question and \
                    answer to.

    Returns:
    --------
                chat_log: list - The chat log with the question and answer \
                    appended.
    """
    if chat_log is None:
        chat_log = session_prompt

    return f"{chat_log}{restart_sequence}: {question}{start_sequence}{answer}"
