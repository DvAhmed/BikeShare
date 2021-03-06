import time
import pandas as pd
import numpy as np
Cities = ['chicago' , 'new york city', 'washington']
Months = ['january' , 'february', 'march' , 'april' , 'may' , 'june' , "all" ]
Days = ['monday' , 'tuesday', 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday', "all"]

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
    while True :
        city = input ("Frist Choose a City: ").lower()
        if city not in  CITY_DATA :                                      
            print ("Invalid City!!!")
        else :
            break
           
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month = input ("Choose a Month: ").lower()
        if month != "all" and month not in  Months :                                      
            print ("Invalid Month!!!")
        else :
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)         
    while True :
        day = input ("Choose a Day: ").lower()
        if day != "all" and day not in  Days :                                      
            print ("Invalid Day!!!")
        else :
            break

    print('='*50)
    return city,month,day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= pd.read_csv(CITY_DATA[city])
    df["Start_Time"] = pd.to_datetime (df["Start Time"])  
    df["month"] = df["Start_Time"].dt.month  
    df["day_of_week"] = df["Start_Time"].dt.weekday_name
    if month != "all" :
        months_list = ['january' , 'february', 'march' , 'april' , 'may' , 'june']
        month = months_list.index(month)+1
        df = df [df["month"] == month]        
    if day != "all" :
        df = df [df["day_of_week"] == day.title()]        

    return df


def disply_data(df) :
    j = 0
    row_data = input ("Would you like to eplore 5 rows data?: ").lower()
    pd.set_option ("display.max_columns", None)   
    while True :
        if row_data == "no" :
            break 
        print (df.iloc[j:(j+5)])
        row_data = input("Would you like to eplore 5 rows data?: ").lower()
        j = j+1


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print(f"Data shows that,The most common month is {common_month}")

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print(f" Data shows that ,The most common day is {common_day}")

    # TO DO: display the most common start hour
    common_start_hour = (df["Start_Time"].dt.hour).mode()[0]
    print(f"Data shows that,The most common start hour is {common_start_hour}")           

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print(f"Data shows that,The most common start station is {common_start_station}") 

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print(f"Data shows that,The most common end station is {common_end_station}") 

    # TO DO: display most frequent combination of start station and end station trip
    df['c_trip'] = df['Start Station'] + df['End Station']
    common_trip = df['c_trip'].mode()[0]
    print(f"Data shows that,The most common end station is {common_trip}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(f"Data shows that,The total travel time is {total_travel_time}") 

    # TO DO: display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    print(f"Data shows that,The average travel time is {average_travel_time}") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_type = df["User Type"].value_counts()

    # TO DO: Display counts of gender
    if "Gender" in df :
        print (f"Data shows that ,Count of gender {count_of_user_type}")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df :
        earliest_year_of_birth = int(df["Birth Year"].min())
        print (f"Data shows that,The earliest year of birth {earliest_year_of_birth}")
        recent_year_of_birth = int(df["Birth Year"].max())
        print (f"Data shows that,The recent year of birth {recent_year_of_birth}")
        common_year_of_birth = int(df["Birth Year"].mode()[0])
        print (f"Data shows that,The common year of birth {common_year_of_birth}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def main():
    while True:
        city, month ,day = get_filters()
        df = load_data(city, month ,day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disply_data(df)
                                   

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
