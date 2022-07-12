from fastapi import APIRouter

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
def get_users_list():
    return [{'id': 1}, {'id': 2}]