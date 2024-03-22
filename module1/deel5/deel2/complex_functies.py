data_woorden = ',kat,konijn,schaap'
separator_teken = ','
position_getal = 3


def get_value(data: str, separator: str, position: int) -> str:
    data = data_woorden
    separator = separator_teken
    position = position_getal
    data = data.split(separator)
    if 0 <= position< len(data):
        data = data[position]
        return data
    else:
        data = None


data = get_value(position_getal,separator_teken,data_woorden)


print(data)



