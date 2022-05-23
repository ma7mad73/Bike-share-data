import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

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
    city = input('First you\'ve got to choose a city name from (chicago, new york city, washington)\n >>>').lower()
    while city not in CITY_DATA:
        print('Please enter a valid city')
        city = input('First you\'ve got to choose a city name from (chicago, new york city, washington)\n >>>').lower()


    # TO DO: get user input for month (all, january, february, ... , june)

    month = input('please choose a month:(all, january, february, march, april, may, june)\n >>>').lower()
    while month not in months:
        print('Please enter a valid input')
        month = input('please choose a month:(all, january, february, march, april, may, june)\n >>>').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('please choose a day:(all, saturday, sunday, monday, tuesday, wednesday, thursday, friday)\n >>>').lower()
    while day not in days:
        print('Please enter a valid input')
        day = input('please choose a day:(all, saturday, sunday, monday, tuesday, wednesday, thursday, friday)\n >>>').lower()

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    month_number = months.index(month)
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        df = df[df['month'] == month_number]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    df['hour'] = df['Start Time'].dt.hour

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('most common month is: ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('most common day of week is: ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour

    print('most common start hour is: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station is: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('most commonly used end station is: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip

    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    print('most frequent combination of start station and end station trip is: ', df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time: ', df['Trip Duration'].sum().round())

    # TO DO: display mean travel time
    print('average travel time: ', df['Trip Duration'].mean().round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('count of user types: ', df['User Type'].value_counts().to_frame())

    if city != 'washington':

        # TO DO: Display counts of gender
        print('count of genders: ', df['Gender'].value_counts().to_frame())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('earliest year of birth: ', int(df['Birth Year'].min()))
        print('most recent year of birth: ', int(df['Birth Year'].max()))
        print('most common year of birth: ', int(df['Birth Year'].mode()[0]))
    else:
        print('that\'s all the data for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """ Iterates through the raw data by 5 rows at a time"""

    #prompt the user whether they would like want to see the raw data.
    answer = input('would you like to see the first five rows of raw data?(yes/no)\n >>>').lower()
    start = 0

    while True:
        #validating user input
        if answer not in ['yes', 'no']:
            print('Please enter a valid input')
            answer = input('would you like to see five rows of raw data?(yes/no)\n >>>').lower()

        elif answer == 'yes':
            print(df.iloc[start:start+5])
            print('-'*40)
            start += 5

            #checking if there are 5 more rows to display
            if df.shape[0] >= start+5:
                answer = input('would you like to see five more rows of raw data?(yes/no)\n >>>').lower()
            else:
                print('you have reached the end of the rows.')
                break

        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n >>>').lower()
        while restart not in ['yes', 'no']:
            print('Please enter a valid input')
            restart = input('\nWould you like to restart? Enter yes or no.\n >>>').lower()

        if restart == 'no':
            print('thank you')
            break


if __name__ == "__main__":
	main()
