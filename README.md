# Trade P&L Service

A full-stack app that ingests CSV trade data and calculates profit & loss (P&L) by strategy.

---

## Quick Start

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Frontend (new terminal)
cd frontend
npm install
npm run dev  # http://localhost:5173
```

---

## Tech Stack

| Component | Technology | Why |
|-----------|-----------|-----|
| **Backend** | FastAPI | Type-safe (Pydantic), ~10x faster (ASGI), auto-docs, CORS |
| **Frontend** | React + Vite | Component-based, hooks, instant HMR |
| **HTTP** | Axios | Cleaner than Fetch, auto JSON |
| **CSV** | Generator | Constant 5MB memory for any size |

---

## Architecture

```
Frontend (React)             Backend (FastAPI)
├─ App.jsx                   ├─ main.py
├─ UploadForm.jsx     ──POST──► routes/upload.py
├─ PnlTable.jsx              ├─ routes/pnl.py ◄──GET──
└─ api.js                    ├─ app/state.py
                             ├─ services/csv_processor.py
                             └─ services/pnl_calculator.py
```

---

## API Endpoints

**POST /upload**: Accepts CSV file, saves to uploads/, updates state
- Response: `{"message": "File uploaded"}`

**GET /pnl**: Calculates P&L by strategy
- Response: `[{"strategy": "momentum", "pnl": 1000.50}, ...]`

---

## CSV Format

```csv
trade_id,strategy,symbol,side,quantity,price
1,momentum,AAPL,buy,100,150.00
2,momentum,AAPL,sell,100,160.00
```

**Required**: strategy, symbol, side (buy/sell), quantity, price

---

## Design Decisions

| Decision | Choice | Why | Limitation |
|----------|--------|-----|-----------|
| State | Global current_file | Simple demo | Only 1 user |
| CSV Processing | Generator (stream) | 5MB RAM for any size | Slightly complex |
| Matching | First buy → first sell | Simple demo | Not FIFO |
| State Mgmt | useState | Shows judgment | Redux for 50+ vars |

---

## Setup

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
# Docs: http://localhost:8000/docs
```

### Frontend

```bash
cd frontend
npm install
npm run dev  # http://localhost:5173
npm run build  # Production
```

---

