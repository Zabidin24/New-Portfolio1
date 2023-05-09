from flask import Flask, render_template ,jsonify
from database import engine
from sqlalchemy import text


app=Flask(__name__)

def load_exps_from_db():
 with engine.connect() as conn:
    result=conn.execute(text("select * from exp" ))
    result_dicts=[]
    for row in result.all():
     result_dicts.append(row._asdict())
    return result_dicts
    
@app.route("/")
def hello_world():
  exper=load_exps_from_db()
  return render_template('home.html',
                          exp=exper,
                          page_name='Portfolio')
@app.route("/api/expertise")
def list_expertise():
  return jsonify(Expertise)
if __name__ =="__main__":
  app.run(host='0.0.0.0',debug=True)
