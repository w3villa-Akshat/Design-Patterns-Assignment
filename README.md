 # Tiny Office System (Design Pattern Assignment)

This project demonstrates three design patterns:

1. Singleton – OfficeDatabase  
   Ensures only one database connection exists.

2. Factory – EmployeeFactory  
   Creates different types of employee objects (FullTime, PartTime, Intern).

3. Observer – AttendanceSubject  
   Notifies HR and Security when employee checks in.

## Flow:
Employee Check-In →
   Factory creates employee →
   Singleton database used →
   Observer notifies HR + Security



## Flow Diagram:
                          ┌────────────────────────┐
                          │   Office System Start  │
                          └─────────────┬──────────┘
                                        │
                                        ▼
                       ┌────────────────────────────────┐
                       │   Singleton (OfficeDatabase)   │
                       │  → Only one DB connection      │
                       └────────────────┬───────────────┘
                                        │
                                        ▼
                       ┌────────────────────────────────┐
                       │     Factory (EmployeeFactory)  │
                       │  → Creates employee type        │
                       │    (FullTime/Intern/PartTime)   │
                       └────────────────┬───────────────┘
                                        │
                                        ▼
                       ┌────────────────────────────────┐
                       │ Observer (AttendanceSubject)   │
                       │ → HR + Security auto-notified   │
                       └────────────────┬───────────────┘
                                        │
                                        ▼
                             ┌────────────────────┐
                             │   Employee Check-In │
                             └────────────────────┘
                                        │
                                        ▼
               ┌────────────────────────────────────────────────┐
               │ HRSystemObserver receives notification          │
               └────────────────────────────────────────────────┘
                                        │
                                        ▼
               ┌────────────────────────────────────────────────┐
               │ SecuritySystemObserver receives alert           │
               └────────────────────────────────────────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────────┐
                         │        System Completed        │
                         └───────────────────────────────┘



## How to Run:
python main.py


## Output:


--- SINGLETON DEMO ---
Database Connected
db1 is db2: True

--- FACTORY DEMO ---
Employee 1: Full-Time Employee
Employee 2: Intern Employee

--- OBSERVER DEMO ---
Akshat checked in
[HR] Notification: Akshat just checked in
[Security] Alert: Akshat just checked in