"""
  definition of the functions that are employed in the project
"""

# import packages

import time
import matplotlib.pyplot as plt
import numpy as np


# definition of the functions that are employed in the project

def dict_and_list(start_, end_):
    """
    Creates a list with ASCII (in DECIMAL) elements from start to end (start
    and end are given in input), initializes a dictionary which key elements
    are the elements of the list and whose related values are set to zero.

    Arguments:

      start_: integer value, decimal number of the first ASCII element
      end_: integer value, decimal number of the last ASCII element

    Returns:

      ascii_dict: dictionary which key elements are the elements of the
      list and whose related values are set to zero
      ascii_list: list with chars, ascii elements which decimal number
      goes from start to end
    """
    ascii_dict = {chr(i): 0 for i in range (start_, end_ + 1)}
    ascii_list = [chr(i) for i in range (start_, end_ + 1)]

    return ascii_dict, ascii_list



def count_function(file_string, start_, end_):
    """
    Creates a list with ASCII (in DECIMAL) elements from start to end (start
    and end are given in input), initializes a dictionary which key elements
    are the elements of the list and whose related values are set to zero,
    counts the number of each element in the text file.

    Arguments:

      file_string: text file's string opened in the read mode
      start_: integer value, decimal number of the first ASCII element
      end_: integer value, decimal number of the last ASCII element

    Returns:

      ascii_dict: dictionary which key elements are the elements of the
      list and whose relative values are updated to the related count
      ascii_list: list with chars, ascii elements which decimal number
      goes from start to end
    """
    ascii_dict, ascii_list = dict_and_list(start_, end_)

    # for every element of the list counts how many times that
    # element appears in the text file
    for i, element in enumerate(ascii_list):

        number = file_string.count(ascii_list[i])

        # updates the related value of the key after counting
        ascii_dict.update({ascii_list[i]: number})

    return ascii_dict, ascii_list



def count_relative(file_string, start_, end_):
    """
    Creates a list with ASCII (in DECIMAL) elements from start to end (start
    and end are given in input), initializes a dictionary which key elements
    are the elements of the list and whose related values are set to zero,
    counts the number of each element in the text file and divides by the sum
    of all the values in the dictionary.

    Arguments:

      file_string: text file's string opened in the read mode
      start_: integer value, decimal number of the first ASCII element
      end_: integer value, decimal number of the last ASCII element


    Returns:

      ascii_dict: dictionary which key elements are the elements of the
      list and whose relative values are updated to the related count
    """
    ascii_dict, ascii_list = count_function(file_string, start_, end_)

    # sum of all the values in the dictionary
    sum_all = sum(ascii_dict.values())

    # divides every value relative to every key by sum_all
    # if it is different than zero
    for i, element in enumerate(ascii_list):

        if sum_all != 0:
            ascii_dict.update({ascii_list[i]: ascii_dict[ascii_list[i]]/sum_all})

    return ascii_dict



def histogram_relative(file_string, start_, end_):
    """
    Creates a list with ASCII (in DECIMAL) elements from start to end (start
    and end are given in input), initializes a dictionary which key elements
    are the elements of the list and whose related values are set to zero,
    counts the number of each element in the text file and divides by the sum
    of all the values in the dictionary.
    Shows the histogram with the keys and values of the dictionary and returns
    the elapsed time without considering the plt.show command.

    Arguments:

      file_string: text file string, in read mode
      start_: integer value, number of the first ascii element
      end_: integer value, number of the last ascii element + 1

    Returns:

      shows the histogram and returns the elapsed time without considering
      the plt.show command
    """
    start = time.time()

    ascii_dict = count_relative(file_string, start_, end_)

    # creates the histogram with the keys and values of the dictionary
    plt.bar(ascii_dict.keys(), ascii_dict.values(), width = 0.82,
    edgecolor = 'cyan', linewidth = 0.4)

    plt.xlabel('Letters', color = 'navy')
    plt.ylabel('Relative frequence of each letter in the text file', color = 'navy')
    plt.title('Histogram: relative frequence of each letter in the text file', color = 'navy')

    end = time.time()

    # shows the histogram
    plt.show()

    # return the elapsed time relative to this function without considering
    # the plt.show command
    return end - start


def choose_parts(file_path, start_line, end_line, print_choose = False):
    """
    If print_choose is True, given the number of the first and the last line
    between which we want to read and print out the text file, it prints out the
    text in between.

    Arguments:

      file_path: path to the text file
      start_line: integer value, line from which we want to start reading and
      printing out the text file
      end_line: integer value, line at we want to finish reading and
      printing out the text file
      print_choose: boolean value

    Returns:

      prints out the chosen part of the text file
    """
    if print_choose is True:

        # opens the text file in the read mode
        with open(file_path, 'r') as file_:

            # creates an array with lines numbers we want to print
            line_range = np.linspace(start_line - 1, end_line - 1, end_line - start_line + 1)

            # creates a tuple with lines in the range of line_range
            lines = (line for i, line in enumerate(file_) if i in line_range)

            for line in lines:
                print(line)


def stats_book(file_path, print_stats = False):
    """
    If print_stats is True prints out the basic statistics of the text file: the total
    number of lines, words, characters, characters without whitespace,
    numbers, special characters and whitespace.

    Arguments:

      file_path: path to the text file
      print_stats: boolean value

    Returns:

      prints out the basic statistics of the text file
    """
    if print_stats is True:

        # opens the text file in the read mode
        with open(file_path, 'r') as file_:

            # computes and prints out the number of total lines
            total_lines = max(i for i, line in enumerate(file_))
            print(f'Number of total lines: {total_lines + 1}')


        with open(file_path, 'r') as file_:

            file = file_.read()

            # computes and prints out the number of total words
            total_words = len(file.split())
            print(f'Number of total words: {total_words}')

            # computes and prints out the number of total characters
            total_characters_whitein = len(file)
            print(f'Number of total characters: {total_characters_whitein}')

            # computes and prints out the number of characters without whitespace
            data = file.replace(" ","")
            total_characters_notwhite = len(data)
            print(f'Number of characters without whitespace: {total_characters_notwhite}')

            # computes and prints out a dictionary which keys are the numbers from
            # 0 to 9 and whose values are the total number of times in which that
            # number appears in the the text file
            ascii_dict_numbers = count_function(file, 48, 58)
            print(f'Dictionary of numbers: {ascii_dict_numbers}')

            # computes and prints out a dictionary which keys are special characters
            # and whose values are the total number of times in which that character
            # appears in the the text file
            ascii_dict_specialchars = {**count_function(file, 33, 48)[0],
            **count_function(file, 58, 65)[0], **count_function(file, 91, 97)[0],
            **count_function(file, 123, 127)[0]}
            print(f'Dictionary of specialchars: {ascii_dict_specialchars}')

            # computes and prints out the number of total whitespace
            total_whitespace = file.count(" ")
            print(f'Number of whitespace: {total_whitespace}')
