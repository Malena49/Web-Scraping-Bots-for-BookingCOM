from locale import currency
from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.refuse_cookie()
    bot.change_currency(currency='usd')
    bot.place_to_go(place="Paris")
    bot.select_when(check_in="2022-05-19", check_out="2022-05-21")
    bot.select_guest(nombre_adult=5)
    bot.submit_search()