import os
import pymysql

def main(req: func.HttpRequest) -> func.HttpResponse:
    connection_string = os.getenv('MYSQL_CONNECTION_STRING')
    
    # Parse the connection string
    conn_params = dict(item.split('=') for item in connection_string.split(';') if item)
    
    # Connect to MySQL
    connection = pymysql.connect(
        host=conn_params['Server'],
        user=conn_params['Uid'],
        password=conn_params['Pwd'],
        database=conn_params['Database'],
        ssl={'ca': '/path/to/BaltimoreCyberTrustRoot.crt.pem'}
    )
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
    
    return func.HttpResponse(f"The current time is: {result[0]}")
