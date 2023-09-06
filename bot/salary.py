def calculate_salary(total_hours: float, b_hours: float, beyond_b_hours: float, working_days: int, fixed_salary: int):
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
    bonus_for_b_hours: float = (
            average_hours_per_day_business * bonus_days * per_business_hour
    )
    bonus_for_beyond_b_hours: float = (
            average_hours_per_day_beyond_business * bonus_days * per_beyond_business_hour
    )

    total_monthly_salary: float = fixed_salary + bonus_for_b_hours + bonus_for_beyond_b_hours

    return {

        "business": bonus_for_b_hours,
        "beyond": bonus_for_beyond_b_hours,
        "salary": total_monthly_salary
    }


if __name__ == "__main__":
    calculate_salary(
        total_hours=195.98, b_hours=183.98, beyond_b_hours=11.99, working_days=23, fixed_salary=500
    )
