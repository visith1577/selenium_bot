from book.booking import Booking
import typer_cli.cli as CLI
import typer


app = typer.Typer()


def main():
    try:
        with Booking() as bot:
            bot.get_land_page()
            bot.change_currency()
            CLI.enter_location(bot)
            CLI.select_dates(bot)
            CLI.number_of_adults(bot)
            bot.click_search()
            bot.booking_filterations()
            bot.report_listings()

    except Exception as e:
        if 'in PATH' in str(e):
            typer.echo(
                'You are trying to run the bot from command line \n'
                'Please add to PATH your Selenium Drivers \n'
                'Windows: \n'
                '    set PATH=%PATH%;C:path-to-your-folder \n \n'
                'Linux: \n'
                '    PATH=$PATH:/path/toyour/folder/ \n'
            )
        else:
            raise


if __name__ == '__main__':
    typer.run(main)