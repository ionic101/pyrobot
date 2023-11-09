def read_level(level_file_name: str) -> list[list[int]]:
    with open(file=level_file_name, encoding='utf-8') as file:
        return list(map(lambda line: list(line.strip()), file.readlines()))
