from crypt import methods
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from bot import ask, append_to_chat_log

app = Flask(__name__)

# Change secret key to something unique and secret
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route("/bot", methods=["POST"])
def tricky():
    """
    This is the main function of the bot.
    It will receive the message from the user,
    and send the response back to the user.
    """
    incoming_msg = request.values("Body")
    chat_log = session.get("chat_log")
    answer = ask(incoming_msg, chat_log)
    session["chat_log"] = append_to_chat_log(chat_log, incoming_msg, answer)

    msg = MessagingResponse()
    msg.message(answer)

    return str(msg)


if __name__ == "__main__":
    app.run(debug=True)
