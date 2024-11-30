import yaml

from src.DataReader import DataReader
from src.Types import DataType


class YAMLDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            parsed = yaml.safe_load(file)

            for student in parsed:
                for student_name, subjects in student.items():
                    subjects = [(subject_name, grade) for subject_name, grade in subjects.items()]
                    self.students[student_name] = subjects
            return self.students
