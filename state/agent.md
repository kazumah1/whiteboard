---

# 🧑‍💻 Whiteboard AI Tutor — Agent Plan & Progress

## Quick Status Summary

- **Models:** [x] Defined (minimal logic)
- **Services:** [ ] Mostly stubs/pseudocode
- **Prompts:** [x] Present
- **Routes:** [ ] Minimal/incomplete
- **Frontend:** [ ] Not started

---

## Service Responsibility Map

> **Purpose:** This map defines the clear boundaries and responsibilities for each backend service. Use it to avoid logic bleed and keep the codebase maintainable and testable.

### **LessonService**
**Responsibilities:**
- Load, save, and manage lesson structures (DAG of LessonNodes)
- Handle high-level lesson traversal (moving between concepts/branches)
- Provide access to the current lesson node and its DLL
- Expose lesson-level operations to the API layer

**Should NOT:**
- Handle step-by-step traversal within a concept (leave to StepService)
- Generate narration or context (leave to NarrationService/ContextService)

**Interacts with:** StepService, TraversalService

---

### **StepService**
**Responsibilities:**
- Traverse DLL of steps within a LessonNode (next/prev step, jump, etc.)
- Execute, undo, or redo step actions (whiteboard commands)
- Manage current step pointer within a concept

**Should NOT:**
- Handle lesson-level traversal (leave to LessonService)
- Generate narration or context

**Interacts with:** LessonService, TraversalService

---

### **TraversalService**
**Responsibilities:**
- Track and update the user's traversal state (current node/step)
- Maintain traversal history for undo/redo
- Provide state snapshots for context/narration

**Should NOT:**
- Directly manipulate lesson or step data (should work with models/services)
- Generate narration or context

**Interacts with:** LessonService, StepService, ContextService

---

### **NarrationService**
**Responsibilities:**
- Generate narration for a given step (using ScriptGeneratorService)
- Handle clarification requests (using context and LLM)
- Format and log narration events

**Should NOT:**
- Traverse lessons or steps
- Assemble context (leave to ContextService)
- Call LLM directly (use ScriptGeneratorService)

**Interacts with:** ContextService, ScriptGeneratorService

---

### **ContextService**
**Responsibilities:**
- Gather all relevant context for narration/clarification (previous steps, board state, etc.)
- Format context for prompt filling

**Should NOT:**
- Generate narration or clarification (leave to NarrationService)
- Traverse lessons/steps (should use TraversalService)

**Interacts with:** TraversalService, RAGService

---

### **ScriptGeneratorService**
**Responsibilities:**
- Fill prompt templates and call the LLM API
- Return generated text for narration or clarification

**Should NOT:**
- Assemble context (leave to ContextService)
- Traverse lessons/steps

**Interacts with:** PromptService, RAGService

---

### **PromptService**
**Responsibilities:**
- Load and provide prompt templates
- Fill templates with provided variables

**Should NOT:**
- Call LLM API
- Assemble context

**Interacts with:** ScriptGeneratorService

---

### **RAGService**
**Responsibilities:**
- Retrieve relevant context chunks for RAG-based clarifications

**Should NOT:**
- Generate narration or clarification
- Traverse lessons/steps

**Interacts with:** ContextService, ScriptGeneratorService

---

> **Tip:** If you find yourself writing code in a service that doesn't fit its responsibilities above, refactor it to the correct service or create a new one if needed.

---

## 1. Project Overview

This project is an AI-powered whiteboard tutor. The backend is built with FastAPI and Pydantic models, designed to serve lessons as a DAG (Directed Acyclic Graph) of concepts, each with a DLL (Doubly Linked List) of whiteboard steps and narration events. The frontend (to be built) will render these lessons, allow stepwise playback, and support narration and clarifications via LLM.

---

## 2. Current State (as of latest code review)

- **Models:** [x] Pydantic models for lessons, steps, commands, narration, etc. are defined. They are mostly data containers with minimal logic.
- **Services:** [ ] Service classes exist for narration, script generation, lesson management, context, etc. Most methods are stubs or pseudocode with TODOs.
- **Prompts:** [x] Prompt templates for narration and clarification are present.
- **Routes:** [ ] Backend routes are minimal or not fully implemented.
- **Frontend:** [ ] Not started.

---

## 3. MVP Plan vs. Current State

