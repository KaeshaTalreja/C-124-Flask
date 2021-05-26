from flask import Flask,jsonify,request

myApp=Flask(__name__)

contacts=[
    {
        'id':1,
        'name': u'Home',
        'contactNo':u'9876543210',
        'status':False
    },
    {
        'id':2,
        'name': u'Work',
        'contactNo':u'9812345678',
        'status':False
    }
]

@myApp.route("/")
def welcome():
    return "Welcome to Contacts API"

@myApp.route("/addContacts",methods=["POST"])
def add_contacts():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide data"
        },400)
    
    contact={
        'id':contacts[-1]['id']+1,
        'name': request.json['name'],
        'contactNo':request.json.get('description',""),
        'status':False    
    }

    contacts.append(contact)
    return jsonify({
        "status":"Success",
        "message":"Contact added successfully"
    })

@myApp.route("/viewContacts")
def view_contacts():
    return jsonify({
        "data":contacts
    })

if(__name__=="__main__"):
    myApp.run(debug=True)