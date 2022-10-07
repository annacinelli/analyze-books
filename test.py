"""
  definition of test functions
"""

def control(file_path):
    """
    Opens and prints out every line of the text file whose
    path to the file is given in input

    Arguments:

      file_path: path to the text file

    Returns:

      prints out every line of the text file whose path
      to the file is given in input
    """
    print(f'Opening input file {file_path}')

    # opens the text file in the read mode
    with open(file_path, 'r') as input_file:

        text = input_file.read()

    print(text)
    print('Done.\n')
