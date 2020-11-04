from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        "id": 1,
        "Name": u"Vikrant",
        "Contact": u"9888003326",
        "done": False
    },
    {
        "id": 2,
        "Name": u"Ritu",
        "Contact": u"9876546726",
        "done": False
    },
    {
        "id": 3,
        "Name": u"Samiksha",
        "Contact": u"7087808026",
        "done": False
    },
]
@app.route("/")
def hello_world():
    return "hello world"
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data !",

        }, 400)
    contact = {
        "id": tasks[-1]["id"]+1,
        "name": request.json["name"],
        "contact": request.json.get("Contact",""),
        "done": False
    }
    tasks.append(contact)
    return jsonify({
        "status": "Success",
        "message": "Contact added successfully",
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })
if (__name__== "__main__"):
    app.run(debug = True)