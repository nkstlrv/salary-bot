def calculate_salary(
    total_hours: float,
    b_hours: float,
    beyond_b_hours: float,
    working_days: int,
    fixed_salary: int,
):
    obligatory_hours: int = 6
    per_business_hour: int = 5  # $
    per_beyond_business_hour: int = 15  # $

    basic_hours: float = obligatory_hours * working_days

    average_hours_per_day_total: float = total_hours / working_days
    average_hours_per_day_business: float = b_hours / working_days
    average_hours_per_day_beyond_business: float = beyond_b_hours / working_days

    days_covered_by_basic: float = basic_hours / average_hours_per_day_total

    # Bonus calculation:
    bonus_days: float = working_days - days_covered_by_basic
    bonus_for_b_hours = round(average_hours_per_day_business * bonus_days * per_business_hour, 2)
    bonus_for_beyond_b_hours = round(average_hours_per_day_beyond_business * bonus_days * per_beyond_business_hour, 2)

    result_dict: dict = {
        "basic_hours": round(basic_hours, 2),
        "avarage_hours_total": round(average_hours_per_day_total, 2),
        "avarage_hours_business": round(average_hours_per_day_business, 2),
        "avarage_hours_beyond_business": round(average_hours_per_day_beyond_business, 2),
        "days_covered_basic": round(days_covered_by_basic, 2),
        "bonus_days": round(bonus_days, 2),
        "bonuses_business": bonus_for_b_hours,
        "bonuses_beyond_business": bonus_for_beyond_b_hours,
        "salary": fixed_salary + bonus_for_b_hours + bonus_for_beyond_b_hours
    }

    result = f"""
Total hours: {total_hours}
{b_hours} - during business hours
{beyond_b_hours} - beyond business hours

AVG {result_dict["avarage_hours_total"]} hours per day ({result_dict["avarage_hours_business"]} during bh + {result_dict["avarage_hours_beyond_business"]} beyond bh)
Basic {result_dict["basic_hours"]} hours were completed on: {result_dict["days_covered_basic"]} day of the month
Bonuses are calculated for {result_dict["bonus_days"]} days
({result_dict["avarage_hours_business"]} x {result_dict["bonus_days"]} x ${per_business_hour}) + ({result_dict["avarage_hours_beyond_business"]} x {result_dict["bonus_days"]} x ${per_beyond_business_hour}) = ${result_dict["bonuses_business"]} + ${result_dict["bonuses_beyond_business"]}
Total monthly salary = Fixed salaries + (${result_dict["bonuses_business"]} + ${result_dict["bonuses_beyond_business"]}) 
"""

    print(result)

    return result


if __name__ == "__main__":
    # calculate_salary(total_hours=195.98, b_hours=183.98, beyond_b_hours=11.99, working_days=23, fixed_salary=500)
    calculate_salary(
        total_hours=194.4,
        b_hours=178.5,
        beyond_b_hours=15.9,
        working_days=22,
        fixed_salary=500, )