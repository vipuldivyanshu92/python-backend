# account management library
# has login, signup,check nickname... request links

from pymonogo import Connection
import json
from datetime import datetime
#imports for hashing
import hashlib, uuid

auth_id=''

# mongodb code
connection=Connection()
users_collection = connection.Giffie.users_collection
def hash_password(password):
  salt = uuid.uuid4().hex
  hashed_password = hashlib.sha512(password + salt).hexdigest()
  return hashed_password
  
def create_account(auth_id,nick_name,password,email,phone_num,dob):
  password=hash_password(password)
  timestamp=str(datetime.now())
  account_exists=false;
  if(users_collection.find_one({'nick_name':nick_name},{'_id':1,'auth_id':1,'phone_num':1,'dob':1} != None ):
    return {'msg':'Nickname in use,click forgot password to retrive account'}
  if(users_collection.find_one({'email':email},{'_id':1,'auth_id':1,'phone_num':1,'dob':1} != None ):
    return {'msg':'Email in use, click forgot password to retrive account'}
  user={'nickname
  try:
    
  catch(Exception e):
    


