# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.YAMLDataReader import YAMLDataReader


class TestYAMLDataReader:

    @pytest.fixture()
    def yaml_file_and_data_content(self) -> tuple[str, DataType]:
        yaml_content = """
                        - Иванов Иван Иванович:
                            математика: 67
                            литература: 100
                            программирование: 91
                        - Петров Петр Петрович:
                            математика: 78
                            химия: 87
                            социология: 76
                        - Иванов Петр Иванович:
                            математика: 90
                            химия: 90
                            социология: 90
                        - Никитин Никита Никитич:
                            математика: 91
                            литература: 89
                            социология: 90
        """
        expected_data = {
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
        return yaml_content, expected_data

    @pytest.fixture()
    def filepath_and_data(self,
                          yaml_file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("test_data.yaml")
        p.write_text(yaml_file_and_data_content[0], encoding='utf-8')
        return str(p), yaml_file_and_data_content[1]

    def test_yaml_read(self,
                       filepath_and_data: tuple[str, DataType]) -> None:
        file_path = filepath_and_data[0]
        data = filepath_and_data[1]
        file_content = YAMLDataReader().read(file_path)
        assert file_content == data
