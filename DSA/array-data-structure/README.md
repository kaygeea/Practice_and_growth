# Exercise 1
### Let us say your expense for every month are listed below:
- January - 2200
- February - 2350
- March - 2600
- April - 2130
- May - 2190

### Create a list to store these monthly expenses and using that, find out:
1. Task 1: In Feb, how many dollars you spent extra compare to January
2. Task 2: Find out your total expense in first quarter of the year
3. Task 3: Find out if you spent exactly 2000 dollars in any month.
4. Task 4: June month just finished and your expense is 1980 dollar. Add this item to monthly expense list
5. Task 5: You returned an item that you bought in a month of April, and got a refund of 200$. Make a correction to your monthly expense list based on this.

## Usage:
A function inside the `exercise_1` module created for each task. Given the data set below:
```python
monthly_expenses: List[Dict] = [
    {
        "january": 2200,
        "february": 2350,
        "march": 2600,
        "april": 2130,
        "may": 2190,
    }   
]
```
- **Task 1** - This task can be achieved by calling the `def compare_monthly_expenses()` function, which takes 3 positional arguments:
```python
from exercise_1 import compare_monthly_expenses

compare_monthly_expenses(monthly_expenses, 'february', 'january')
```

- **Task 2** - This task can be achieved by calling the `calc_quarter_one_expense()` function, which takes 1 positional argument:
```python
from exercise_1 import calc_quarter_one_expense

calc_quarter_one_expense(monthly_expenses)
```

- **Task 3** - This task can be achieved by calling the `check_amount()` function, which takes 2 positional arguments:
```python
from exercise_1 import check_amount

check_amount(monthly_expenses, 2000)
```

- **Task 4** - This task can be achieved by calling the `add_expense_record()` function, which takes 3 positional arguments:
```python
from exercise_1 import add_expense_record

add_expense_record(monthly_expenses, "june", 1980)
```

- **Task 5** - This task can be achieved by calling the `update_monthly_expense()` function, which takes 3 positional arguents:
```python
from exercise_1 import update_monthly_expense

update_monthly_expense(monthly_expenses, "april", -200)
```