from ast import If
from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.refuse_cookie()
        bot.change_currency(currency='usd')
        bot.place_to_go(place="Paris")
        bot.select_when(check_in="2022-05-23", check_out="2022-05-24")
        bot.select_guest(nombre_adult=5)
        bot.submit_search()
        bot.applyfilter()
        bot.report_result()
except Exception as e:
    if "in PATH" in str(e):
        print(
            "please add chromedriver to your PATH \n"
            "Window: \n"
            "   set PATH=%PATH%;C:path-to-your-folder\ \n \n"
            "Linux: \n"
            "   PATH=$PATH:/path/toyour/folder/ \n"
            )
    else:
        raise