| Component                               | Status (Now) | Needs Work? |
| --------------------------------------- | ------------ | ----------- |
| Structured DAG + DLL lesson engine      | [x] Defined, [ ] Logic | Yes         |
| Command-based whiteboard renderer       | [ ]          | Yes         |
| Step-by-step drawing + narration sync   | [ ]          | Yes         |
| GPT-based narration generation          | [ ] Pseudocode| Yes         |
| Traversal tracking + narration log      | [ ] Pseudocode| Yes         |
| Clarification Q&A                       | [ ] Pseudocode| Yes         |
| Basic UI and hosting                    | [ ]          | Yes         |

---

## 4. Backend Task Breakdown

### **A. Core Logic & Data**
- [x] Define Pydantic models for lessons, steps, commands, narration, etc.
- [ ] Implement full traversal logic for lessons (DAG/DLL navigation, step execution, undo/redo, branching).
- [ ] Implement persistent lesson loading (from file or DB, not just hardcoded in service).
- [ ] Complete all TODOs in services:
    - [ ] Context assembly (gather all info for LLM prompts)
    - [ ] Board state and previous context extraction
    - [ ] RAG (retrieve relevant context for clarifications)
    - [ ] Narration and clarification generation (LLM API calls, prompt filling)
    - [ ] Traversal history and narration log persistence
- [ ] Implement and test all FastAPI endpoints:
    - [ ] `GET /lesson/{id}`: Return full lesson structure (DAG, DLL, commands)
    - [ ] `POST /narrate`: Accept step range, return narration
    - [ ] `POST /clarify`: Accept traversal state + question, return clarification
- [ ] Create a full test lesson (3+ steps, with narration and commands)
- [ ] Ensure endpoints return correct, complete data for frontend

### **B. Testing & Polish**
- [ ] Add unit/integration tests for lesson traversal, narration, and clarification
- [ ] Add error handling and validation
- [ ] Prepare for deployment (env vars, config, etc.)

---

## 5. Frontend Task Breakdown

### **A. Setup & Core Components**
- [ ] Scaffold frontend project (React/Next.js or Vite + React + Tailwind)
- [ ] Integrate `react-konva` (or similar) for canvas rendering
- [ ] Build Whiteboard component (renders commands step-by-step)
- [ ] Build PlaybackController component (tracks DLL step pointer, Next/Back buttons)
- [ ] Fetch and parse `/lesson/{id}` from backend
- [ ] Animate draw commands (timed delays, fade-ins)

### **B. Narration & Clarification**
- [ ] Add NarrationBox component (displays or plays narration)
- [ ] Add narration playback controller (fetch from `POST /narrate`)
- [ ] Link narration triggers from DLL steps (e.g., `narrate: true`)
- [ ] Sync narration and drawing step timing (simple fixed delays or manual sync map)
- [ ] Build clarification UI (textbox + “Ask” button)
- [ ] Display new narration + optional visual pointer overlay
- [ ] Track TraversalHistory locally in frontend

### **C. Polish & Optional**
- [ ] Export full narration log (txt or chat-like)
- [ ] Build Transcript component to view all utterances
- [ ] Debug backtracking behavior (ensure consistent undo/redo visuals)
- [ ] Pre-generate narration to speed up first-run experience
- [ ] Deploy backend (Render/Fly.io) and frontend (Vercel)
- [ ] User test: walk through lesson with real users

---

## 6. Prioritized Action Plan

### **Backend First Steps**
1. **Implement lesson traversal and state management logic** (DAG/DLL, undo/redo, branching)
2. **Finish narration and clarification generation** (LLM API, prompt filling, context assembly)
3. **Wire up all FastAPI endpoints** for lesson, narration, and clarification
4. **Make lesson loading dynamic** (from file or DB)
5. **Test with a full lesson** (3+ steps, narration, commands)

### **Frontend First Steps**
1. **Scaffold frontend project** (React/Next.js or Vite)
2. **Build whiteboard renderer and playback controls**
3. **Connect to backend endpoints** and render lesson data
4. **Implement narration and clarification UI**
5. **Test end-to-end flow** (drawing, narration, clarification)

---

## 7. Next Steps (Immediate TODOs)

- [ ] Backend: Complete traversal, narration, and clarification logic
- [ ] Backend: Implement and test all endpoints
- [ ] Frontend: Scaffold project and build whiteboard/playback UI
- [ ] Frontend: Connect to backend and test lesson flow

---

## 8. Notes
- The current codebase is a solid skeleton, but most core logic and all frontend work remain to be implemented.
- Use this agent.md as a living document—update as you make progress or encounter new issues.

--- 