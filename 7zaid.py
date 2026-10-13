@app.post("/create_user,response_model=UserResponse)
def create_user(user: UserCreate,session: Session = Depends(get_db)):
    existing_user=session.exec(select(User).where(User.email==user.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
        hashed_password= generate_password_hash(data.password)
        user=User(username=data.username,email=data.email,password=hashed_password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user