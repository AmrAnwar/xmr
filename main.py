from flask import Flask
from transformers import pipeline
from flask import request

app = Flask(__name__)

# from transformers import pipeline

def xmr():
    xmr = pipeline('text-generation', model='./Xmr', tokenizer="dbmdz/german-gpt2")
    return xmr


def generate(model, start_str: str):
    result = model(start_str, max_length=100)[0]['generated_text']
    print("result:", result)
    return result

xmr_obj = xmr()


@app.route('/')
def hello_world():
    start_str = request.args.get('start_string', default = "", type = str)
    return generate(xmr_obj, start_str)

if __name__ == "__main__":
    app.run(host='0.0.0.0')