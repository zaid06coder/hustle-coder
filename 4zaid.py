@contextmanager
async def lifespan(app: FastAPI):
  def  create_db_and_tables():
    SQLModel.metadata.create_all(engine)    
    app=fastapi(lifespam=lifespan)
     @app.get("/")
    def home():
        return {"message":"hello world"}

    
     class ship(basemodel):
        weight:float=Field(...,gt=0,description="weight of the ship")
        content:str=field(max
                          _length=100,description="content of the ship")
        
        
   
