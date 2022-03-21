def calculate(salary, rate_per_hour, percent_award):
    try:
        return (rate_per_hour * salary) + (percent_award * rate_per_hour * salary)/100
    except TypeError:
        return