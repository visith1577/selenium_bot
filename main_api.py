from fastapi import FastAPI
from datetime import date
from book.booking import Booking
from pydantic import BaseModel

app = FastAPI()

app.post('/')
def enter_data(num_adults: int, location: str, check_in: date, check_out: date):
    return {
        'number_of_adults': num_adults,
        'location': location,
        'check_in': check_in,
        'check_out': check_out
    }


class Data(BaseModel):
    num_adults: int
    location: str
    check_in: date
    check_out: date


app.get('/data')
async def get_results(data: Data):
    try:
        with Booking() as bot:
            bot.get_land_page()
            bot.change_currency()
            bot.enter_location(data.location)
            bot.select_dates(data.check_in, data.check_out)
            bot.number_of_adults(data.num_adults)
            bot.click_search()
            bot.booking_filterations()
            bot.report_listings()

    except Exception as e:
        if 'in PATH' in str(e):
            return {
                "Exception" : 'You are trying to run the bot from command line \n'
                'Please add to PATH your Selenium Drivers \n'
                'Windows: \n'
                '    set PATH=%PATH%;C:path-to-your-folder \n \n'
                'Linux: \n'
                '    PATH=$PATH:/path/toyour/folder/ \n'
            }
        else:
            raise
