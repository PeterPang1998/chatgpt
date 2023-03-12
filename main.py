#!/usr/bin/env python3 
import openai
from flask import Flask, request, render_template
# create the api key
openai.api_key = "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"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
def get_Chat_Response():
    userText = request.args.get("msg")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=userText,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )

    answer = response["choices"][0]["text"]
    return str(answer)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port="8400",debug=True)
