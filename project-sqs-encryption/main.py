
import functions
import argparse


def argparser():
    parser = argparse.ArgumentParser(
                        prog='ProgramName',
                        description='What the program does',
                        epilog='Text at the bottom of help')
    parser.add_argument('key')
    args = parser.parse_args()

    return  args

# execution
args = argparser()
print(functions.run(args.key))



# 'alias/pythonfordevops'