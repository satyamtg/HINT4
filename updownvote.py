from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import json

SECRET = 'KhGkMigTi9aD4Vv4zsz8xISP2kU5I7rgq265DXiZ'
DSN = 'https://hint-ec580.firebaseio.com'
EMAIL = 'abhishek.tiwari3507@gmail.com'
authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
firebase = FirebaseApplication(DSN, authentication)

def upvote(idno):
    upvote = firebase.get("/articles/"+idno+"/upvote", None)
    upvote = upvote+1
    firebase.patch("/articles/"+idno, {'upvote': upvote})

def downvote(idno):
    downvote = firebase.get("/articles/"+idno+"/downvote", None)
    downvote = downvote-1
    firebase.patch("/articles/"+idno, {'downvote': downvote})    
