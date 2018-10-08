import requests
#user = driver.find_element_by_name("LoginUserPassword_auth_username")
#password = driver.find_element_by_name("LoginUserPassword_auth_password")
#user.clear()
#user.send_keys("RA1611003010766")
#password.clear()
#password.send_keys("Cse~1323")
#driver.find_element_by_name("UserCheck_Login_Button_span").click()
s=requests.Session()
print(s)
l=requests.head('https://192.168.10.3/connect/PortalMain',verify=False)
i=l.headers['Set-Cookie'].split(';')
sesid=i[0]
header={
	'POST' : '/connect/Login HTTP/1.1',
	'Host' : '192.168.10.3',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0',
	'Accept' : '*/*',
	'Accept-Language' : 'en-US,en;q=0.5',
	'Accept-Encoding' : 'gzip, deflate',
	'Referer' : 'https://192.168.10.3/connect/PortalMain',
	'Content-type' : 'application/x-www-form-urlencoded',
	'Content-Length' : '310',
	'Cookie': 'cpnacportal_login_type=password; cpnacportal_username=RA1611003010766; %s' %(sesid),
	'Connection' : 'close'
}
login=requests.post('https://192.168.10.3/connect/Login',headers=header,verify=False)
print(login.text)

