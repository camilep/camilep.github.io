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
    print('Hello! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Tell me, Which city would you like to explore? We can see Chicago, New York City or Washington...:\n")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Sorry, I can't recognize this city. Please try again")
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Great! Now, We can see some monthly information. Which month would you like to see? (january, february,...,june). \nIf you want to see all the data, please write 'all'...:\n")
        month = month.lower()
        if month in ['january','february', 'march','april','may','june','all']:
            break
        else:
            print("Please, type one month from january to june. If you want to see all the data, type 'all'...:\n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Ok. Now we can see some daily information. Please write a day of the week. But if you want to see all the days, please type 'all'...:\n")
        day = day.lower()
        if day in ['monday','tuesday','wednesday','thursday','friday','all']:
            break
        else:
            print("Please, type one day from the week. If you want to see all the data, type 'all'...:\n")


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
    # 1 Read info from city selected into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # 2 Convert into a datetime the Start Time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # 3 From the Start Time column, select only month and day to create two new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # 4 Filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # Filter by month to create a new dataframe
        df = df[df['month'] == month]

    # 5 Filter by day of week 
    if day != 'all':
        # Filter by day of week to create a new dataframe
        
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month for travel in bikes is (If 1: January, 2: February...): ", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print("The most common day for travel in bikes is: ", df['day_of_week'].mode()[0], "\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour to ride a bike is: ", df['hour'].mode()[0],"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0], "\n")

    # TO DO: display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['Comb Station'] = df['Start Station'] + " " + df['End Station']
    print("The most commonly combination start station is: ", df['Comb Station'].mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is:", df['Trip Duration'].sum(), "minutes\n")

    # TO DO: display mean travel time
    print("The mean travel time is: ", df['Trip Duration'].mean(), "minutes\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print("The counts of user type is: \n",user_types, "\n")
    if city != 'washington':
        
    # TO DO: Display counts of gender
        gen = df.groupby(['Gender'])['Gender'].count()
        print("The counts for gender is: \n",gen,'\n')
   

    # TO DO: Display earliest, most recent, and most common year of birth
    
        earliest_birth = df['Birth Year'].min()
        print(f'The year of earliest birth in the selected data is: {int(earliest_birth)}\n')
        recent_birth = df['Birth Year'].max()
        print(f'The year of most recent birth in the selected data is: {int(recent_birth)}\n')
        common_birth = df['Birth Year'].mode()[0]      
        print(f'The most common birth in the selected data is in the year: {int(common_birth)}\n')
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_raw_data_input(df,i=1):
    see_raw = input('\nIf you like, I can show you some raw data. Would you like to see it? Please enter yes or no\n')
    if see_raw.lower() == 'yes':
        print(df[i:i+5])
        i += 5
        show_raw_data_input(df, i)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_raw_data_input(df)
        restart = input('\nWould you like to restart? Please enter yes or no \n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
