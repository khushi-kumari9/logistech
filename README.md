# 🔷 LogisTech — Automated Warehouse Orchestration System (Python)

LogisTech is a Python-based warehouse orchestration system that optimizes storage allocation, automates truck loading, and ensures reliable tracking through SQL persistence.
This project demonstrates backend engineering using **OOP**, **Singleton Pattern**, **Binary Search**, **Backtracking**, **Stacks/Queues**, and **SQL logging**.

---

## 🚀 1. Overview

Modern fulfillment centers process thousands of packages per hour, facing challenges such as:

* Wasted storage space (“shipping air”)
* Item damage due to incorrect bin selection
* Inefficient or incorrect truck loading (LIFO problems)
* Data loss when assignments are not recorded consistently

**LogisTech solves these using structured algorithms and a central controller.**

---

## 🧭 2. System Architecture

### 🕹️ A. Control Tower — Singleton Pattern

`LogiMaster` acts as the single source of truth for:

* Sorted bin inventory
* Package conveyor queue
* Truck loading stack
* SQL database connection

Only one instance can exist to prevent conflicting assignments.

---

### 📦 B. Conveyor Belt — FIFO Queue

Packages arriving at the warehouse are enqueued and processed strictly in arrival order.

---

### 🏗️ C. Loading Dock — LIFO Stack + Rollback

Truck loading is simulated using a stack:

* Last-in-first-out behavior
* Supports `rollback_load()` to reverse loading errors
* Reflects real-world unloading when reordering shipments

---

### 🧠 D. Storage Optimizer

#### 1️⃣ Binary Search — Best-Fit Bin

With thousands or millions of bins, linear scanning is too slow.
Bins are pre-sorted by capacity, and Binary Search identifies the smallest bin that fits a package in **O(log N)** time.

#### 2️⃣ Backtracking — Truck Capacity Planner

Used when several fragile bundles must be loaded together:

* Recursively checks combinations of packages
* Backtracks if truck capacity is exceeded
* Determines whether a grouping is loadable or impossible

---

### 🗄️ E. SQL Logging (Persistence Layer)

Every storage and loading decision is written into a relational database to guarantee recoverability.

**Table: `shipment_logs`**

* `tracking_id`
* `bin_id`
* `timestamp`
* `status`

All writes use try–except blocks to ensure consistency even during crashes.

---

## 🧱 3. Low-Level Design

### 🔹 LogiMaster (Singleton)

Attributes:

* `bin_inventory` — sorted list for binary search
* `conveyor_queue` — FIFO queue
* `loading_stack` — LIFO stack
* `db_connection` — SQLite

### 🔹 StorageUnit (Abstract Class)

Defines:

* `occupy_space(amount)`
* `free_space()`

### 🔹 StorageBin (inherits StorageUnit)

Properties:

* `bin_id`
* `capacity`
* `location_code`

Implements `__lt__` for sorting.

### 🔹 Package

Properties:

* `tracking_id`
* `size`
* `destination`

---

## 📂 4. Project Structure

```
logistech/
│
├── controller/
│   ├── logimaster.py
│   ├── storage_unit.py
│   ├── storage_bin.py
│   ├── package.py
│   ├── algorithms,py
│
│   
│
├── data/
│   ├── schema.py
│   ├──database.py
├── main.py
└── README.md
```

---

## 🧪 5. Running the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your_username>/logistech.git
cd logistech
```

### 2️⃣ Initialize the database

```bash
sqlite3 logistech.db < data/setup.sql
```

### 3️⃣ Run the system

```bash
python main.py
```

---

## ✔️ 6. Evaluation Checklist

* [x] Singleton: Only one controller instance exists
* [x] Binary Search selects optimal bin in O(log N)
* [x] Queue handles package intake (FIFO)
* [x] Stack simulates truck loading (LIFO) + rollback
* [x] SQL persistence logs all actions
* [x] Backtracking correctly validates shipment feasibility

---

## 🎯 7. Future Enhancements

* REST API (FastAPI / Flask)
* Web dashboard for warehouse visualization
* Unit tests using pytest
* Multi-threaded conveyor simulation
* Docker container support

---

## 📘 Summary

LogisTech demonstrates practical backend system design using Python, showing how real-world logistics operations can be modeled using clean OOP structures, efficient algorithms, and reliable state persistence.
