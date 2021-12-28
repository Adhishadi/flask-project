from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/admin')
def admn():
    return 'hi helloo'



@app.route('/test',methods = ['GET'])
def test():
    if request.method == 'GET':
        return jsonify({"name":"Adhish"})

if __name__ == "__main__":
    app.run(debug=True)

