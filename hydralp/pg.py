import psycopg2

def query(user, password, config):
  db = config["connection"]["db"]
  table = config["connection"]["table"]
  host = config["connection"]["host"]
  port = config["connection"]["port"]
  db_pass = config["connection"]["password"]

  user_col = config["basic"]["username"]
  pass_col = config["basic"]["password"]

  extras = config["extra"].keys()
  extras_str = ", ".join(extras)
  cols = user_col + ", " + pass_col + ", " + extras_str

  conn = psycopg2.connect(
    database=db,
    host=host,
    password=db_pass,
    port=port
  )
  
  cur = conn.cursor()

  query = f"select {cols} from {table} where {user_col}=%s and {pass_col}=%s"

  cur.execute(query, (user, password))

  res = cur.fetchone()

  cur.close()
  conn.close()

  return res
