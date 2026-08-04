def estimate_budget(trip_days, daily_expense):
    return trip_days * daily_expense

# Example usage
if __name__ == '__main__':
    days = 7
    daily_expense = 100
    total_budget = estimate_budget(days, daily_expense)
    print(f'Total estimated budget: ${total_budget}')