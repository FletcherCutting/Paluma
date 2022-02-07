from flask import Flask
from flask_restful import Api, Resource
from IPython.display import display

import os
import numpy as np
import pandas as pd

app = Flask(__name__)
api = Api(app)

palumaData = pd.DataFrame(columns=["identifier", "type", "info"])

if os.path.isfile('./df.csv'):
    palumaData = pd.read_csv('df.csv')

class PalumaPing(Resource):
    def get(self, identifier):
        print('Print request from {}'.format(identifier))
        
        df = pd.DataFrame({
            "identifier": [identifier],
            "type": ['ping'],
            "info": ['']
        })

        global palumaData
        palumaData = pd.concat([palumaData, df])
        palumaData.to_csv('df.csv', index=False)

api.add_resource(PalumaPing, '/ping/<string:identifier>')

if __name__ == '__main__':
    app.run(debug=True)
