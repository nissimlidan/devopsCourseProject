
def tic_tac_toe_choose():
    acceptable_values = range(0,10)
    within_range = False
    user_input = 'test'
    while (user_input.isdigit() == False or within_range == False):
        #user_input = input('You entered an incorrect value, please try again, Please enter number between(0-9)')
        user_input = input('Please enter number between(0-9)')
        if user_input.isdigit() == False:
            print('You entered an incorrect value, please try again')
        if user_input.isdigit() == True:
            if(int(user_input) in acceptable_values):
                within_range = True
            else:
                print('You entered an value that not in range of 0-9, please try again')
                print('test')



tic_tac_toe_choose()


# row1 = ['_', '_', '_']
# row2 = ['_', '_', '_']
# row3 = ['_', '_', '_']
#
# position_row_input = input("Choose an row number from 0 to 2")
# position_row_input = int(position_row_input)
# for i in range(0,1):
#     row1[position_row_input] = 'X'
#     print(row1)
#     print(row2)
#     print(row3)

#position_row_input = input("Choose an row number from 0 to 2")
#position_col_input = input("Choose an colume number from 0 to 2")
#print(position_row_input , position_col_input)