from sqlalchemy import create_engine,text
import os
conn_string=os.environ['db_conn_string']

engine=create_engine(conn_string
                     ,connect_args={
                       "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }})
def load_exps_from_db():
 with engine.connect() as conn:
    result=conn.execute(text("select * from exp" ))
    result_dicts=[]
    for row in result.all():
     result_dicts.append(row._asdict())
    return result_dicts
   
def load_exp_from_db(id):
  with engine.connect() as conn:
    result=conn.execute(text("select * from exp where id= :val"),{"val":id})
    rows=result.all()
    if len(rows)==0:
      return None
    else: 
      return rows[0]._asdict()
def add_enquiry_to_db(ex_id,data):
  with engine.connect() as conn:
      query=text("insert into applications(ex_id,FullName,Email,LinkedinUrl,Requirements,Comments) VALUES(:ex_id,:FullName,:Email,:LinkedinUrl,:Requirements,:Comments)")
      conn.execute(query, {
            'ex_id': ex_id,
            'FullName': data['FullName'],
            'Email': data['Email'],
            'LinkedinUrl': data['LinkedinUrl'],
            'Requirements': data['Requirements'],
            'Comments': data['Comments']
        })