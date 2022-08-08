# -*- coding: utf-8 -*-


def max_profit_calculator(File_name):
    
    data = []



    with open(File_name) as file:
        lines = file.readlines()

    for index in range(1,len(lines)):
        line = lines[index]
        parts = line.split(",")
        data.append((parts[0],float(parts[2]),float(parts[3])))

    best_profit = 0
    sell_date_index = 0
    buy_date_index = 0


    for index in range(len(data)):
        buy_day = data[index][0]
        buy_price = data[index][2]
        for i in range(len(data)):
            sell_day = data[i][0]
            sell_price = data[i][1]
            profit = sell_price - buy_price
            if profit > best_profit:
                best_profit = profit
                buy_date_index = index
                sell_date_index = i
    buy_day = data[buy_date_index][0]
    sell_day = data[sell_date_index][0]
    buy_price = data[buy_date_index][2]
    sell_price = data[sell_date_index][1]



    print("Reading Data ...")
    print("*"*40)
    message = "The maximum profit is {:.2f} per share"
    print(message.format(best_profit))
    print("")
    buy_on = "Buy on {} at a price of {:.2f}"
    sell_on = "Sell on {} at a price of {:.2f}"
    print(buy_on.format(buy_day,buy_price))
    print(sell_on.format(sell_day,sell_price))
    print("")
    ratio = "Change in value ratio:{:.3f}"
    print(ratio.format(sell_price/buy_price))

    print("*"*40)        


def ask_filename():
    selection = input("Please enter the data file name:")
    return selection
    
running = True   
while running:
    
    #print("Thank you and Good-Bye!")
    try:
        File_name = ask_filename()
        if File_name == "":
            running = False
        elif File_name != "":
            max_profit_calculator(File_name)

    except FileNotFoundError:
        #while File_name != "GOOG.csv"or"AAPL.csv"or"AMZN.csv"or"MSFT.csv"or"TSLA.csv":
            print("Error Reading data ...")
            print("The file does not exist. Please check the name and try again")
print("")
print("Thank you and Good-Bye!")
    
