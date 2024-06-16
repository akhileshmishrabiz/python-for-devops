import  boto3
from packaging.version import Version
import argparse

lambda_function = boto3.client('lambda')



def function_with_lower_runtime(python_runtime):
    fun_with_lower_runtime = []
    response = lambda_function.list_functions()["Functions"]
    for item in response:
        function_name = item["FunctionName"]
        runtime = item["Runtime"].split("python")[1]
        if not Version(runtime) >= Version(python_runtime):
            fun_with_lower_runtime.append(function_name)
    return fun_with_lower_runtime


def update_python_runtime(function_name, python_runtime):
    response = lambda_function.update_function_configuration(
        FunctionName=function_name,
        Runtime=f'python{python_runtime}'
        )


def run(python_runtime):
    print(function_with_lower_runtime(python_runtime))
    for function_name in function_with_lower_runtime(python_runtime):
        update_python_runtime(function_name, python_runtime)

def argparser():
    parser = argparse.ArgumentParser(
                        prog='ProgramName',
                        description='What the program does',
                        epilog='Text at the bottom of help')
    parser.add_argument('python_runtime')
    args = parser.parse_args()
    return  args

# execution

if __name__ == '__main__':
    args = argparser()
    run(args.python_runtime)