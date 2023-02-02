import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = ""




@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        autosar = request.form["autosar"]
        f = open("responses.txt", "a+")
        f.write(autosar+ '\n')
        f.close
        response = openai.Completion.create(model="text-davinci-003",prompt=generate_prompt(autosar),temperature=0.6,top_p=0.5, max_tokens=3500)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(autosar):
    return (autosar + " in AUTOSAR")