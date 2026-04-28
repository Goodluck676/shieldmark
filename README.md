ShieldMark 🛡️

"Every dollar you earned, yours."


What Is ShieldMark?
ShieldMark is a transaction integrity system built for small business owners who cannot watch every employee every second.
An employee can charge a customer $200, log $150 in the system, and pocket $50. The owner never knows.
ShieldMark fixes that. It compares what actually happened to what was recorded. If there is a gap — it tells the owner.
The northstar behind every decision:

"The owner should sleep well tonight."


The Problem
Employee skimming fraud is one of the most common and hardest to detect forms of small business theft. It happens quietly, transaction by transaction, until the damage is significant.
Most small business owners do not have the tools to catch it early. ShieldMark is built to change that.

What ShieldMark Does Today

Simulates 10 employees and their transactions
Secretly plants fraud on 2 to 3 employees per run
Validates every amount before touching the math
Compares actual sale amount against logged amount
Flags discrepancies and labels each transaction
Prints a clean report the owner can read instantly

Sample output:
====================================
   SHIELDMARK TRANSACTION REPORT
====================================
Employee: Joseph
Discrepancy: $160
Status: Underreported
ID: emp5
----------------------------------------------------
Employee: Kemi
Discrepancy: $23
Status: Underreported
ID: emp6
----------------------------------------------------
Employee: Shade
Discrepancy: $0
Status: Accurate
ID: emp1
----------------------------------------------------

Architecture
ShieldMark is built on a three-layer architecture:
LAYER 1 — GUARD
validate_amount()
Single job: checks if an amount is a real positive number
Returns: True or False — bad data never reaches the math

LAYER 2 — HELPER
calculate_discrepancy()
Single job: calculates the gap between actual and logged
Returns: float rounded to 2 decimal places

LAYER 3 — COORDINATOR
process_transaction()
Single job: orchestrates the full pipeline
Returns: staff_id, staff_name, discrepancy, status

DATA FACTORY
generate_transactions()
Single job: creates simulated employee transactions
Plants fraud on 2 to 3 employees per run

ENTRY POINT
run_shieldmark.py
Single job: connects the pipeline and prints the owner report

Key Engineering Principles
Every decision in ShieldMark is guided by these principles:

One function one job — no function does more than one thing
Fail fast — bad data is rejected immediately at the Guard layer
Guard before data — garbage in, garbage out
Type before value — check what something is before checking what it contains
Single responsibility — each layer owns exactly one concern


Project Structure
ShieldMark/
│
├── src/
│   ├── validate_amount.py        # Guard, Helper, and Coordinator layers
│   ├── generate_transactions.py  # Data factory
│   └── run_shieldmark.py         # Entry point — run this to see the report
│
└── README.md

How To Run
bashcd src
python run_shieldmark.py

What Is Coming Next
ShieldMark is actively being expanded:
Phase 2 — Linux, Git branching, professional version control
Phase 3 — AWS S3, Lambda, CloudWatch, SNS
          Store logs in the cloud
          Run detection automatically
          Email the owner in real time when fraud is detected
Phase 4 — Docker and GitHub Actions CI/CD
          Automated testing on every commit
          Full deployment pipeline
Real time alerts are coming in Phase 3 via AWS SNS.

About This Project
ShieldMark is a capstone project built by Geraldine — a final semester Computer Science student specializing in Cloud Computing and AWS, graduating May 2026.
Geraldine works full time at PNC Bank where her responsibilities include customer transactions, fraud detection, and incident response. ShieldMark is built on that real world experience.
This project is dedicated to God.

Built with Python · Expanding to AWS · GitHub Actions CI/CD coming soon
