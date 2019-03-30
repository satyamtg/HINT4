from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import json

SECRET = 'KhGkMigTi9aD4Vv4zsz8xISP2kU5I7rgq265DXiZ'
DSN = 'https://hint-ec580.firebaseio.com'
EMAIL = 'abhishek.tiwari3507@gmail.com'
authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
firebase = FirebaseApplication(DSN, authentication)

def upvote(idno):
    upvote = firebase.get("/articles/"+idno+"/upvote/", None)
    if(upvote == None):
        firebase.patch("/articles/"+idno, {'upvote': '1'})
    #print("/articles/"+idno+"/upvote")
    #print(upvote)
    upvote = upvote+1
    firebase.patch("/articles/"+idno, {'upvote': upvote})

def downvote(idno):
    downvote = firebase.get("/articles/"+idno+"/downvote/", None)
    if(downvote == None):
        firebase.patch("/articles/"+idno, {'downvote': '1'})
    downvote = downvote+1
    firebase.patch("/articles/"+idno, {'downvote': downvote})

def getfakeratio(idno):
    upvote = firebase.get("/articles/"+idno+"/upvote/", None)   
    downvote = firebase.get("/articles/"+idno+"/downvote/", None)
    fakeratio = downvote/(upvote+downvote)
    print(fakeratio)
    return fakeratio

#Test
#upvote("1")
#upvote("2")
#downvote("3")
#getfakeratio("1")

