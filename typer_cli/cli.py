import typer


def enter_location(bot):
    loc = typer.prompt("please enter the location you want to visit.....")
    typer.echo(f"You chose {loc}")
    bot.enter_location(loc)


def select_dates(bot):
    check_in = typer.prompt("Enter check in (dates should be between the current & nex month) yyyy-mm-dd format")
    check_out = typer.prompt("Enter check out dates")
    typer.echo(f"You choose {check_in} to {check_out}")
    bot.select_dates(check_in, check_out)


def number_of_adults(bot):
    num = typer.prompt("Enter number of adults")
    typer.echo(f"booking for {num} adults ")

    bot.number_of_adults(int(num))