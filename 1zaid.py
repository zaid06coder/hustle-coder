@app.post("/new.skip",response_model=response)
def create_new_shipment(shipments:ship);
    new_id=max (shipments)+1
    new_content={
        "id@app.post("/new.skip", response_model=response)
        "status":"placed",
    }
shipments.update({new_id:new_content})
return[shipments[new_id]]
@app.put("/update"/{sid}")
def update_shipment(sid: int, shipment: dict):
    if sid not in shipments:
        raise exception(create yuor own Exception
                        status_code=HTTP_404_NOT_FOUND,
                        detail="product with the id not found",
                        )
                        shipment[sid]={"id":sid,**data.model_dump(),"status":shipment return shipments[sid]}