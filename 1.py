from sys import argv

script_name, hours, rate_per_hour, prize = argv
print(f"Выработка в час - {hours},\n"
      f"Ставка в час - {rate_per_hour}, \n"
      f"Премия - {prize}, \n"
      f"З/П сотрудника {(int(hours) * int(rate_per_hour)) + int(prize)}")
