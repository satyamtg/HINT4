from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import json

SECRET = 'KhGkMigTi9aD4Vv4zsz8xISP2kU5I7rgq265DXiZ'
DSN = 'https://hint-ec580.firebaseio.com'
EMAIL = 'abhishek.tiwari3507@gmail.com'
authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
firebase = FirebaseApplication(DSN, authentication)

<<<<<<< HEAD
def uploadarticle(idno, body, headline, author):
    data={'body' :body, 'author' :author, 'headline':headline}
=======
def uploadarticle(idno, body, headline, author, downvote, upvote,score):
    #changing score to str beacuse json is not float32 serialisable
    data={'body' :body, 'author' :author, 'headline':headline,'ml_score':str(score), 'idno': idno,'downvote':downvote, 'upvote':upvote}
>>>>>>> aea8c646d7920f4704bee8a3aa9893b9c62a2939
    putpath="/articles/"+str(idno)
    firebase.patch(putpath, data)

def fetcharticle(idno):
    data = firebase.get("/articles/"+str(idno), None)
    return data

# #Test
# uploadarticle("2+", "hello hi byt", "HHHH", "HHHHHHHHHH")
