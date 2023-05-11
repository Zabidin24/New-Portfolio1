from flask import Flask, render_template ,jsonify, request
from database import load_exps_from_db, load_exp_from_db


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
@app.route("/exp/<id>")
def show_jobs(id):
  exp=load_exp_from_db(id)
  if not exp:
    return "Not found 404"
  return render_template('expertise.html',exp=exp)


@app.route("/exp/<id>/enquire", methods=['post'])
def enquire_info(id):
  data=request.form
  return jsonify(data)
  
  
if __name__ =="__main__":
  app.run(host='0.0.0.0',debug=True)
