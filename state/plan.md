---

# 🗓️ **Whiteboard AI Tutor MVP Timeline**

---

## ✅ **Week 1: Core Architecture & Backend Foundation**

### 🎯 Goal: Build the core backend structures (DAG, DLL, commands, narration) and serve them via FastAPI.

#### Tasks:

* [x] Set up FastAPI project + directory structure
* [x] Define LessonNode, StepDLLNode, CommandGroup, WhiteboardCommand, and NarrationEvent in pydantic
* [x] Build static JSON lesson template (e.g., matrix multiplication)
* [x] Write FastAPI routes:

  * GET /lesson/{id} → return DAG + DLL + commands
  * POST /narrate → accept step range, return GPT-generated narration
* [x] Test: create one full LessonNode with a 3–step DLL and command group

#### Deliverables:

* ✅ Working backend that loads and serves a simple DAG lesson + DLL
* ✅ Narration generation endpoint integrated with GPT-4 API
* ✅ JSON lesson file stored locally or loaded via script

---

## ✅ **Week 2: Frontend Whiteboard Renderer + Basic Playback**

### 🎯 Goal: Render whiteboard commands and step through DLL visually

#### Tasks:

* [x] Set up frontend (Next.js or Vite + React + Tailwind)
* [x] Integrate Excalidraw for canvas rendering
* [x] Build:

  * ✅ Whiteboard component (renders commands)
  * ✅ PlaybackController component (tracks DLL step pointer)
* [x] Add step navigation: "Next" and "Back" buttons
* [x] Fetch and parse /lesson/{id} from backend
* [x] Animate draw commands (timed delays, fade-ins)

#### Deliverables:

* ✅ Frontend canvas correctly renders step-by-step whiteboard drawings
* ✅ Clean UI layout with simple controls
* ✅ Backend-fed visuals for a 3-step test lesson

---

## ✅ **Week 3: Narration Integration + DLL ↔ Playback Logic**

### 🎯 Goal: Link narration to drawing; trigger narration events per DLL step group

#### Tasks:

* [x] Add narration playback controller:

  * ✅ Fetch from POST /narrate
  * ✅ Render as text or generate audio
* [x] Add NarrationBox component (displays or plays narration)
* [x] Link narration triggers from DLL steps (e.g., narrate: true)
* [x] Sync narration and drawing step timing (simple fixed delays or manual sync map)
* [x] Begin tracking TraversalHistory locally in frontend

#### Deliverables:

* ✅ Narration and drawing playback are loosely synchronized
* ✅ Narration appears only when narrate=True step is reached
* ✅ Clicking through lesson gives both voice + visuals

---

## ✅ **Week 4: Clarification Handling + Polishing**

### 🎯 Goal: Add basic user clarification + dynamic narration regeneration

#### Tasks:

* [x] Build clarification UI:

  * ✅ Textbox + "Ask" button
* [x] Backend /clarify route:

  * ✅ Takes current TraversalState + question
  * ✅ Uses GPT to generate clarification
* [x] Display new narration + optional visual pointer overlay
* [x] Add NarrationEvent logging + versioning per step
* [x] Track full TraversalHistory (optional: per-step snapshot or hash)

#### Deliverables:

* ✅ User can ask one-off clarification questions
* ✅ Clarification narration is generated and appended to log
* ✅ narration_log and traversal_history are now persistent
* ✅ Frontend polishing: animations, minor bugs, timing refinements

---

## 🔄 **Week 5: Testing, Export, and Polish (In Progress)**

### 🎯 Goal: Stabilize app, add optional transcript/log export and user-friendly polish

#### Tasks:

* [ ] Export full narration log (.txt or chat-like)
* [ ] Build Transcript component to view all utterances
* [ ] Debug backtracking behavior (ensure consistent undo/redo visuals)
* [ ] Pre-generate narration to speed up first-run experience
* [ ] Deploy backend (Render/Fly.io) and frontend (Vercel)
* [ ] User test: sit with 1–2 people and walk through lesson

#### Deliverables:

* 🔄 Clean end-to-end demo with one complete lesson
* [ ] Working chat-like lesson history
* [ ] Basic lesson export or share functionality
* [ ] Hosting-ready MVP

---

## 📦 MVP Deliverable Summary

| Component                               | Status |
| --------------------------------------- | ------ |
| ✅ Structured DAG + DLL lesson engine    | ✔️     |
| ✅ Command-based whiteboard renderer     | ✔️     |
| ✅ Step-by-step drawing + narration sync | ✔️     |
| ✅ GPT-based narration generation        | ✔️     |
| ✅ Traversal tracking + narration log    | ✔️     |
| ✅ Clarification Q&A                     | ✔️     |
| 🔄 Basic UI and hosting                  | 🔄     |

---

## 🎯 **Current Status & Next Steps**

### ✅ **Completed**
- Backend API with all endpoints implemented
- Excalidraw integration with proper element schema
- Frontend components (Whiteboard, PlaybackControls, NarrationBox)
- API service layer with TypeScript types
- Responsive UI with Tailwind CSS

### 🔄 **In Progress**
- End-to-end testing with real lesson data
- CORS configuration for local development
- Error handling and loading states

### 📋 **Next Steps**
1. **Test the full flow**: Start backend, start frontend, test lesson navigation
2. **Add CORS to backend**: Enable CORS for `http://localhost:3000`
3. **Create test lesson**: Build a simple matrix multiplication lesson
4. **Polish UI**: Add animations, improve error handling
5. **Deploy**: Set up hosting for both backend and frontend

---

## 📈 Optional Fast Tracks (If You Have Extra Time)

* RAG chunking of narration log for context-aware clarifications
* Add TTS via ElevenLabs or OpenAI
* Animate transitions between lesson DAG nodes
* Track "is_backtrack" and regenerate narration with a different prompt style
* Add a progress bar or minimap of DAG structure

---

# Plan

## Main Page Redesign
- The main page now displays two buttons: **Load Lesson** and **Generate Lesson**.
  - **Load Lesson** navigates to `/load-lesson`, which contains the Excalidraw implementation (previously on the main page).
  - **Generate Lesson** is present but disabled for now (future feature).
- The Excalidraw content was moved from the main page to a new file: `src/app/load-lesson.tsx`.
- Navigation links were added for user flow between the main page and the lesson loader.

## Rationale
- This change makes the main page a simple entry point for users, allowing for future expansion (e.g., lesson generation, dashboard, etc.).
- The Excalidraw implementation is now accessible via a dedicated route, improving clarity and separation of concerns.

## Next Steps
- Implement the lesson generation feature when ready.
- Further refine navigation and UI as new features are added.