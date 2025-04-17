def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers

def main():
    miles = float(input('Enter the number of miles: '))
    kilometers = miles_to_kilometers(miles)
    print(f'You have {miles} miles, which is {kilometers} kilometers.')

main()
