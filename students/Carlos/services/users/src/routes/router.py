from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/.health")
def health():
    return {"status": "ok"}

@router.post("/")
#usuario creado
def create_user_route ():
    return {
        "message" ,"usuario creado"

    }

@router.put("/{id}")
def update_user_route (id: int):
    # usuario actualizado
    return {
        "id":id,
        "message": "usuario autorizado"

    }
@router.get("/{id}")
def get_user_route (id: int):
    # informacion usuario
    return {
        "id" : id
    }

@router.get("/")
def list_user_route () -> list:

    return [
        {   "id": 123123   }
    ]


