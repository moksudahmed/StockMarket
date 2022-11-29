import flask
from flask import request, jsonify
import processdata
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/stock/all', methods=['GET'])
def api_stockall():
    processdata.isModified() 
    return jsonify(processdata.get_stock_data())    

@app.route('/api/v1/resources/stock/top_ten_gainer', methods=['GET'])
def api_top_ten_gainer():
   # processdata.isModified() 
    return jsonify(processdata.get_top10_gainer_data())    

@app.route('/api/v1/resources/stock/top_ten_loser', methods=['GET'])
def api_top_ten_loser():
   # processdata.isModified() 
    return jsonify(processdata.get_top10_loser_data())    

@app.route('/api/v1/resources/stock/top_20_share', methods=['GET'])
def api_top_20_share():
   # processdata.isModified() 
    return jsonify(processdata.get_top20_share_data())    

app.run()
