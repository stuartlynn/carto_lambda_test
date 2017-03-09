from flask import Flask
from flask import jsonify
from flask import request
from urllib import urlencode
import requests
import pandas 
import StringIO

from sklearn.cluster import AgglomerativeClustering 
app = Flask(__name__)

@app.route('/')
def index():
    input_query = request.args.get('inputQuery')
    cluster_no  = request.args.get('clusterNo')
    username    = request.args.get('username')
    target_table = request.args.get('target')


    if not cluster_no:
        cluster_no = 3 

    if not username:
        return 'require username'

    if not input_query:
        return 'need input query'


    url = 'https://{username}.carto.com/api/v2/sql?'.format(username=username) + urlencode({'q':input_query,'format':'csv'})
    data = pandas.read_csv(url)
    X= data.drop('cartodb_id',axis=1).as_matrix()
    AC = AgglomerativeClustering(int(cluster_no))
    s = StringIO.StringIO()
    result = AC.fit_predict(X)

    data.assign(result=result).to_csv(s)

    return s.getvalue()

if __name__ == '__nain__':
    app.run()
