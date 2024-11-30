# Лабораторная работа №1 по дисциплине "Технологии программирования"

## Знакомство с системой контроля версий Git и инструментом CI/CD GitHub Actions

### Цели работы:

1. Познакомиться c распределенной системой контроля версий кода Git и ее функциями;
2. Познакомиться с понятиями «непрерывная интеграция» (CI) и «непрерывное развертывание»
   (CD), определить их место в современной разработке программного обеспечения;
3. Получить навыки разработки ООП-программ и написания модульных тестов к ним на
   современных языках программирования;
4. Получить навыки работы с системой Git для хранения и управления версиями ПО;
5. Получить навыки управления автоматизированным тестированием программного обеспечения, расположенного в системе Git, с
   помощью инструмента GitHub Actions.

### 9 вариант
Формат входного файла - YAML.

Необходимо определить и вывести на экран студента, имеющего 90 баллов по всем дисциплинам. Если таких студентов несколько, нужно
вывести любого из них. Если таких студентов нет, необходимо вывести сообщение об их
отсутствии.

### UML-диаграмма

```mermaid
    classDiagram
   class DataReader {
      +read(self, path: str) DataType
   }

   class TextDataReader {
      -key: str
      -students: DataType
      +read(self, path: str) DataType
   }

   class YAMLDataReader {
      -students: DataType
      +read(self, path: str) DataType
   }

   class TestYAMLDataReader {
      +yaml_file_and_data_content(self) tuple[str, DataType]
      +fileth_and_data(self, yaml_file_and_data_content: tuple[str, DataType], tmpdir) tuple[str, DataType]
      +test_yaml_read(self, filepath_and_data: tuple[str, DataType]) None
   }

   class TestTextDataReader {
      +file_and_data_content(self) tuple[str, DataType]
      +fileth_and_data(self, yaml_file_and_data_content tuple[str, DataType], tmpdir) tuple[str, DataType]
      +test_read(self, filepath_and_data: tuple[str, DataType]) None
   }

   DataReader <|-- YAMLDataReader
   TestTextDataReader ..> TextDataReader
   TestYAMLDataReader ..> YAMLDataReader
   DataReader <|-- TextDataReader
```

```mermaid
    classDiagram
    class CalcRating {
        -data: DataType
        -rating: RatingType
        +calc(self) RatingType
    }

    class StudentsController {
        -data: DataType
        +get_students_with_rating_equals_90(self) list[str]
    }

    class TestCalcRating {
        +input_data(self): tuple[DataType, RatingType])
        +test_init_calc_rating(self, input_data: tuple[DataType, RatingType]) None
        +test_calc(self, input_data: tuple[DataType, RatingType]) None
    }

    class TestStudentsController {
        +input_valid_data_one_student(self) DataType
        +input_valid_data_two_students(self) DataType
        +empty_data(self) DataType
        +input_invalid_data(self) DataType
        +test_init_student_controller(self, input_valid_data_one_student: DataType) None
        +test_init_empty_student_controller(self, empty_data: DataType) None
        +test_one_student(self, input_valid_data_one_student: DataType) None
        +test_two_students(self, input_valid_data_two_students: DataType) None
        +test_no_students(self, input_invalid_data: DataType) None
        +test_no_students_print(self, input_invalid_data: DataType, capsys) None
    }

    TestCalcRating ..> CalcRating
    TestStudentsController ..> StudentsController
```