from fastapi import APIRouter

fake_items_db = [
  { 'item_name': 'Foo'},
  { 'item_name': 'Bar'},
  { 'item_name': 'Baz'}
]

router = APIRouter(
  prefix='/items'
)

@router.get("/")
async def read_item(skip: int = 0, limit: int = 10):
  return fake_items_db[skip : skip + limit]

@router.get('/{item_id}')
async def read_item(item_id: int):
  return {'item_id': item_id}