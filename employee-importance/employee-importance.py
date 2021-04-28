"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # looks like a recursive search problem.
        # base case:
        #   employee has no subordinates == return value
        # n case:
        #   employee has subordinates
        #       running sum += getImportance(subordinate)
        tgt_emp = getEmployee(employees, id)
        value = tgt_emp.importance
        for sub in tgt_emp.subordinates:
            subObj = getEmployee(employees, sub)
            if len(subObj.subordinates) == 0:
                value += subObj.importance
            else:
                value += self.getImportance(employees, subObj.id)
        return value
    
# def getTotalValue(employee, empList) -> int:
#     value = employee.value
#     for sub in employees
#     return x

# helper fxn to get an employee.
def getEmployee(employees, id):
    for emp in employees:
        if emp.id == id:
            return emp
        