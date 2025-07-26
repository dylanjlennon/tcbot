# Revel TC – MVP

This repository contains a **minimum‑viable product (MVP)** for the Revel transaction‑coordination (TC) platform.  The MVP implements a lightweight back‑end API and a simple front‑end to demonstrate how contracts can be ingested and managed through a web interface.  It is intended as a starting point for further development and iteration.

## Goals of the MVP

- Provide a basic REST API for uploading real‑estate contracts and tracking transactions.
- Demonstrate how extracted contract data can be stored and served to clients.
- Provide a minimal user interface (UI) for viewing and creating transactions.
- Establish a foundation for provenance tracking and version control once this repository is connected to a GitHub project.

## Architecture Overview

The MVP uses **FastAPI** for the back‑end server and **Vanilla JavaScript** with HTML/CSS for the front‑end.  This minimal stack keeps dependencies simple while still allowing future migration to a more robust framework (e.g. React or Vue) as the project evolves.

```
revel_tc_mvp/
├── backend/         # FastAPI app and models
│   ├── main.py      # API entry point
│   ├── models.py    # Pydantic models for request/response
│   └── db.json      # Simple JSON “database” for prototype
├── frontend/        # Minimal front‑end
│   ├── index.html   # Transaction dashboard and form
│   ├── script.js    # Client‑side logic
│   └── styles.css   # Basic styling
└── README.md        # This file
```

In a production‑ready application you would replace the JSON “database” with a proper database (e.g. PostgreSQL), implement authentication, and build a modern front‑end.  See the `docs/wireframe.md` file for a conceptual UI and feature roadmap.

## Running the MVP

The MVP requires Python 3.8+ and the `pip` dependencies listed in `backend/requirements.txt`.

### 1. Install dependencies

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Start the back‑end server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.  It exposes the following endpoints:

- `POST /transactions/` – upload a new contract and create a transaction.
- `GET /transactions/` – list all transactions.
- `GET /transactions/{id}` – retrieve a single transaction by ID.

### 3. Open the front‑end

Open the `frontend/index.html` file in a browser.  The page provides a simple form for uploading contract text (simulated contract field) and displays existing transactions.  It communicates with the back‑end API using the Fetch API.

## Next Steps

This MVP is intentionally minimal.  The next iterations should:

1. **Replace the JSON store** with a real database and add models for documents, tasks and users.
2. **Integrate document ingestion** (uploading PDF or DOC files) and extraction (OCR/NLP) services.
3. **Implement authentication and roles** for coordinators, agents, and clients.
4. **Expand the front‑end** with a modern framework, real‐time updates and dashboard widgets.
5. **Add tests** and continuous integration (CI) to ensure reliability as features are added.

See `docs/wireframe.md` for a conceptual wireframe and feature breakdown.