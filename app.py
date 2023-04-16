from flask import Flask,render_template, request
import openai
import pandas as pd
from urllib.request import urlopen
from flask import Flask, Response
from bs4 import BeautifulSoup
global df
df = pd.read_csv('output.csv',encoding='unicode_escape', on_bad_lines='skip')

# api_key = NEED TO ADD THIS FOR CODE TO WORK!
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
    conversation.append({'role':response.choices[0].message.role,'content':response.choices[0].message.content})
    return conversation


app = Flask(__name__)
@app.route("/")

def home():
    return render_template("homepage.html")
@app.route('/handle_data', methods=['POST'])

def handle_data():
    global df
    url_text = request.form['link']
    print(f"url_text handle_data:{url_text}")
    text_content = request.form['text']    
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
        
    first_question = "Can you reformat the following information into Lecture Number, Topic Name, Date, Homeworks due date into a csv, from the following text:" + text
    # Lecture Number, Topic Name, Date,Homework Info, Homeworks into a csv, from the following text:" + text
    conversation.append({'role':'system','content':first_question})
    conversation = chat_gpt_conversation(conversation)
    # print(f"conversation[-1]['content']:{conversation[-1]['content']}")
    lst = conversation[-1]['content'].split('\n')
    for i in range(len(lst)):
        if lst[i].find(":") == -1:
            lst[i] = lst[i].split(',')
        else:
            index = lst[i].find(":")
            lst[i] = [lst[:index]] + ''.join(lst[i][lst[i].find(":")+1:]).split(',')
        print(f"lst[i]:{lst[i]}")
        if lst[i][-1] == "":
            lst[i] = lst[i][:-1]
    lst = lst[1:]
    # print(f"Type of conversation[-1]['content']:{type(conversation[-1]['content'])},list of output:{lst}")
    with open('output.csv','w') as out:
        # out.write("Lecture Number, Topic Name,Day, Date,Homework due date Info, Homeworks due date\n")
        out.write(conversation[-1]['content'].strip())
    df  = pd.read_csv('output.csv',encoding='unicode_escape', on_bad_lines='skip')
    
    return render_template('homepage.html', proxies=lst, titles=[''])

@app.route('/get_csv')
def get_csv():
    global df
    return Response(
        df,
        mimetype="text/csv",
        headers={"Content-disposition":
"attachment; filename=assignment.csv"})
# send_from_directory("/", "output.csv", as_attachment=True)

@app.route('/get_syllabus')
def get_syllabus():
    global df
    # df = pd.read_csv('output.csv')
    print(f"df:{df} get_syllabus")
    result = df.to_json(orient="table")
    return {"syllabus": result}
