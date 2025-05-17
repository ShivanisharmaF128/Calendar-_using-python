#📅 Calendar Display App Using Python
A visually enhanced calendar application built with Python and the Rich library. This project prints a beautiful and color-coded calendar for any given month and year in the terminal. Perfect for beginners exploring Python scripting, terminal UI design, and date-time operations.


![IMAGE ](https://github.com/ShivanisharmaF128/Calendar-_using-python/blob/main/output.jfif)

---

## 📌 Objective
The goal of this project is to create a visually structured calendar that enhances readability using terminal styling. It helps learners understand how to use:
-The calendar module
-Terminal formatting with rich
-Logic building for displaying dates

---

## 📝 Overview
-📆 Displays any month of a selected year in a table format
-🎨 Uses rich to add colors and a neat box border
-🟨 Highlights month and year in yellow
-🟩 Colors weekdays (Mon–Sat) in green
-🟥 Highlights Sundays in red
-🧪 Clean and user-friendly CLI output

---
## Code
```sh
python --version
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


```
---
## 📜 Code Explanation
-**calendar.monthcalendar()** generates the structure of the month.
-**rich.table.Table()** helps design a formatted, colorful table.
-Coloring logic makes Sunday red and weekdays green.
-Custom box styling gives it a clean framed look.

---

## 📢 Conclusion
This calendar project is a practical and fun way to learn how to combine Python logic with styled terminal output. You can extend this project to:
-Take dynamic input from the user
-Highlight the current date
-Show events or holidays

---
### 🤝 Contribution
Contributions are always welcome!
If you want to improve the UI or add new features, follow these steps:

- Fork this repository 📌
- Make necessary changes 🛠️
- Create a pull request 🔄

----


## 👨‍💻 Author

  Shivani Sharma
  
📌 Passionate about Python, Data Science, and GUI Development.

🌐 Connectact : shivanisharmaf128@gail.com 
