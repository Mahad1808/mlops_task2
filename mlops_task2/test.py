from main import mlops
#testing that students don't exceed the limit
mlopsObj = mlops(10)
def test_getTotalStudents():
    assert mlopsObj.getTotalStudents() == 10
#trying to add students
def test_addStudents():
    mlopsObj.addStudents()
    assert mlopsObj.getTotalStudents() == 11
#removal
def test_removeStudents():
    mlopsObj.removeStudents()
    assert mlopsObj.getTotalStudents() == 10

def test_getClassName():
    assert mlopsObj.getClassName() == "MLOPS CS-B"