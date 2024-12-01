import time

def wait_for_me(seconds : float) -> None:
    """
    Doesn't pause the script but waits "seconds" for the next line of code to run.
    """
    start = time.time()
    while True:
        if (time.time()) - start >= seconds:
            break
        
def compare_dates(date1,date2) -> tuple|list:
    """
    Given 2 dates format (DD,MM,YYYY), this function returns the latest one.
    
    Requires the dates given to be of type list or tuple with integrers formatted as mentioned.
    """
    if date1[2] < date2[2]:
        return date2
    elif date1[2] > date2[2]:
        return date1
    else:
        if date1[1] < date2[1]:
            return date2
        elif date1[1] > date2[1]:
            return date1
        else:
            if date1[0] < date2[0]:
                return date2
            else:
                return date1

def get_date() -> tuple:
    """
    Returns a tuple with the current dates, format (DD,MM,YYYY).
    
    All values inside the tuple are type integrer.
    """    
    t = time.localtime()
    year, month, day_of_month = t[:3]
    current_date = (day_of_month, month, year)
    return current_date