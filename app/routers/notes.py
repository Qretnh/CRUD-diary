from db.connector import get_session
from fastapi import APIRouter, Depends, HTTPException
from logger import logger
from schemas import notes as schemas
from schemas.notes import DeleteResponse
from services.db import notes as services
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND

router = APIRouter(tags=["notes"])


@router.post(
    "/",
    response_model=schemas.NoteRead,
    description="Создать новую заметку в дневнике",
)
async def create_note(
    note: schemas.NoteCreate, session: AsyncSession = Depends(get_session)
):
    new_note = await services.create_note(session, note)
    logger.info(f"Была создана задача №{new_note.id} '{new_note.title}'")
    return new_note


@router.get(
    "/{note_id}",
    response_model=schemas.NoteRead,
    description="Получить заметку по ID",
)
async def read_note(note_id: int, session: AsyncSession = Depends(get_session)):

    db_note = await services.get_note(session, note_id)
    if not db_note:
        logger.info(f"Заметка №{note_id} не найдена")
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Заметка не найдена"
        )
    logger.info(f"Заметка №{note_id} найдена")
    return db_note


@router.get(
    "/",
    response_model=list[schemas.NoteRead],
    description="Получить список всех заметок",
)
async def read_notes(session: AsyncSession = Depends(get_session)):
    notes = await services.get_notes(session)
    logger.info(f"Найдено {len(notes)} заметок")
    return notes


@router.put(
    "/{note_id}",
    response_model=schemas.NoteRead,
    description="Обновить существующую заметку",
)
async def update_note(
    note_id: int,
    note: schemas.NoteUpdate,
    session: AsyncSession = Depends(get_session),
):
    db_note = await services.update_note(session, note_id, note)
    if not db_note:
        logger.info(f"Заметка №{db_note} не найдена")
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Заметка не найдена"
        )
    logger.info(f"Заметка №{db_note.id} успешно обновлена")
    return db_note


@router.delete(
    "/{note_id}",
    description="Удалить уже существующую заметку по ID",
)
async def delete_note(
    note_id: int, session: AsyncSession = Depends(get_session)
):
    deleted = await services.delete_note(session, note_id)
    if not deleted:
        logger.info(f"Заметка {note_id} не найдена для удаления")
        return DeleteResponse(
            status="not_found", detail=f"Заметка с ID={note_id} не существовала"
        )
    logger.info(f"Заметка {note_id} успешно удалена")
    return DeleteResponse(
        status="deleted", detail=f"Заметка с ID={note_id} успешно удалена"
    )


@router.patch(
    "/{note_id}/done",
    response_model=schemas.NoteRead,
    description="Отметить заметку как выполненную",
)
async def mark_done(note_id: int, session: AsyncSession = Depends(get_session)):
    db_note = await services.mark_done(session, note_id)
    if not db_note:
        logger.info(f"Заметка {note_id} не найдена")
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Заметка не найдена"
        )
    logger.info(f"Заметка {note_id} выполнена!")
    return db_note
