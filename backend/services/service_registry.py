from services.lesson_service import LessonService
from services.step_service import StepService
from services.traversal_service import TraversalService
from services.context_service import ContextService
from services.script_generator_service import ScriptGeneratorService
from services.prompt_service import PromptService
from services.narration_service import NarrationService
# from services.rag_service import RAGService

# Instantiate services in dependency order
traversal_service = TraversalService()
step_service = StepService()
prompt_service = PromptService()
# rag_service = RAGService()
context_service = ContextService(traversal_service)
script_generator_service = ScriptGeneratorService(
    prompt_service, traversal_service, context_service
)
lesson_service = LessonService(traversal_service, step_service)
narration_service = NarrationService(script_generator_service)

# Attach lesson_service to traversal_service for context lookups
traversal_service.lesson_service = lesson_service 