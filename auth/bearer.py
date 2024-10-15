from fastapi import Request, HTTPException,Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from models import TokenModel 
from database.database import get_db

class TokenBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(TokenBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request,db: Session = Depends(get_db)):
        credentials: HTTPAuthorizationCredentials = await super(TokenBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer" or not credentials.scheme == "Basic" :
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication schema.")
            
            user = self.verify_token(db,credentials.credentials)
            if not user:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or expired token.")
            return user
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authorization code.")

    def verify_token(self, db,token: str):        
        token_obj = db.query(TokenModel).filter(TokenModel.token == token).first()
        if token_obj:
            return token_obj.user
        return None


