from flask import Flask, render_template ,jsonify
from database import load_exps_from_db


app=Flask(__name__)


    
@app.route("/")
def hello_world():
  exper=load_exps_from_db() 
  return render_template('home.html',
                          exp=exper,
                          page_name='Portfolio')
@app.route("/api/expertise")
def list_expertise():
  exper=load_exps_from_db() 
  return jsonify(exper)
if __name__ =="__main__":
  app.run(host='0.0.0.0',debug=True)
