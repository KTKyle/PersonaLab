from fastapi import APIRouter

router = APIRouter(prefix="/personas", tags=["Personas"])


@router.post("/")
def create_persona():
    return {"message": "Create persona endpoint"}


@router.get("/")
def list_personas():
    return {"message": "List personas endpoint"}


@router.get("/{persona_id}")
def get_persona(persona_id: int):
    return {"message": f"Get persona {persona_id}"}


@router.put("/{persona_id}")
def update_persona(persona_id: int):
    return {"message": f"Update persona {persona_id}"}


@router.delete("/{persona_id}")
def delete_persona(persona_id: int):
    return {"message": f"Delete persona {persona_id}"}

@router.get("/health")
async def health_check():
    return {"status": "ok"}