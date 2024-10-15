
from models import AuthModel,TokenModel
from datetime import datetime,timezone,timedelta
import random
import string

def authenticate_user(db,username,password):
    user = db.query(AuthModel).filter(AuthModel.username == username).first()
    if not user:
        return None
    return user


def generate_token(db,user):
    token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
    expiration_time = datetime.now(timezone.utc) + timedelta(days=7)
    existing_token = db.query(TokenModel).filter(TokenModel.user_id == user.id).one_or_none()
    if existing_token:
        existing_token.expiration_date = datetime.now(timezone.utc) + timedelta(days=7)
        existing_token.token = token
        db.commit()
        db.refresh(existing_token)
    else:
        token_obj = TokenModel(user_id=user.id,token=token,expiration_date=expiration_time)
        db.add(token_obj)
        db.commit()
        db.refresh(token_obj)
    return token
