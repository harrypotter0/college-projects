import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    # we could put the try anywhere. The weak point, however, starts
    # in my opinion immediately when we accept user input... no longer
    # is this is a closed-program, so I would personally code this block
    # here, but you could put the try right about the print statement
    # of where we search for the color and we KNOW it will throw an error
    # if not in the list.
    try:
        whatColor = raw_input('What color do you wish to know the date of?:')

        if whatColor in colors:
            coldex = colors.index(whatColor)
            theDate = dates[coldex]
            print('The date of',whatColor,'is:',theDate)
        else:
            # now we can handle a specific scenario, instead
            # of handling it with a "catch-all" error.
            # now we have error handling and
            # proper logic. Yay.
            print('This color was not found.')

    # in python 2, this is read exception Exception, e. It's just helpful
    # to know this for porting old scripts if you need to.


    except Exception as e:
        print(e)
