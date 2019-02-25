from flask import g, Markup,request
from flask import (Blueprint, render_template, make_response, redirect, url_for, abort, request, Response)
from tw33t import app
from functools import wraps
from flask import jsonify
from twitter import *
import json, requests, datetime, sys, os, uuid, re, time


# Introduce a "Get tweets" route for the client and log relevant info from each search into a file.

# config tweeter apis
twitter = Twitter(
    auth= OAuth('1098961813935337472-bnLF09f9juoy8c7L7sAFxQZZqU5V3D','WFwWnd3znSZT3px75dtu6FD7g2HElnDDpa62l9KeHInqn',
           'w0i9A8PtXlJxsYcRtWSjmzsDR','Fw4yy8pcu0yTiZbT07QXaGiN4EnGKadWTMrQtSxoQ6XrZ99Cwe'
    )
)
# get three last post in  twitter
@app.route("/api/v1.0/gettweets",methods=['GET'])
def get_my_tweet():
    query = request.args.get('search')
    result= twitter.statuses.user_timeline(screen_name=query,count=5)
    print(type(result))
    log_search_file=open('./log/LogSearch.json','a')
    log_search_file.write(json.dumps(result))
    log_search_file.close()
    return json.dumps(result)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

# handle error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

