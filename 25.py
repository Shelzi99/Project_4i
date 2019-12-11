# This code shows the no. of births in each country between 1986-2006 and the country with the highest birth-rate.
# and then the no. of births according to sex in each country between 1986-2006
# and prints out a message showing for each country if there were more boys or girls.
def main():

    birth_in_each_state = {}
    boys_girls_in_each_state = {}

    # Checking if the state (from the current line) is in the dictionary
    def check_if_state_in_dict():
        if temp_state in birth_in_each_state:
            return True
        else:
            return False

    def check_if_state_in_dict2():
        if temp_state in boys_girls_in_each_state:
            return True
        else:
            return False

    # Creating two dictionaries: (1) country and the no. of births in each state between the years 1986-2006
    # (2) No. of boys and girtls in each country:
    def accumilate_births_per_state():
        with open('births1.xls', 'r') as data_dict:
            # Ignore first line in the file since it has headers - by reading the the first line and after starting the 'for' loop:
            data_dict.readline()
            for line in data_dict:
                global temp_state
                global temp_births
                global year_of_birth
                # Creating a list from each line:
                fields = line.rstrip().split(',')
                temp_state = fields[1]
                temp_births = int(fields[3])
                year_of_birth = fields[0]
                sex = fields[2]
                temp_births_boy = 0
                temp_births_girl = 0

                # Creating a dictionary I - no. of births in each country between 1986-2006:
                if int(year_of_birth) >= 1986 and int(year_of_birth) <= 2006:

                    if check_if_state_in_dict():
                        # Accumulating the no. of births by adding the temporary no. to the current value (dict.get(value)):
                        birth_in_each_state[temp_state] = temp_births + birth_in_each_state.get(temp_state)
                    else:
                        birth_in_each_state[temp_state] = temp_births

                # Creating dictionary II - including each country and no. of boys and girls:
                if sex == '"boy"':
                    if check_if_state_in_dict2():
                        # Accumulating  no. of 'boy' births in that country:
                        temp_births_boy = temp_births + boys_girls_in_each_state.get(temp_state)[0]
                        boys_girls_in_each_state[temp_state] = [temp_births_boy, temp_births_girl]
                    else:
                        boys_girls_in_each_state[temp_state] = [temp_births, temp_births_girl]
                elif sex == '"girl"':
                    if check_if_state_in_dict2():
                        # Accumulating  no. of 'boy' births in that country:
                        temp_births_girl = temp_births + boys_girls_in_each_state.get(temp_state)[1]
                        boys_girls_in_each_state[temp_state] = [boys_girls_in_each_state.get(temp_state)[0], temp_births_girl]
                    else:
                        birth_in_each_state[temp_state] = [temp_births, temp_births_girl]

    def print_message():
        print('Between the years 1981-2006:')
        for i in boys_girls_in_each_state:
            no_boys = boys_girls_in_each_state.get(i)[0]
            no_girls = boys_girls_in_each_state.get(i)[1]
            if no_boys > no_girls:
                print('In {} there were more boys ({:,}) than girls ({:,})'.format(i, no_boys, no_girls))
            elif no_boys < no_girls:
                print('In {} there were more girls ({}) than boys ({})'.format(i, no_girls, no_boys))
            else:
                print('In {} there were the same no. of girls ({}) and boys ({})'.format(i, no_girls, no_boys))

    accumilate_births_per_state()

    a = max(birth_in_each_state, key=birth_in_each_state.get)
    b = max(birth_in_each_state.values())
    print ('State name and no. of births in each state: ', birth_in_each_state)
    print('\nThe highest no. of births between 1986-2006 was in {} with {:,} births.\n'.format(a, b))
    print (boys_girls_in_each_state)
    print_message()
if __name__ == '__main__':
    main()