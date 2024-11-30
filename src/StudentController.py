from typing import List

from src.Types import DataType


class StudentsController:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def get_students_with_rating_equals_90(self) -> List[str]:
        students = []
        for student in self.data:
            is_equals_90 = True
            for _, rating in self.data[student]:
                if rating != 90:
                    is_equals_90 = False
                    break
            if is_equals_90:
                students.append(student)
        if len(students) == 0:
            print("No student with average rating equal to 90.")
        return students
