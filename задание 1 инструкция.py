def convert_seconds(seconds):
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"

seconds = int(input("Введите количество секунд: "))
print("Результат:", convert_seconds(seconds))
