from fastapi import APIRouter
from services.service_registry import lesson_service
from global_library_items import global_library_items

router = APIRouter(tags=["lesson"])

def get_lesson_library_items(lesson_id):
    # Placeholder for lesson-specific library items (could fetch from DB or lesson data)
    return []

@router.get("/{lesson_id}")
async def get_lesson(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id)
    return lesson.model_dump()

@router.get("/{lesson_id}/current_node")
async def get_current_node(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id)
    node = lesson_service.get_current_node()
    return node.model_dump()

@router.get("/{lesson_id}/current_node/elements")
async def get_current_node_elements(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id)
    node = lesson_service.get_current_node()
    elements = lesson_service.get_elements_for_node(node.id)
    # Example appState and scrollToContent (customize as needed)
    appState = {
        "viewBackgroundColor": "#AFEEEE",
        "currentItemFontFamily": 5,
    }
    scrollToContent = True
    # Combine global and lesson-specific library items
    libraryItems = global_library_items + get_lesson_library_items(lesson_id)
    return {
        "elements": [el.model_dump() for el in elements],
        "appState": appState,
        "scrollToContent": scrollToContent,
        "libraryItems": libraryItems,
    }

@router.get("/{lesson_id}/next_node")
async def next_node(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id)
    node = lesson_service.get_next_node()
    if node:
        return node.model_dump()
    return {"error": "No next node"}