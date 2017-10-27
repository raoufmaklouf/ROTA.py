import urllib.request
import os
from datetime import datetime
from sys import exit

logo='''
         _________________ROTA__________________

          ROTA=f413efee4a810029b41cbf6d72f91962

          by Raouf Maklouf
                                 
                     ____  ____  _________ 
                    / __ \/ __ \/_  __/   |
                   / /_/ / / / / / / / /| |
                  / _, _/ /_/ / / / / ___ |
                 /_/ |_|\____/ /_/ /_/  |_|
                                     
                                 
                                                        
          Free Tool For Find Admin Panel Page 
      
         ____________hapy hacking__-_-__________
'''
print(logo)
print(' ')
print(' ')
print('\033[45m [+] enter protocol type and url(http://www.example.com) \033[0m')
print(' ')
url=str(input('\033[44m url: \033[0m'))
os.system('clear')

print('\033[45m [1] if you want used Default word list enter [1] \033[0m')
print('\033[45m [2] if you want used other word list enter [2] \033[0m')
print(' ')
try:
    choicelist=int(input('\033[44m Enter your choice: \033[0m'))
except ValueError:
    print(' ')
    print('\033[45m [-] Error -_- Your choice is wrong is not exist \033[0m')
    exit()
os.system('clear')
def choice1():
    adlist=['administrator/\n', 'admin1/\n', 'admin2/\n', 'admin3/\n', 'admin4/\n', 'admin5/\n', 'usuarios/\n', 'usuario/\n', 'moderator/\n', 'webadmin/\n', 'adminarea/\n', 'bb-admin/\n', 'adminLogin/\n', 'admin_area/\n', 'panel-administracion/\n', 'instadmin/\n', 'memberadmin/\n', 'administratorlogin/\n', 'adm/\n', 'admin/account.php\n', 'admin/index.php\n', 'admin/login.php\n', 'admin/admin.php\n', 'admin_area/admin.php\n', 'admin_area/login.php\n', 'siteadmin/login.php\n', 'siteadmin/index.php\n', 'siteadmin/login.html\n', 'admin/account.html\n', 'admin/login.html\n', 'admin/admin.html\n', 'admin_area/index.php\n', 'bb-admin/index.php\n', 'bb-admin/login.php\n', 'bb-admin/admin.php\n', 'admin/home.php\n', 'admin_area/login.html\n', 'admin_area/index.html\n', 'admin/controlpanel.php\n', 'admin.php\n', 'admincp/index.asp\n', 'admincp/login.asp\n', 'admincp/index.html\n', 'adminpanel.html\n', 'webadmin.html\n', 'webadmin/index.html\n', 'webadmin/admin.html\n', 'webadmin/login.html\n', 'admin/admin_login.html\n', 'admin_login.html\n', 'panel-administracion/login.html\n', 'admin/cp.php\n', 'cp.php\n', 'administrator/index.php\n', 'administrator/login.php\n', 'nsw/admin/login.php\n', 'webadmin/login.php\n', 'admin/admin_login.php\n', 'admin_login.php\n', 'administrator/account.php\n', 'administrator.php\n', 'admin_area/admin.html\n', 'pages/admin/admin-login.php\n', 'admin/admin-login.php\n', 'admin-login.php\n', 'bb-admin/index.html\n', 'bb-admin/login.html\n', 'acceso.php\n', 'bb-admin/admin.html\n', 'admin/home.html\n', 'login.php\n', 'modelsearch/login.php\n', 'moderator.php\n', 'moderator/login.php\n', 'moderator/admin.php\n', 'account.php\n', 'pages/admin/admin-login.html\n', 'admin/admin-login.html\n', 'admin-login.html\n', 'controlpanel.php\n', 'admincontrol.php\n', 'admin/adminLogin.html\n', 'adminLogin.html\n', 'home.html\n', 'rcjakar/admin/login.php\n', 'adminarea/index.html\n', 'adminarea/admin.html\n', 'webadmin.php\n', 'webadmin/index.php\n', 'webadmin/admin.php\n', 'admin/controlpanel.html\n', 'admin.html\n', 'admin/cp.html\n', 'cp.html\n', 'adminpanel.php\n', 'moderator.html\n', 'administrator/index.html\n', 'administrator/login.html\n', 'user.html\n', 'administrator/account.html\n', 'administrator.html\n', 'login.html\n', 'modelsearch/login.html\n', 'moderator/login.html\n', 'adminarea/login.html\n', 'panel-administracion/index.html\n', 'panel-administracion/admin.html\n', 'modelsearch/index.html\n', 'modelsearch/admin.html\n', 'admincontrol/login.html\n', 'adm/index.html\n', 'adm.html\n', 'moderator/admin.html\n', 'user.php\n', 'account.html\n', 'controlpanel.html\n', 'admincontrol.html\n', 'panel-administracion/login.php\n', 'wp-login.php\n', 'adminLogin.php\n', 'admin/adminLogin.php\n', 'home.php\n', 'adminarea/index.php\n', 'adminarea/admin.php\n', 'adminarea/login.php\n', 'panel-administracion/index.php\n', 'panel-administracion/admin.php\n', 'modelsearch/index.php\n', 'modelsearch/admin.php\n', 'admincontrol/login.php\n', 'adm/admloginuser.php\n', 'admloginuser.php\n', 'admin2.php\n', 'admin2/login.php\n', 'admin2/index.php\n', 'usuarios/login.php\n', 'adm/index.php\n', 'adm.php\n', 'affiliate.php\n', 'adm_auth.php\n', 'memberadmin.php\n', 'administratorlogin.php\n', 'admin/\n', 'account.asp\n', 'admin/account.asp\n', 'admin/index.asp\n', 'admin/login.asp\n', 'admin/admin.asp\n', 'admin_area/admin.asp\n', 'admin_area/login.asp\n', 'admin/index.html\n', 'admin_area/index.asp\n', 'bb-admin/index.asp\n', 'bb-admin/login.asp\n', 'bb-admin/admin.asp\n', 'admin/home.asp\n', 'admin/controlpanel.asp\n', 'admin.asp\n', 'pages/admin/admin-login.asp\n', 'admin/admin-login.asp\n', 'admin-login.asp\n', 'admin/cp.asp\n', 'cp.asp\n', 'administrator/account.asp\n', 'administrator.asp\n', 'acceso.asp\n', 'login.asp\n', 'modelsearch/login.asp\n', 'moderator.asp\n', 'moderator/login.asp\n', 'administrator/login.asp\n', 'moderator/admin.asp\n', 'controlpanel.asp\n', 'user.asp\n', 'admincontrol.asp\n', 'adminpanel.asp\n', 'webadmin.asp\n', 'webadmin/index.asp\n', 'webadmin/admin.asp\n', 'webadmin/login.asp\n', 'admin/admin_login.asp\n', 'admin_login.asp\n', 'panel-administracion/login.asp\n', 'adminLogin.asp\n', 'admin/adminLogin.asp\n', 'home.asp\n', 'adminarea/index.asp\n', 'adminarea/admin.asp\n', 'adminarea/login.asp\n', 'panel-administracion/index.asp\n', 'panel-administracion/admin.asp\n', 'modelsearch/index.asp\n', 'modelsearch/admin.asp\n', 'administrator/index.asp\n', 'admincontrol/login.asp\n', 'adm/admloginuser.asp\n', 'admloginuser.asp\n', 'admin2.asp\n', 'admin2/login.asp\n', 'admin2/index.asp\n', 'adm/index.asp\n', 'adm.asp\n', 'affiliate.asp\n', 'adm_auth.asp\n', 'memberadmin.asp\n', 'administratorlogin.asp\n', 'siteadmin/login.asp\n', 'siteadmin/index.asp\n', 'admin/account.cfm\n', 'admin/index.cfm\n', 'admin/login.cfm\n', 'admin/admin.cfm\n', 'admin_area/admin.cfm\n', 'admin_area/login.cfm\n', 'siteadmin/login.cfm\n', 'siteadmin/index.cfm\n', 'admin_area/index.cfm\n', 'bb-admin/index.cfm\n', 'bb-admin/login.cfm\n', 'bb-admin/admin.cfm\n', 'admin/home.cfm\n', 'admin/controlpanel.cfm\n', 'admin.cfm\n', 'admin/cp.cfm\n', 'cp.cfm\n', 'administrator/index.cfm\n', 'administrator/login.cfm\n', 'nsw/admin/login.cfm\n', 'webadmin/login.cfm\n', 'admin/admin_login.cfm\n', 'admin_login.cfm\n', 'administrator/account.cfm\n', 'administrator.cfm\n', 'pages/admin/admin-login.cfm\n', 'admin/admin-login.cfm\n', 'admin-login.cfm\n', 'login.cfm\n', 'modelsearch/login.cfm\n', 'moderator.cfm\n', 'moderator/login.cfm\n', 'moderator/admin.cfm\n', 'account.cfm\n', 'controlpanel.cfm\n', 'admincontrol.cfm\n', 'acceso.cfm\n', 'rcjakar/admin/login.cfm\n', 'webadmin.cfm\n', 'webadmin/index.cfm\n', 'webadmin/admin.cfm\n', 'adminpanel.cfm\n', 'user.cfm\n', 'panel-administracion/login.cfm\n', 'wp-login.cfm\n', 'adminLogin.cfm\n', 'admin/adminLogin.cfm\n', 'home.cfm\n', 'adminarea/index.cfm\n', 'adminarea/admin.cfm\n', 'adminarea/login.cfm\n', 'panel-administracion/index.cfm\n', 'panel-administracion/admin.cfm\n', 'modelsearch/index.cfm\n', 'modelsearch/admin.cfm\n', 'admincontrol/login.cfm\n', 'adm/admloginuser.cfm\n', 'admloginuser.cfm\n', 'admin2.cfm\n', 'admin2/login.cfm\n', 'admin2/index.cfm\n', 'usuarios/login.cfm\n', 'adm/index.cfm\n', 'adm.cfm\n', 'affiliate.cfm\n', 'adm_auth.cfm\n', 'memberadmin.cfm\n', 'administratorlogin.cfm\n', 'cp.cgi\n', 'administrator/index.cgi\n', 'administrator/login.cgi\n', 'nsw/admin/login.cgi\n', 'webadmin/login.cgi\n', 'admin/admin_login.cgi\n', 'admin_login.cgi\n', 'administrator/account.cgi\n', 'administrator.cgi\n', 'pages/admin/admin-login.cgi\n', 'admin/admin-login.cgi\n', 'admin-login.cgi\n', 'login.cgi\n', 'modelsearch/login.cgi\n', 'moderator.cgi\n', 'moderator/login.cgi\n', 'moderator/admin.cgi\n', 'account.cgi\n', 'controlpanel.cgi\n', 'admincontrol.cgi\n', 'rcjakar/admin/login.cgi\n', 'webadmin.cgi\n', 'webadmin/index.cgi\n', 'acceso.cgi\n', 'webadmin/admin.cgi\n', 'adminpanel.cgi\n', 'user.cgi\n', 'panel-administracion/login.cgi\n', 'wp-login.cgi\n', 'adminLogin.cgi\n', 'admin/adminLogin.cgi\n', 'home.cgi\n', 'admin.cgi\n', 'adminarea/index.cgi\n', 'adminarea/admin.cgi\n', 'adminarea/login.cgi\n', 'panel-administracion/index.cgi\n', 'panel-administracion/admin.cgi\n', 'admin/index.html/', 'modelsearch/index.cgi\n', 'modelsearch/admin.cgi\n', 'admincontrol/login.cgi\n', 'adm/admloginuser.cgi\n', 'admloginuser.cgi\n', 'admin2.cgi\n', 'admin2/login.cgi\n', 'admin2/index.cgi\n', 'usuarios/login.cgi\n', 'adm/index.cgi\n', 'adm.cgi\n', 'affiliate.cgi\n', 'adm_auth.cgi\n', 'memberadmin.cgi\n', 'administratorlogin.cgi\n', 'admin4\n', 'admincontrol.html', 'joomla/administrator\n', 'admin/account.js\n', 'admin/index.js\n', 'admin/login.js\n', 'admin/admin.js\n', 'admin_area/admin.js\n', 'admin_area/login.js\n', 'siteadmin/login.js\n', 'siteadmin/index.js\n', 'admin_area/index.js\n', 'bb-admin/index.js\n', 'bb-admin/login.js\n', 'bb-admin/admin.js\n', 'admin/home.js\n', 'admin/controlpanel.js\n', 'admin.js\n', 'admin/cp.js\n', 'cp.js\n', 'administrator/index.js\n', 'administrator/login.js\n', 'nsw/admin/login.js\n', 'webadmin/login.js\n', 'admin/admin_login.js\n', 'admin_login.js\n', 'administrator/account.js\n', 'administrator.js\n', 'pages/admin/admin-login.js\n', 'admin/admin-login.js\n', 'admin-login.js\n', 'login.js\n', 'modelsearch/login.js\n', 'moderator.js\n', 'moderator/login.js\n', 'moderator/admin.js\n', 'account.js\n', 'controlpanel.js\n', 'admincontrol.js\n', 'rcjakar/admin/login.js\n', 'webadmin.js\n', 'webadmin/index.js\n', 'acceso.js\n', 'webadmin/admin.js\n', 'adminpanel.js\n', 'user.js\n', 'panel-administracion/login.js\n', 'wp-login.js\n', 'adminLogin.js\n', 'admin/adminLogin.js\n', 'home.js\n', 'adminarea/index.js\n', 'adminarea/admin.js\n', 'adminarea/login.js\n', 'panel-administracion/index.js\n', 'panel-administracion/admin.js\n', 'modelsearch/index.js\n', 'modelsearch/admin.js\n', 'admincontrol/login.js\n', 'adm/admloginuser.js\n', 'admloginuser.js\n', 'admin2.js\n', 'admin2/login.js\n', 'admin2/index.js\n', 'usuarios/login.js\n', 'adm/index.js\n', 'adm.js\n', 'affiliate.js\n', 'adm_auth.js\n', 'memberadmin.js\n', 'administratorlogin.js\n', 'admin/account.cgi\n', 'admin/index.cgi\n', 'admin/login.cgi\n', 'admin/admin.cgi\n', 'admin_area/admin.cgi\n', 'admin_area/login.cgi\n', 'siteadmin/login.cgi\n', 'siteadmin/index.cgi\n', 'admin_area/index.cgi\n', 'bb-admin/index.cgi\n', 'bb-admin/login.cgi\n', 'bb-admin/admin.cgi\n', 'admin/home.cgi\n', 'admin/controlpanel.cgi\n', 'admin/cp.cgi\n', 'admin_panel/\n', 'admin_panel.html\n', 'adm_cp/\n']
    cturl=[]
    a=datetime.now()
    for i in adlist:
        i=i.rstrip("\n")
        tesurl=(url+''+'/'+''+i)
        try:
            urllib.request.urlopen(tesurl)
            urlfound=('\033[42;142m {} [+]found \033[0m'.format(tesurl))
            print(urlfound)
            cturl.append(urlfound)
        except urllib.error.HTTPError:
            print('\033[31;142m {} [-]Not found \033[0m'.format(tesurl))   
            continue
    b=datetime.now()
    c=(b-a)
    d=len(cturl)
    print(' ')
    print('\033[45m Finished the scany at {} \033[0m'.format(c))
    print('\033[45m The number of results obtained is: {} url \033[0m'.format(d))
    print(' ')
    for i in cturl:
        i=i[:-14]        
        print(i)
        
def choice2():
    print(' ')
    wordlist=input('\033[44m enter word list: \033[0m')
    os.system('clear')
    wordlist=open(wordlist,'r')
    cturl=[]
    a=datetime.now()    
    for i in wordlist:
        i=i.rstrip("\n")
        tesurl=(url+''+'/'+''+i)
        try:
            urllib.request.urlopen(tesurl)
            urlfound=('\033[31;42m {} [+]found \033[0m'.format(tesurl))
            print(urlfound)
            cturl.append(urlfound)
        except urllib.error.HTTPError:
            print('\033[31;142m {} [-]Not found \033[0m'.format(tesurl))
            continue
    b=datetime.now()
    c=(b-a)
    d=len(cturl)
    print(' ')
    print('\033[45m Finished the scany at {} \033[0m'.format(c))
    print('\033[45m The number of results obtained is: {} url \033[0m'.format(d))
    print(' ')
    for i in cturl:
        i=i[:-14]
        print(i)

if choicelist == 1:
    choice1()
elif choicelist == 2:
    choice2()
else:
    print(' ')
    print('\033[41m [-] Error -_- Your choice is wrong is not exist \033[0m')
    