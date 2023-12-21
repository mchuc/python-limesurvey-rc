from pylimerc import PyLimeRc as RC

URL = "https://myurl.com/index.php/admin/remotecontrol"
SUVERY_ID = 123456
USER = "username"
PASS = "password"

test = RC(URL)
#test = RC(URL,"/directory/to/pylimerc.yml")
#test.set_url(URL)
test.get_session_key(USER,PASS)
test.add_participants(SUVERY_ID,
                      [{
                          "firstname": "A",
                          "lastname": "B",
                          "email": "XXX@gmail.com",
                          "emailstatus": "OK",
                          "language": "pl",
                          "token": "123456789"
                      }]
                      , True)

# test.add_participants(SUVERY_ID,
#                       [
#                       {
#                           "firstname": "C",
#                           "lastname": "D",
#                           "email": "YYY@gmail.com",
#                           "emailstatus": "OK",
#                           "language": "pl",
#                           "token": "123456789"
#                       },{
#                           "firstname": "D",
#                           "lastname": "D",
#                           "email": "YYY@gmail.com",
#                           "emailstatus": "OK",
#                           "language": "pl",
#                           "token": "123456789"
#                       } ,{
#                           "firstname": "E",
#                           "lastname": "D",
#                           "email": "YYY@gmail.com",
#                           "emailstatus": "OK",
#                           "language": "pl",
#                           "token": "123456789"
#                       },{
#                           "firstname": "F",
#                           "lastname": "D",
#                           "email": "YYY@gmail.com",
#                           "emailstatus": "OK",
#                           "language": "pl",
#                           "token": "123456789"
#                       },{
#                           "firstname": "G",
#                           "lastname": "D",
#                           "email": "YYY@gmail.com",
#                           "emailstatus": "OK",
#                           "language": "pl",
#                           "token": "123456789"
#                       }
#
#
#
#                       ]
#                       , True)

test.invite_participants(SUVERY_ID)
print("OK")
