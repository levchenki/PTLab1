# -*- coding: utf-8 -*-
import argparse
import sys

from src.CalcRating import CalcRating
from src.StudentController import StudentsController
from src.YAMLDataReader import YAMLDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = YAMLDataReader()

    students = reader.read(path)
    print("Students: ", students)

    calc_rating = CalcRating(students)
    student_ratings = calc_rating.calc()

    print("Rating: ", student_ratings)

    students_with_90_grades = StudentsController(students).get_students_with_rating_equals_90()
    print("Students with rating equals 90: ", students_with_90_grades)

if __name__ == "__main__":
    main()
