from rich.console import Console
from rich.table import Table
from rich import box
import calendar

console = Console()

yy = 2025
mm = 5

table = Table(title=f"[bold yellow]Calendar - {calendar.month_name[mm]} {yy}[/bold yellow]", box=box.SQUARE)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in days:
    color = "red" if day == "Sun" else "green"
    table.add_column(day, style=color, justify="center")

month_cal = calendar.monthcalendar(yy, mm)

for week in month_cal:
    row = []
    for i, day in enumerate(week):
        if day == 0:
            row.append("")
        elif i == 6:
            row.append(f"[bold red]{day}[/bold red]")
        else:
            row.append(f"[green]{day}[/green]")
    table.add_row(*row)

console.print(table)
