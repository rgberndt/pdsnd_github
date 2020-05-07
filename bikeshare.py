import time
import pandas as pd
import numpy as np

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "new york": "new_york_city.csv",
    "washington": "washington.csv",
}

MONTH_DATA = ['january',
              'february',
              'march',
              'april',
              'may',
              'june',
              'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        city = input(
            "\nPlease enter city (Chicago, New York, Washington) you whish to analyze: ").lower()
        while city not in ["chicago", "new york", "washington"]:
            city = input("Invalid input, please try again: ").lower()

        # get user input for month (all, january, february, ... , june)
        month = input(
            "\nPlease enter month (january to june) you whish to analyze. \nIf you like to look at all months, please enter 'all': ").lower()
        while month not in ["all", "january", "february", "march", "april", "may", "june"]:
            month = input("Invalid input, please try again: ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input(
            "\nPlease enter day (e.g. monday) you whish to analyze. \nIf you like to look at all days, please enter 'all': ").lower()
        while day not in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            day = input("Invalid input, please try again: ").lower()

        return city, month, day
    except Exception as e:
        print("Error: ", e)
    print('-'*40)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
                # read csv file, with filename from input and CITY_DATA
        df = pd.read_csv(CITY_DATA[city])

        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        # filter by month
        if month != 'all':
                # months list necessary because dt.month returns int
            month = MONTH_DATA.index(month) + 1
            df = df.loc[df['month'] == month, :]

            # filter by day of week
        if day != 'all':
            df = df[df['day_of_week'] == day.title()]

        return df
    except Exception as e:
        print("Error: ", e)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # TO DO: display the most common month
    try:
        month_most = (
            MONTH_DATA[(df['month'].mode().values[0])-1]).capitalize()
        print("The most common month is: " + month_most)

        # TO DO: display the most common day of week
        print("The most common day of the week is: {}".format(
            df['day_of_week'].mode().values[0]))

        # TO DO: display the most common start hour
        df['start_hour'] = df['Start Time'].dt.hour
        print("The most common start hour: {}".format(
            df['start_hour'].mode().values[0]))

    except Exception as e:
        print("Error: ", e)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    try:
        # TO DO: display most commonly used start station
        print("The most commonly used start station is: {} used {} times".format(
            df['Start Station'].mode().values[0], df['Start Station'].value_counts()[0])
        )

        # TO DO: display most commonly used end station
        print("The most commonly used end station is: {} used {} times".format(
            df['End Station'].mode().values[0], df['End Station'].value_counts()[0])
        )

        # TO DO: display most frequent combination of start station and end station trip
        df['combi'] = df['Start Station'] + " to " + df['End Station']
        print("The most frequent combination of start station and end station is: {} driven {} times".format(
            df['combi'].mode().values[0], df.groupby(["Start Station", "End Station"]).size().max())
        )

    except Exception as e:
        print("Error: ", e)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    try:
        df['Travel Time'] = df['End Time'] - df['Start Time']

        # TO DO: display total travel time
        print("The total travel time is: {}".format(df['Travel Time'].sum()))

        # TO DO: display mean travel time
        print("The mean travel time is: {}".format(df['Travel Time'].mean()))

    except Exception as e:
        print("Error: ", e)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print("These are the counts of user types:\n",
              df['User Type'].value_counts())

    # TO DO: Display counts of gender
        print("The counts of gender is:\n", df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest birth year is: ", int(df['Birth Year'].max()))
        print("The most recent birth year is: ", int(df['Birth Year'].min()))
        print("The most common birth year is: ", int(df['Birth Year'].mode()))

    except Exception as e:
        print("Error: ", e)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def display_raw(df):
    watch_raw = input('Would you like to see raw data? yes/no ').lower()
    while watch_raw not in ["yes", "y", "no", "n"]:
        watch_raw = input("Invalid input, please try again: ").lower()
    
    if watch_raw=="yes" or watch_raw=="y":
        while True:
            for i in range(5):
                print(df.iloc[i])
                print()
            watch_raw = input('Would you like to see more? yes/no ').lower()
            while watch_raw not in ["yes", "y", "no", "n"]:
                watch_raw = input("Invalid input, please try again: ").lower()
            if watch_raw=='yes' or watch_raw=='y':
                continue
            elif watch_raw=='no' or watch_raw=='n':
                break
            
    



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
