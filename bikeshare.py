import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data! \nWould you like to explore Chicago, New York City or Washington?")

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter name of city to explore: ").lower()
    while city.lower() not in ["chicago","new york city", "washington"]:
        city = input("Your choice of city does not match our available cities. \nPlease try again: ").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter the month to view data for: ").lower()
    while month.lower() not in ["all", "january", "february", "march", "april", "may", "june"]:
        month = input("Please enter a valid month from january to june: ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day of the week: ").title()
    while day.title() not in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "all"]:
        day = input("Please enter a valid day or type 'all' : ").title()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of the week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    # filter by month if applicable

    if month != "all":

        # use the index of the months list to get the corresponding int
        months = [ "january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        #filter by month to create the new dataframe
        df = df[df["month"] == month ]

    # filter by day of week if applicable
    if day != "all":

        # filter by day of week to create a new dataframe
        df = df[df["day_of_week"] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("The most common month is: ", common_month)


    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("The most common day is: ", common_day)


    # TO DO: display the most common start hour
    df["Start_Hour"] = df["Start Time"].dt.hour
    common_hour = df["Start_Hour"].value_counts().idxmax()
    print("The most common start hour is: ", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].value_counts().idxmax()
    print("The most commonly used start station is: ", common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].value_counts().idxmax()
    print("The most commonly used end station is: ", common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination_station = df.groupby(["Start Station", "End Station"]).size().nlargest(1)
    print("The most frequent used combination of start station and end station is: ", frequent_combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    total_travel_time_hours = total_travel_time // 3600
    total_travel_time_remainder = total_travel_time % 3600
    total_travel_time_minutes = total_travel_time_remainder // 60
    total_travel_time_seconds = total_travel_time_remainder % 60
    print("Total travel time is:\n", total_travel_time_hours, "hours\n", total_travel_time_minutes, "minutes\n", total_travel_time_seconds, "seconds")


    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    mean_travel_time_hours = mean_travel_time // 3600
    mean_travel_time_remainder = mean_travel_time % 3600
    mean_travel_time_minutes = mean_travel_time_remainder // 60
    mean_travel_time_seconds = mean_travel_time_remainder % 60
    print("Mean travel time is:\n", mean_travel_time_hours, "hours\n", mean_travel_time_minutes, "minutes\n", mean_travel_time_seconds, "seconds")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df["User Type"].value_counts()
        print("Counts for each user type     is:\n{}".format(user_types))
    except:
        print("The user count is: Oops! There are no user categories to count")


    # TO DO: Display counts of gender
    try:
        gender_count = df["Gender"].value_counts()
        print("The gender count is:\n{}".format(gender_count))
    except KeyError:
        print("The gender count is: Oops! no data for gender")



    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df["Birth Year"].min()
        print("The earliest year of birth is:", earliest_year_of_birth)
    except:
        print("Oops! sorry no data avaliable for earliest year of birth")

    try:
        recent_year_of_birth = df["Birth Year"].max()
        print("The most recent year of birth is:", recent_year_of_birth)
    except:
        print("Oops! sorry no data avaliable for most recent year of birth")

    try:
        common_year_of_birth = df["Birth Year"].mode()[0]
        print("The most common year of birth is:", common_year_of_birth)
    except:
        print("Oops! sorry no data avaliable for most common year of birth")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def data_display_mode(df):
    """ display five rows of data and ask user to add more five 5 rows.
    continue till user type 'no'
    """
    print("Would you like to view raw data?\nNote that raw data will be displayed 5 rows at a time and you just need to press 'enter' to view next 5 rows.  ")
    data_display = 0

    while ( input("Click 'enter' to continue to view raw data or type 'no' to quit : ") != "no"):
        data_display += 5
        print(df.head(data_display))




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_display_mode(df)

        restart = input('\nWould you like to restart? Enter yes or no: \n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
