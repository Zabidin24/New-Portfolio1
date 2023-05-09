from sqlalchemy import create_engine,text
conn_string="mysql+pymysql://epvl7l5gdol390wgcz20:pscale_pw_bHwNum3vozS0rcDS6gvZT6oCg2BU1Etoe4rlt0EwKjL@aws.connect.psdb.cloud/portfolio"
engine=create_engine(conn_string
                     ,connect_args={
                       "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }})
