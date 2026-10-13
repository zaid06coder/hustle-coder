@app.get("/shipments")
def get_shipments(session:session=depends(get_session)):
    return session.execute(select(shipment)).all()
@app.get("/shipments/{shipment_id}")
def get_shipment(shipment_id:int,data:ship,sesssion:session=depends(get_session)):
    shipment=session.get(shipment,shipment_id)  
    shipment.sqlmodel_update(data.model_dump())
    session.add(shipment)
    session.commit()
    session.refresh(shipment) 
    return shipment


    @app.patch("/shipments/{shipment_id}")
    def shipment_patch(shipment_id:int,data:ship,session:session=depends(get_session)):
        shipment=session.get(shipment,shipment_id)
        shipment.sqlmodel_update(data.model_dump(exclude_unset=True))
        session.add(shipment)
        session.commit()
        session.refresh(shipment)
        return shipment

    @app.delete("/shipments/{shipment_id}")
    def shipment_delete(shipment_id:int,session:session=depends(get_session)):
        shipment=session.get(shipment,shipment_id)
        session.delete(shipment)
        session.commit()
        return {"message":"shipment deleted successfully"}