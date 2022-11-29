from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://PikaEW:gur9693@cluster0.hwkxjea.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.portfolio


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/jk", methods=["POST"])
def jk_post():
    url_receive = request.form['url_give']
    writer_receive = request.form['writer_give']
    comment_receive = request.form['comment_give']
    heart_receive = request.form['heart_give']

    if '?v=' in url_receive and 'youtu' in url_receive:
        video_id = url_receive.split('?v=')[1]
    else:
        video_id = url_receive.split('.be/')[1]


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    # if '?v=' in url_receive:
    #     video_id = url_receive.split('?v=')[1]
    # elif '.be/' in url_receive:
    #     video_id = url_receive.split('.be/')[1]
    # else :


    title = soup.select_one('title').text
    img = 'https://img.youtube.com/vi/' + video_id + '/0.jpg'

    doc = {
        'title':title,
        'img':img,
        'writer':writer_receive,
        'comment':comment_receive,
        'heart':heart_receive,
        'url':url_receive,

    }
    db.jks.insert_one(doc)

    return jsonify({'msg':'꾸러미에 추가!'})

@app.route("/jk", methods=["GET"])
def jk_get():
    jk_list = list(db.jks.find({}, {'_id': False}))
    return jsonify({'jks':jk_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)