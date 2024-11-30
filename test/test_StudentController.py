import pytest

from src.StudentController import StudentsController
from src.Types import DataType


class TestStudentController:

    @pytest.fixture()
    def input_valid_data_one_student(self) -> DataType:
        one_student: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 76)
            ],
            "Иванов Петр Иванович": [
                ("математика", 90),
                ("химия", 90),
                ("социология", 90)
            ],
            "Никитин Никита Никитич": [
                ("математика", 91),
                ("литература", 89),
                ("социология", 90)
            ],
        }
        return one_student

    @pytest.fixture()
    def input_valid_data_two_students(self) -> DataType:
        one_student: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 90),
                ("химия", 90),
                ("социология", 90)
            ],
            "Иванов Петр Иванович": [
                ("математика", 90),
                ("химия", 90),
                ("социология", 90)
            ],
            "Никитин Никита Никитич": [
                ("математика", 91),
                ("литература", 89),
                ("социология", 90)
            ],
        }
        return one_student

    @pytest.fixture()
    def empty_data(self) -> DataType:
        return DataType()

    @pytest.fixture()
    def input_invalid_data(self) -> DataType:
        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 76)
            ],
            "Иванов Петр Иванович": [
                ("математика", 90),
                ("химия", 80),
                ("социология", 90)
            ],
            "Никитин Никита Никитич": [
                ("математика", 91),
                ("литература", 89),
                ("социология", 90)
            ],
        }
        return data

    def test_init_student_controller(self,
                                     input_valid_data_one_student: DataType):
        controller = StudentsController(input_valid_data_one_student)
        assert input_valid_data_one_student == controller.data

    def test_init_empty_student_controller(self, empty_data: DataType):
        controller = StudentsController(empty_data)
        assert empty_data == controller.data

    def test_one_student(self, input_valid_data_one_student: DataType):
        expected = ['Иванов Петр Иванович']
        controller = StudentsController(input_valid_data_one_student)
        students = controller.get_students_with_rating_equals_90()
        assert students == expected

    def test_two_students(self, input_valid_data_two_students: DataType):
        expected = ['Петров Петр Петрович', 'Иванов Петр Иванович']
        controller = StudentsController(input_valid_data_two_students)
        students = controller.get_students_with_rating_equals_90()
        assert students == expected

    def test_no_students(self, input_invalid_data: DataType):
        expected = []
        controller = StudentsController(input_invalid_data)
        students = controller.get_students_with_rating_equals_90()
        assert students == expected

    def test_no_students_print(self, input_invalid_data: DataType, capsys):
        controller = StudentsController(input_invalid_data)
        controller.get_students_with_rating_equals_90()
        captured = capsys.readouterr()
        assert captured.out == 'No student with average rating equal to 90.\n'
