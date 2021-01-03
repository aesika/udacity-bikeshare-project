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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ("\n Which city would you like to filter by? Chicago, New York City or Washington? \n").lower()
        if city not in ('chicago' , 'new york city' , 'washington'):
            print("Sorry, I did not get it. Please try again.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(" \n Which month would you like filter by? January, February, March, April, May, June? or type 'all' if you don't want a specific month. \n").lower()
        if month not in ('january' , 'february' , 'march' , 'april' , 'may' , 'june' , 'all'):
            print("Sorry, I did not get it. Please try again.")
            continue
        else:
            break
            
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n Which day would you like to filter by? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday? or type 'all' if you don't want a specific day. \n").lower()
        if day not in ('saturday' , 'sunday' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'all'):
            print("Sorry, I did not get it. Please try again.")
            continue
        else:
            break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['week_day'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month = df['month'] .mode()[0]
    print('The most common month is:' , common_month) 

    # TO DO: display the most common day of week
    common_day = df['week_day'] .mode()[0]
    print('The most common day is:' , common_day)   

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is:' , common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is:' , start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is:' , end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_stations = df.groupby(['Start Station' , 'End Station']).count()
    print('The most frequent combination of start&end station is:' , start_station , " & " , end_station)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('The total travel time is:' , total_travel_time/60 , "minutes")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is:' , mean_travel_time/60 , "minutes")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types are: \n' , user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types are: \n' , gender_types)
    except KeyError:
        print("\nGender Types: \n Gender data is not available for this month.")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('\nEarliest year of birth:' , earliest_birth_year)
    except KeyError:
        print("n\Birth year data is not available for this month.")
    try:
        most_recent_birth_year = df['Birth Year'].max()
        print('\nMost Recent year of birth:' , most_recent_birth_year)
    except KeyError:
        print("n\Birth year data is not available for this month.")
        
    try:
        most_common_birth_year = df['Birth Year'].value_counts().idxmax()
        print('n\Most common birth year:' , most_common_birth_year)
    except KeyError:
        print("n\Birth year data is not available for this month.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    
    print(df.head())
    next = 0
    
    while True:
        view_raw_data = input('\nDy you want to see more 5 lines of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            view_raw_data = input('\nDo you want to see 5 lines of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
                
            display_raw_data(df)
            break
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
