import time
import pandas as pd
import numpy as np
from inputs import get_inputs

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    city = get_inputs('Would you like to see data for Chicago, New York, or Washington? \n', cities)

    #get whether the user wants to filter the date by month, day, both or not at all
    while True:
        date_filter = input('Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter \n').lower()
        if date_filter == 'month':
            # TO DO: get user input for month (all, january, february, ... , june)
            month = get_inputs('Which month? January, February, March, April, May, or June? \n', months)
            day = 'all'
            break
        elif date_filter == 'day':
            month = 'all'
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = get_inputs('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? \n', days)
            break
        elif date_filter == 'both':
            month = get_inputs('Which month? January, February, March, April, May, or June? \n', months)
            day = get_inputs('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? \n', days)
            break
        elif date_filter == 'none':
            month = 'all'
            day = 'all'
            break
        else:
            print('Invalid entry')
            continue

    print('-'*40)
    return city, month, day


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
    # load data file for the specified city into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('\nThe Most Popular Month: {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nThe Most Popular Day: {}'.format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe Most Popular Hour: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe Most Popular Start Station: {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe Most Popular End Station: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = 'From '+ df['Start Station'] +' To '+ df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('\nThe Most Popular Trip: {}'.format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal Trip Duration: ', total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('\nAverage Trip Duration: ', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCounts Of User Types:\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print('\nCounts Of User Genders:\n', user_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year Of Birth:\n', earliest_year)
        recent_year = df['Birth Year'].max()
        print('\nMost Recent Year Of Birth:\n', recent_year)
        popular_year = df['Birth Year'].mode()[0]
        print('\nPopular Year Of Birth:\n', popular_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw bikeshare data."""
    row_length = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5
    for i in range(0, row_length, 5):

        user_data_display_perefernce= input('Would you like to explore the data? answer by Yes or No\n').lower()
        if user_data_display_perefernce != 'yes':
            break

        # retrieve and convert data to json format
        # split each json row data
        row_data = df.iloc[i: i + 5]
        print(row_data)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
