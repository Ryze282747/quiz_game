from flask import current_app
import pymysql

def get_db():
  return pymysql.connect(
    host=current_app.config["DB_HOST"],
    user=current_app.config["DB_USER"],
    password=current_app.config["DB_PASS"],
    database=current_app.config["DB_NAME"],
    cursorclass=pymysql.cursors.DictCursor  # return dicts
  )
  
def execute_sql(sql, values=None, isSelect=False):
  try:
    conn = get_db()
    
    cursor = conn.cursor()
    
    if values is not None:
      cursor.execute(sql, values)
    else:
      cursor.execute(sql)
    
    if isSelect:
      data = cursor.fetchall()
      conn.close()
      return {"data":data, "status":200}
  
    conn.commit()
    conn.close()
    return {"status":200}
  except Exception as e:
    print(f"Error(db.execute_sql): {e}")
    return {"error":str(e), "status":500}