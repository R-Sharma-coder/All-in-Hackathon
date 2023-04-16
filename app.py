from flask import Flask,render_template, request
import openai
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
api_key = "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" # Open AI key for sylabbus extraction.
openai.api_key = api_key
model_id = 'gpt-3.5-turbo'
csv_file_name = 'output.csv'
url_text_main = None
content_main = None
def chat_gpt_conversation(conversation):
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = conversation
    )
    api_usage = response['usage']
    print(f'Total Tokens consumed :{api_usage["total_tokens"]}')
    # print(f'Response from model.role :{response.choices[-1].message.role}')
    # print(f'Response content from gpt: {response.choices[-1].message.content}')
    #stop means complete
    # print(response['choices'][0].finish_reason)
    # print(response['choices'][0].index)
    conversation.append({'role':response.choices[0].message.role,'content':response.choices[0].message.content})
    return conversation


app = Flask(__name__)
@app.route("/")

def home():
    return render_template("homepage.html")
@app.route('/handle_data', methods=['POST'])

def handle_data():
    url_text = request.form['link']
    print(f"url_text handle_data:{url_text}")
    url_text_main = url_text
    text_content = request.form['text']
    
    content_main = text_content
    conversation = []
    text = ""
    if url_text and len(text_content) < 10:
        html = urlopen(url_text).read()
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
    else:
        text = str(text_content)
        
    first_question = "Can you reformat the following information into Lecture Number, Topic Name, Day, Date, Homeworks due date into a csv, from the following text:" + text
    # Lecture Number, Topic Name, Date,Homework Info, Homeworks into a csv, from the following text:" + text
    conversation.append({'role':'system','content':first_question})
    conversation = chat_gpt_conversation(conversation)
    print(f"conversation[-1]['content']:{conversation[-1]['content']}")
    print(f"Type of conversation[-1]['content']:{type(conversation[-1]['content'])},list of output:{list(conversation[-1]['content'])}")
    with open('output.csv','w') as out:
        out.write("Lecture Number, Topic Name,Day, Date,Homework due date Info, Homeworks due date\n")
        out.write(conversation[-1]['content'].strip())
    print(f"writes to output.csv")
        # Refine the output to add or remove a column, 
    # conversation.append({'role':'user','content':'can you be more specific on item #2?'})
    # conversation = chat_gpt_conversation(conversation)
# def change_data_request():
#     new_question = "Can you reformat the following information into Lecture Number, Topic Name, Day, Date, Homeworks due date into a csv, from the following text:" + text
    data  = pd.read_csv('output.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])
@app.route('/table')

def table():
    
    # converting csv to html
    data = pd.read_csv('sample_data.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])
@app.route('/handle_data2', methods=['POST'])

def handle_data2():
    print(f'URL: {url_text_main}, Content: {content_main} in handle_data2')
    # print(f'Column Name: {request.form['text']}')
    url_text = url_text_main
    text_content = content_main
    add_column = request.form['text']
    conversation = []
    text = ""
    if url_text and len(text_content) < 10:
        html = urlopen(url_text).read()
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
    else:
        text = str(text_content)
        
    first_question = "Can you reformat the following information into Lecture Number, Topic Name, Day, Date, Homeworks due date," + add_column + "into a csv, from the following text:" + text
    conversation.append({'role':'system','content':first_question})
    conversation = chat_gpt_conversation(conversation)
    
    with open('output2.csv','w') as out:
        out.write(conversation[-1]['content'].strip())
        # Refine the output to add or remove a column, 
    # conversation.append({'role':'user','content':'can you be more specific on item #2?'})
    # conversation = chat_gpt_conversation(conversation)
# def change_data_request():
#     new_question = "Can you reformat the following information into Lecture Number, Topic Name, Day, Date, Homeworks due date into a csv, from the following text:" + text
    data  = pd.read_csv('output2.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])
# @app.route('/table')