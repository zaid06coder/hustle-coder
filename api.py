class Userlogin(BaseModel):
    email: emailstr
    password:str
    class loginResponse(BaseModel):
        message:str
        id:int
        username:str
        email:emailstr
        