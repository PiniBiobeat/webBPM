import psycopg2
import requests
import jsonpath



def create_token():
    token_url = "https://groupa.lupa.co.il/v1/api.aspx?method=login&cloudcode=public&app_version=3.4.108.d&device_type=android&lang=he&token="
    data = {'email': 'pinimautoxoxo@lupa.co.il', 'password': 'pinim1'}
    response = requests.get(token_url, data)
    if response.status_code != 200:
        token_url = 'https://monitor.lupa.co.il/api/api.aspx?method=write_errors&source=AutomationMonitor&service_api=hi'
        obj = {}
        obj["errors"] = str('login')
        requests.post(token_url, data=obj)
    token_value = jsonpath.jsonpath(response.json(), 'payload')
    token = token_value[0]['token']
    return  token


def test_check_all_site_ver3():
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
        cursor.execute("SELECT * FROM public.monitor_app_ver_3")
        record = cursor.fetchall()
        print(len(record))
        print("You are connected to - ", record, "\n")
        list_url_err = list()
        token_from_login = create_token()
        event_token = "&event_token=f932c5f9a2914232b085724ac6b39dbd"
        for i in record:
            token_site = i[0]
            response = requests.get(token_site + token_from_login)
            if response.status_code != 200:
                e = {"source": "AutomationMonitor", "service_api": i[1], "error_code": 17, "active": "true",
                     "token": "", "extra_params": {"url": i[0] + token_from_login ,"Error_code":response.status_code}}
                list_url_err.append(e)
                continue
        token_url = 'http://monitor.lupa.co.il/api/api.aspx?method=write_errors&source=AutomationMonitor&service_api=hi'
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
#test_create_token()
test_check_all_site_ver3()

#{"isValid":false,"errorCode":117,"Error":"ERROR_UNABLE_PARSE_TREE_MESSAGE","method":"albumthemes3","payload":null}
