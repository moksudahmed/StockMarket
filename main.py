
from flask import Flask
import threading
import time
import markettiming
from flask import Flask , request, jsonify
import processdata
import scraper_engine
import log


my_stock_app = Flask(__name__)


def run_app():
    my_stock_app.run(debug=False, threaded=True)


def while_function():
    #markettiming.determine_market_timming("11:20:00 PM", "02:30:00 PM")
    while True:
            scraper_engine.scraper_engine()            
            print("Data Scraped")
            data = {"Data Scraped":markettiming.get_bd_current_local_time()}
                    
            log.write_json(data)
            
            time.sleep(30)
            pass

@my_stock_app.route('/')
def hello_world():
    return jsonify(log.get_log())


@my_stock_app.route('/api/stock/all', methods=['GET'])
def api_stockall():
   # processdata.isModified() 
    return jsonify(processdata.get_stock_data())    

@my_stock_app.route('/api/stock/details')
def with_parameters():
    trading_code = request.args.get('trading_code')
    output = processdata.get_stock_details(trading_code)
  #  print(output)
    return jsonify(output)
 
@my_stock_app.route('/api/stock/get_top10_gainer_data', methods=['GET'])
def api_get_top10_gainer_data():
   # processdata.isModified() 
    return jsonify(processdata.get_top10_gainer_data())    

@my_stock_app.route('/api/stock/get_top10_loser_data', methods=['GET'])
def api_get_top10_loser_data():
   # processdata.isModified() 
    return jsonify(processdata.get_top10_loser_data())    

@my_stock_app.route('/api/stock/get_top20_share_data', methods=['GET'])
def api_get_top20_share_data():
   # processdata.isModified() 
    return jsonify(processdata.get_top20_share_data())    

@my_stock_app.route('/api/stock/get_local_time', methods=['GET'])
def api_get_local_time():
    return jsonify(processdata.get_local_time())    

if __name__ == "__main__":
    first_thread = threading.Thread(target=run_app)
    second_thread = threading.Thread(target=while_function)
    first_thread.start()
    second_thread.start()