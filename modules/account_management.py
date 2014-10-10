# account management library
# has login, signup,check nickname... request links

# from pymonogo import Connection
import json
from datetime import datetime
#imports for hashing
import hashlib, uuid

AUTH_ID=''

# mongodb code
# connection=Connection()
# users_collection = connection.Giffie.users_collection
def hash_password(password):
  salt = uuid.uuid4().hex
  hashed_password = hashlib.sha512(password + salt).hexdigest()
  return hashed_password
  
def create_account(auth_id,db,nick_name,password,email,phone_num,dob):
  if(auth_id != AUTH_ID):
    return {'msg':'Nice Try'}
  password=hash_password(password)
  account_exists=false;
  try:
    if(users_collection.find_one({'nick_name':nick_name},{'_id':1,'auth_id':1,'phone_num':1,'dob':1} != None ):
      return {'msg':'Nickname in use,click forgot password to retrive account'}
    if(users_collection.find_one({'email':email},{'_id':1,'auth_id':1,'phone_num':1,'dob':1} != None ):
      return {'msg':'Email in use, click forgot password to retrive account'}
  except Exception:
    print 'error in reading the database'
    return {'msg':'SYSERROR'}
  timestamp=str(datetime.now())
  user={'nick_name':nick_name,'password':password,'email':email,'phone_num':phone_num,'dob':dob,'timestamp':timestamp}
  try:
    db.insert(user)  
    return {'msg':'SUCCESS','timestamp':timestamp}
  except Exception:
    return {'msg':'SYSERROR'}

def signin(auth_id,db,nick_name,password):
  if(auth_id != AUTH_ID):
    return {'msg':'Nice Try'}
  password=hash_password(password)
  try:
    u=db.find_one({'nick_name':nick_name,'password':password})
    if(u!=None):
      return {'cookie':nick_name+'^'+u[timestamp]}
  except Exception:
    return {'msg':'SYSERROR'}

def forgotpass(auth_id,db,email):
  if(auth_id != AUTH_ID):
    return {'msg':'Nice Try'}
  ### Write send email of forgot password code

