# Wireframe and Feature Concepts

This document outlines a simple wireframe and feature breakdown for the Revel TC MVP.  It describes how the web interface could evolve to support transaction coordinators, agents and clients.  These wireframes are conceptual – they are intended to guide future UI/UX design rather than serve as polished mockups.

## Dashboard Page

The dashboard is the home page for agents and coordinators.  It provides an overview of active and closed transactions along with quick actions.

```
┌─────────────────────────────────────────────────────────────────┐
│  Revel TC – Dashboard                                          │
├─────────────────────────────────────────────────────────────────┤
│ [Create New Transaction]   [Upload Contract]                   │
│                                                               │
│  Active Transactions                                          │
│  ┌───────────┬─────────────┬─────────┬─────────────┐           │
│  │ ID        │ Property    │ Status  │ Closing Date │           │
│  ├───────────┼─────────────┼─────────┼─────────────┤           │
│  │ #1        │ 123 Main St │ New     │ 2025‑08‑10   │           │
│  │ #2        │ 456 Elm Rd  │ In Prog │ 2025‑07‑31   │           │
│  │ …         │ …           │ …       │ …            │           │
│  └───────────┴─────────────┴─────────┴─────────────┘           │
│                                                               │
│  Closed Transactions                                          │
│  (collapsed by default)                                       │
└─────────────────────────────────────────────────────────────────┘
```

### Key elements

- **Create New Transaction**: opens a form where the coordinator can enter contract details or upload a document for extraction.
- **Upload Contract**: triggers file selection and sends the PDF/scan to the back‑end for OCR and data extraction.
- **Active Transactions table**: lists current deals with links to detail pages.  Each row displays the transaction ID, property address, status (new, in progress, closed) and closing date.
- **Closed Transactions**: collapsed section containing recently closed deals.

## Transaction Detail Page

Each transaction has a detail view where coordinators and agents manage tasks, documents and communications.

```
┌─────────────────────────────────────────────────────────────────┐
│  Transaction #2 – 456 Elm Road                                │
├─────────────────────────────────────────────────────────────────┤
│  Summary                                                      │
│  Buyer: Jane Doe    Seller: Acme LLC                          │
│  Closing Date: 2025‑07‑31     Status: In Progress             │
│                                                               │
│  Tabs: [Timeline] [Documents] [Tasks] [Messages] [Notes]      │
│                                                               │
│  Timeline View (default)                                      │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ • 2025‑07‑05 – Contract Signed (completed)               │ │
│  │ • 2025‑07‑08 – Inspection scheduled @ 10am (pending)    │ │
│  │ • 2025‑07‑12 – Appraisal due (pending)                  │ │
│  │ • 2025‑07‑31 – Closing date                            │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Tab descriptions

- **Timeline**: chronological list of past and upcoming milestones (inspection, appraisal, financing contingency, closing).  Users can add or edit events.  Overdue items are highlighted.
- **Documents**: shows a file list with version control and upload buttons.  Each document can be previewed or downloaded.  Integration with e‑signature services should allow sending documents for signatures.
- **Tasks**: displays a checklist of tasks with assignees and due dates (e.g., "order title", "send HOA docs", "schedule final walk‑through").  Tasks can be added, assigned and marked complete.
- **Messages**: centralized conversation threads among stakeholders.  Ideally integrates with email/SMS and logs all communications.
- **Notes**: internal notes for coordinators/agents; not visible to clients.

## Future Enhancements

The MVP provides only basic functionality.  Future features could include:

- **User authentication** and role‑based access control (agents, coordinators, clients, vendors).
- **Notifications and reminders** via email, SMS or mobile push.
- **Document templates** and auto‑generated forms for common contracts and disclosures.
- **Analytics dashboard** showing metrics such as average time to close, bottlenecks per phase and agent productivity.
- **Mobile apps** for coordinators and clients to view tasks and deadlines on the go.

This wireframe is meant to serve as a guiding vision.  As more insights are gathered from stakeholders and testing, the design will evolve.