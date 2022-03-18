from fastapi import APIRouter


router = APIRouter(
  prefix="/users"
)

@router.get('/me')
async def read_current_user():
  return {'user_id': 'current user'}

@router.get('/{user_id}')
async def read_user(user_id: int):
  return {'user_id': user_id}