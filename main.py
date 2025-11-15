from singleton.OfficeDatabase import OfficeDatabase
from factory .EmployeeFactory import EmployeeFactory
from observer.attendance import AttendanceSubject, HRSystemObserver, SecuritySystemObserver


if __name__ == "__main__":

    print("\n--- SINGLETON DEMO ---")
    db1 = OfficeDatabase.get_instance()
    db2 = OfficeDatabase.get_instance()
    print("db1 is db2:", db1 is db2)   # True

    print("\n--- FACTORY DEMO ---")
    factory = EmployeeFactory()
    emp1 = factory.create_employee("fulltime")
    emp2 = factory.create_employee("intern")

    print("Employee 1:", emp1.info())
    print("Employee 2:", emp2.info())

    print("\n--- OBSERVER DEMO ---")
    subject = AttendanceSubject()
    subject.add_observer(HRSystemObserver())
    subject.add_observer(SecuritySystemObserver())

    subject.employee_check_in("Akshat")
