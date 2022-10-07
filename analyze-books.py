"""
  the main file of the project
"""

# import packages

import argparse
import time
import test
import functions as func  # file with the definition of the functions
                          # that are employed in the project


if __name__ == '__main__':

    # use the argparse package to take the path to the text file, other
    # positional arguments and give the commands from the command-line
    parser = argparse.ArgumentParser(
        description = 'Analyze a book or a file in .txt format')

    parser.add_argument('infile', type = str, nargs = '*',
        help = 'input the file-path from the command line and if you type --choose\
               input also the number of the first and the last line from and to you\
               want to print the text file')

    parser.add_argument('--hist', dest = 'hist', action = 'store_true', default = False,
                    help = 'prints out the histogram of the relative frequence of\
                           characters')

    parser.add_argument('--stats', dest = 'stats', action = 'store_true', default = False,
                    help = 'prints ot the basic statistics of the book')

    parser.add_argument('--choose', dest = 'choose', action = 'store_true', default = False,
                    help = 'prints out only the parts of the book you want')

    args = parser.parse_args()


    if args.choose is True:

        START_LINE = int(args.infile[1])
        END_LINE = int(args.infile[2])

    else:

        START_LINE = 0
        END_LINE = 0

    # opens and prints out every line of the text file
    test.control(args.infile[0])


    # opens the text file in the read mode
    with open(args.infile[0], 'r') as file_:

        file = file_.read()

        # creates a string with every uppercase character converted to a
        # lowercase character
        file_lower = file.lower()

        # if args.hist is True it runs the histogram_relative function, else
        # it only runs the count_relative function and computes the elapsed
        # time of the operations it does
        if args.hist is True:

            delta_t1 = func.histogram_relative(file_lower, 97, 123)

        else:
            start = time.time()

            func.count_relative(file_lower, 97, 123)

            end = time.time()

            delta_t1 = end - start


    start2 = time.time()

    # if args.choose is True computes the choose_parts function
    func.choose_parts(args.infile[0], START_LINE, END_LINE, args.choose)

    # if args.stats is True computes the stats_book function
    func.stats_book(args.infile[0], args.stats)

    end2 = time.time()

    # computes the elapsed time of the two previous operations
    delta_t2 = end2 - start2

    # computes and prints out the total elapsed time
    total_time = delta_t1 + delta_t2
    print(f'Total elapsed time: {total_time} s\n')
