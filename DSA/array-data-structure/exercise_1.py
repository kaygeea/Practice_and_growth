from typing import Dict, List

def compare_monthly_expenses(monthly_expenses: List[Dict],
                             month_one: str,
                             month_two: str) -> str:
   """
   Compares difference in expenditure between two months.

   Args:
      monthly_expenses (List[Dict]): A list with the monthly expenditure data.
      month_one (str): Incoming arg for the month to be compared with.
      month_two (str): Incoming arg for the month to be compared against.

   Returns:
      str: A string stating the difference in expenditure between the 2 months.
   """
   month_one_expense: int = monthly_expenses[0][month_one]
   month_two_expense: int = monthly_expenses[0][month_two]

   difference: int = month_one_expense - month_two_expense

   if difference > 0:
      return "You spent ${} more in {} than {}".format(difference, month_one, month_two)
   elif difference < 0:
      str_difference: str = str(difference)[1:]
      return "You spent ${} less in {} than in {}".format(str_difference, month_one, month_two)
   else:
      return "You spent the same amount in {} and {}".format(month_one, month_two)


def calc_quarter_one_expense(monthly_expenses: List[Dict]) -> int | str:
   """
   Calculates the total expense in first quarter of a year.

   Args:
      monthly_expenses (List[Dict]): A list with the monthly expenditure data.

   Returns:
      int | str: The sum of expenses for the first quarter of the year,
                 otherwise an informative string, if len(monthly_expenses) < 2
   """
   total: int = 0

   if len(monthly_expenses[0].values()) > 2:
      for value in list(monthly_expenses[0].values())[:3]:
         total += value
      return "The total quarter 1 expense for this year is ${}".format(total)
   else:
      return ("The first quarter of the year has not yet been completed")
   

def check_amount(monthly_expenses: List[Dict],
                 amount: int
                 ) -> str:
   """
   Checks whether a particular given amount was spent in any given month

   Args:
      monthly_expenses (List[Dict]): A list with the monthly expenditure data.
      amount (int): Incoming argument for the amount to be checked for.
   
   Returns:
      str: Stating whether or not the given amount was spent in a given month.
   """
   list_of_months: str = ""

   for key, value in monthly_expenses[0].items():
      if value == amount:
         list_of_months += ((key + ", "))
   if list_of_months:
      return "Yes! You spent ${} in {}".format(amount, list_of_months[:-2])
   else:
      return "No, you did not spend ${} in any month".format(amount)


def add_expense_record(monthly_expenses: List[Dict],
                       month: str,
                       amount: int
                       ) -> str:
   """
   Adds a new entry to the monthly expense data set

   Args:
      monthly_expenses (List[Dict]): A list with the monthly expenditure data.
      month (str): The name of new month.
      amount (int): The amount spent in the new month.

   Returns:
      List(Dict): The updated monthly expense list, including the new entry.
   """
   if month not in monthly_expenses[0].keys():
      monthly_expenses[0][month] = amount
      print("You added your monthly expense of ${} for {}".format(amount, month))
   else:
      return "Data for the month of {} already exists".format(month)
   return monthly_expenses


def update_monthly_expense(monthly_expenses: List[Dict],
                           month: str,
                           amount: int
                           ) -> List[Dict]:
   """
   Updates stored value of a given month by adding or decuting amount from 

   Args:
      monthly_expenses (List[Dict]): A list with the monthly expenditure data.
      month (str): Name of month whose value is to be updated.
      amount (int): Amount by which the value is to be updated. If the amount
                    is to be deducted from the current value, it should be
                    passed as a negative int.
   """
   old_value = monthly_expenses[0][month]
   new_value = old_value + (amount)
   monthly_expenses[0][month] = new_value

   if new_value > old_value:
      print("The value of your expense for {} just went up by {}".format(month, amount))
   else:
      print("The value of your expense for {} just went down by {}".format(month, amount))
   
   return monthly_expenses