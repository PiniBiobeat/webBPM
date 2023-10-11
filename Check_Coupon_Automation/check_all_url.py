import psycopg2
import requests
import jsonpath

def check_all_site():
    class Error:
        def __init__(self, url, siteName):
            self.siteName = siteName
            self.url = url
    try:

        connection = psycopg2.connect(user="machineDBA",
                                      password="A#214Fdse!35dDC214XAzRDA12^79",
                                      host="10.116.96.3",
                                      port="5432",
                                      database="monitor_db")
        cursor = connection.cursor()
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        cursor.execute("SELECT * FROM public.monitor_sites")
        record = cursor.fetchall()
        print("You are connected to - ", record, "\n")
        list_url_err = list()
        for i in record:
            token_site = i[0]
            response = requests.get(token_site)
            if i[
                2] == True and response.content != b'Index was out of range. Must be non-negative and less than the size of the collection.\r\nParameter name: index':
                e = {"source": "AutomationMonitor", "service_api": i[1], "error_code": 14, "active": "true",
                     "token": "", "extra_params": {"url": i[0],"Error_code":response.status_code}}
                list_url_err.append(e)
                continue
            if response.status_code != 200:
                e = {"source": "AutomationMonitor", "service_api": i[1], "error_code": 14, "active": "true",
                     "token": "", "extra_params": {"url": i[0],"Error_code":response.status_code}}
                list_url_err.append(e)
                continue
        token_url = 'http://monitor.lupa.co.il/api/api.aspx?method=write_errors&source=AutomationMonitor&service_api=hi'




        #token_url_1 = token_url + str(list_url_err)__len__ = {int} 8
        obj = {}
        obj["errors"] = str(list_url_err)
        res = requests.post(token_url, data=obj)

        print(res)
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

check_all_site()
