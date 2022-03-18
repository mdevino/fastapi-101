from fastapi import APIRouter


router = APIRouter(
  prefix='/items'
)

@router.get('/{item_id}')
async def read_item(item_id: int):
  return {'item_id': item_id}