import time
import os

def countdown(user_time):
    try:
        if not isinstance(user_time, int) or user_time <= 0:
            raise ValueError("Time should be a positive integer.")
        
        while user_time >= 0:
            mins, secs = divmod(user_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)
            user_time -= 1

            # Clear previous output for smoother countdown display
            clear_output()

        print("\nLiftoff! Countdown finished.")
    except ValueError as ve:
        print(f"Error: {ve}")

def clear_output():
    # Function to clear the previous output from the terminal/console
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    try:
        user_time = int(input("Enter the countdown time in seconds: "))
        countdown(user_time)
    except ValueError:
        print("Error: Invalid input. Please enter a valid positive integer.")
