from flask import Flask , request , jsonify
from flask_cors import CORS
from sortingAlgos import randomArray, animatedArray , algocomplexity
import json

app = Flask(__name__)
CORS(app)


@app.route('/sort' , methods = ["GET"])
def sort():
    if "parms" in request.args:
        parms = json.loads(request.args["parms"])

        array = parms["data"]
        algo = parms["algo"]

        if array == sorted(array):
            return jsonify(isSorted = True) , 200
        else:
            return jsonify(isSorted = False , data = animatedArray(algo,array))



@app.route('/generate' , methods = ["GET"])
def generate():
    if "parms" in request.args:
        parms = json.loads(request.args["parms"])
        
        arraySize = int(parms["arraySize"])

        return jsonify(data = randomArray(arraySize)) , 200

@app.route('/complexity', methods = ["GET"])
def complexity():
    if 'parms' in request.args:
        parms = json.loads(request.args['parms'])

        algo = parms['algo']

        return jsonify(data = algocomplexity(algo)) , 200
    

if __name__ == '__main__':
    app.run(debug = True)