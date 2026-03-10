# mengimport modul datetime bawaan python
from datetime import datetime, date, timedelta

# mendapatkan tanggal dan waktu saat ini di python
now = datetime.now()


# mendapatkan tanggal saat ini
today = date.today()

# mendapatkan waktu saat ini
current_time = datetime.now().time()

# membuat object tanggal dan waktu
custome_date = datetime(2023, 1, 15)

# format tanggal sebagai string
formated_date1 = today.strftime('%Y-%m-%d')
formated_date2 = today.strftime('%A, %d, %Y')
formated_time1 = current_time.strftime("%I:%M:%S %p")
formated_time2 = current_time.strftime("%H:%M:%S WIB")


next_week = today + timedelta(weeks=1)

print("Tanggal dan Waktu saat ini : ", now)
print("Tanggal hari ini: ", today)
print("Waktu saat ini: ", current_time)
print("Tanggal khusus:", custome_date)
print("Tanggal yang diformat: ", formated_date1)
print("Tanggal yang diformat: ", formated_date2)
print("Jam yang diformat: ", formated_time1)
print("Jam yang diformat", formated_time2)
print("Tanggal satu minggu kedepan: ", next_week)
