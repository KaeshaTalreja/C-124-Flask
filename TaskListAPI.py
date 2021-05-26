# download pip using
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3 get-pip.py
# pip3 install Flask

from flask import Flask,jsonify,request

myAPI=Flask(__name__)

tasks=[
    {
        'id':1,
        'task': u'Practice projects',
        'description':u'Practice makes a man perfect',
        'status':False
    },
    {
        'id':2,
        'task': u'Learn new language',
        'description':u'The more you know, better it is.',
        'status':False
    }
]

@myAPI.route("/")
def hello_world():
    return "Hello World!!!"

@myAPI.route("/addTask",methods=["POST"])
def add_tasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide data"
        },400)
    
    task={
        'id':tasks[-1]['id']+1,
        'task': request.json['task'],
        'description':request.json.get('description',""),
        'status':False
    }

    tasks.append(task)
    return jsonify({
        "status":"Success",
        "message":"Task added successfully"
    })

@myAPI.route("/viewTasks")
def view_tasks():
    return jsonify({
        "data":tasks
    })

if(__name__=="__main__"):
    myAPI.run(debug=True)