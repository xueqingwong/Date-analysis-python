
# coding: utf-8

# In[1]:


# %load bikeshare.py
import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

days_of_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


# In[2]:


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
        try:        
            city = input("Select a city from {}, {} or {}:".format(*CITY_DATA.keys())).strip().lower()
            if city in CITY_DATA.keys():
                break
            else:
                raise ValueError("mes of error")
        except ValueError:
            print('Please retry')               

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Please enter a month (all, january, february, ... , june)\n').strip().lower()
            if month in months :
                print('Valid month entered')
                break       
            else:
                raise ValueError("mes of error")
        except ValueError:
            print('Please retry')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Please enter a day of the week (all, monday, tuesday, ... sunday)\n').strip().lower()
            if day in days_of_week:
                print('Valid day of week entered')
                break
            else:
                raise ValueError("mes of error")
        except ValueError:
            print('Please retry')
            
    print('-'*40)            
    return city, month, day          


# In[3]:


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

    # extract month, day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # connect Combined Station from Start Station and End Station to create new columns
    df['Combined Station'] = df['Start Station'] + " - " + df['End Station']    
    
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
        df = df[df['day_of_week'] == day.title()]

    return df


# In[4]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common months
    popular_month = df['month'].mode()[0]
    popular_month_name = months[popular_month-1]
    print('The most popular month is {}'.format(popular_month_name.title()))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week is {}'.format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour is {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[5]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df['Combined Station'].mode()[0]
    print('The most popular trip is {}'.format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {} seconds '.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {} seconds'.format(round(mean_travel_time,2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user types count is \n{}'.format(user_types))

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()

        print('The user gender count is \n{}'.format(user_gender))
    except:
        print('Gender data not available\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        print('The earliest birth year is {}'.format(earliest_birth_year))

        most_recent_birth_year = int(df['Birth Year'].max())
        print('The most recent birth year is {}'.format(most_recent_birth_year))

        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print('The most common birth year is {}'.format(most_common_birth_year))
    except:
        print('Birth Year data not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[ ]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
    
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print("City: {}, Month: {}, Day: {}".format(city, month, day))

    # Restart?
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        restart = restart.lower()

        if(restart == "yes"):
            print("Restarting the script...\n")
            main()

        elif(restart == "no"):
            print("Thank You\n")
            return

        else:
            print("Sorry wrong input....\nTerminating....\n")
            return

if __name__ == "__main__":
        main()

