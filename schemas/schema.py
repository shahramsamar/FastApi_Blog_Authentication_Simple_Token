from pydantic import BaseModel
class NamesSchema(BaseModel):
    name : str 
    first_name : str = None
    last_name : str = None
    
class ResponseNamesSchema(NamesSchema):
    id: int



