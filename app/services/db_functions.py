from app.services.db import execute_sql

def create_data(tb_name, **data):
  try:
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["%s"] * len(data))
    values = tuple(data.values())
  
    sql = f"INSERT INTO {tb_name} ({columns}) VALUES ({placeholders})"
    
    res = execute_sql(sql, values)
    
    if res["status"] == 500:
      return res
    
    return {"msg":"created successfully!", "status":201}
    
  except Exception as e:
    print(f"Error(functions.create_data): {e}")
    return {"msg":"failed to create data.", "error":str(e), "status":500}

def read_data(tb_name, col="*", condition=None, vals=None):
  try:
    
    sql = f"SELECT {col} FROM {tb_name} WHERE {condition}"
    
    if condition is None:
      sql = f"SELECT {col} FROM {tb_name}"
    
    res = execute_sql(sql, isSelect=True, values=vals)
    
    if res["status"] == 500:
      return res
    
    return {"msg":"read successfully!", "data":res["data"], "status":200}
  except Exception as e:
    print(f"Error(functions.read_data): {e}")
    return {"msg":"failed to read data.", "error":str(e), "status":500}

def read_data_ordered(tb_name, col="*", order_by=None, limit=None, desc=False):
  try:
    sql = f"SELECT {col} FROM {tb_name} ORDER BY {order_by}"
    
    if desc:
      sql = f"SELECT {col} FROM {tb_name} ORDER BY {order_by} DESC"
    
    if limit != None:
      sql += f" LIMIT {limit}"
    
    res = execute_sql(sql, isSelect=True)
    
    if res["status"] == 500:
      return res
    
    return {"msg":"read successfully!", "data":res["data"], "status":200}
    
  except Exception as e:
    print(f"Error(functions.read_data_ordered): {e}")
    return {"msg":"failed to update data.", "error":str(e), "status":500}

def update_data(tb_name, condition, val, col):
  try:
    sql  = f"UPDATE {tb_name} SET {col} = %s WHERE {condition}"
    res = execute_sql(sql, (val,))
    
    if res["status"] == 500:
      return res
    
    return {"msg":"updated successfully!", "status":200}
    
  except Exception as e:
    print(f"Error(functions.update_data): {e}")
    return {"msg":"failed to update data.", "error":str(e), "status":500}

def delete_data(tb_name, condition):
  try:
    sql = f"DELETE FROM {tb_name} WHERE {condition}"
    res = execute_sql(sql)
    
    if res["status"] == 500:
      return res
    
    return {"msg":"deleted successfully!", "status":200}
  except Exception as e:
    print(f"Error(functions.delete_data): {e}")
    return {"msg":"failed to delete data.", "error":str(e), "status":500}

  