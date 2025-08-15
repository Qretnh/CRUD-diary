from typing import Sequence

from db.models.note import Note
from schemas.notes import NoteCreate, NoteUpdate
from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def create_note(session: AsyncSession, note_data: NoteCreate) -> Note:
    note = Note(**note_data.model_dump())
    session.add(note)
    await session.commit()
    await session.refresh(note)
    return note


async def get_note(session: AsyncSession, note_id: int) -> Note | None:
    result = await session.execute(select(Note).where(Note.id == note_id))
    return result.scalars().first()


async def get_notes(session: AsyncSession) -> Sequence[Note] | None:
    result = await session.execute(select(Note))
    return result.scalars().all()


async def update_note(
    session: AsyncSession, note_id: int, note_data: NoteUpdate
) -> Note | None:
    stmt = (
        update(Note)
        .where(Note.id == note_id)
        .values(**note_data.dict(exclude_unset=True))
        .execution_options(synchronize_session="fetch")
    )
    await session.execute(stmt)
    await session.commit()
    return await get_note(session, note_id)


async def delete_note(session: AsyncSession, note_id: int) -> bool:
    stmt = delete(Note).where(Note.id == note_id).returning(Note.id)
    result = await session.execute(stmt)
    await session.commit()
    return bool(result.scalar())


async def mark_done(session: AsyncSession, note_id: int) -> Note | None:
    stmt = update(Note).where(Note.id == note_id).values(is_done=True)
    await session.execute(stmt)
    await session.commit()
    return await get_note(session, note_id)
