import argparse
import getopt
import logging
import os
import sys
from zipfile import ZipFile

import boto3
from botocore.exceptions import ClientError, ParamValidationError
from s3transfer import logger

S3_BUCKET_NAME = 'abcd'
S3_BASE_PATH = '/xyz'
internet_access = 'No'
intranet_access = 'No'
execution_role = 'oo'
handlerr = 'lambda_handler'
run_time = 'python3.11'
os.environ['INPUT_NAME'] = 'Actions Toolkit'


class LambdaFunction:
    def __init__(self, name=''):
        if not name:
            raise Exception('No function name given')
        self.name = name
        self.role = execution_role
        self.run = run_time
        self.hand = handlerr
        self.internetacc = internet_access
        self.intranetacc = intranet_access

    def set_role(self, rolename):
        if rolename:
            self.role = rolename

    def set_run(self, runtime):
        if runtime:
            self.run = runtime

    def set_hand(self, handler):
        if handler:
            self.hand = handler

    def set_internetacc(self, internetaccess):
        if internetaccess:
            self.internetacc = internetaccess

    def set_intranetacc(self, intranetaccess):
        if intranetaccess:
            self.intranetacc = intranetaccess

    def set_act(self, action):
        return bool(action)

    def getzip(self, dir):
        file_path = []
        for root, directories, files in os.walk(dir):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_path.append(filepath)
        with ZipFile('output.zip', 'w') as zipf:
            for file in file_path:
                zipf.write(file)
        return zipf

    def create_function(self):
        dir = '/Users/prakritipriya/Desktop/test.py'
        zipl = self.getzip(dir)
        lambda_client = boto3.client('lambda')
        try:
            response = lambda_client.create_function(
                FunctionName=self.name,
                Role=self.role,
                Runtime=self.run,
                Handler=self.hand,
                Code={'Zipfile': zipl}
            )
        except ClientError as e:
            logger.error("Couldn't create function %s. error is => %s", self.name, str(e))
        except ParamValidationError as e:
            logger.error("Param Validation Error")
        except BaseException as e:
            pass

    def update_function(self, newname):
        dir = '/Users/prakritipriya/Desktop/testpy'
        zipl = self.getzip(dir)
        lambda_client = boto3.client('lambda')
        try:
            response = lambda_client.update_function(
                FunctionName=newname,
                Code={'Zipfile': zipl}
            )

        except ClientError as e:
            logger.error("Couldn't update function %s. error is => %s", newname, str(e))
        except ParamValidationError as e:
            logger.error("Param Validation Error")
        except BaseException as e:
            pass


if __name__ == "__main__":
    for i in sys.argv:
        if "=" in i:
            key = i.split('=')[0]
            val = i.split('=')[1]
            if key == 'type':
                type = val
            if key == 'name':
                name = val
            if key == 'rolename':
                rolename = val
            if key == 'handler':
                handler = val
            if key == 'internetaccess':
                internetaccess = val
            if key == 'intranetaccess':
                intranetaccess = val
            if key == 'runtime':
                runtime = val
            if key == 'layer_name':
                layer_name = val
            if key == 'version':
                version = val
            # if key == 'layername':
            #     layername = val
            if key == 'action':
                action = val
            if key == 'newname':
                newname = val
                if type == 'lambda':
                    new = LambdaFunction(name=name)
                    new.set_role(rolename=rolename)
                    new.set_hand(handler=handler)
                    new.set_internetacc(internetaccess=internetaccess)
                    new.set_intranetacc(intranetaccess=intranetaccess)
                    new.set_run(runtime=runtime)
                    new.create_function()
                    actionn = new.set_act(action=action)
                    if actionn:
                        if newname and newname != name:
                            new.update_function(newname=newname)
                        else:
                            print('Function name already exists')
                            break
            print(f"key is {i.split('=')[0]}, Value is {i.split('=')[1]}")
        # for i in sys.argv:
        #     if "=" in i:
        #         key_val_pair = i.split('=')
        #         if len(key_val_pair) >= 2:
        #             key = key_val_pair[0]
        #             val = key_val_pair[1]
        #             print(f"key is {key}, Value is {val}")
        #         else:
        #             print(f"Invalid argument format: {i}")

        if i == '-h' or i == '-m' or i == '-o':
            argumentList = sys.argv[1:]
            options = "hmo:"
            long_options = ["Help", "File", "Output="]
            try:
                arguments, values = getopt.getopt(argumentList, options, long_options)
                for currentArgument, currentValue in arguments:
                    if currentArgument in ("-h", "--Help"):
                        print("Displaying Help")
                        print("""prc2.py type=lambda name=prak rolename=ss handler=lambda_handler
                                internetaccess=No intranetaccess=No
                                runtime=python3.11
                                src=/Users/prakritipriya/Desktop/testpy layer=se newname=prak """)
                    elif currentArgument in ("-m", "--File"):
                        print("Displaying file_name:", sys.argv[0])
                    elif currentArgument in ("-o", "--Output"):
                        print(("Enabling special output mode (% s)") % (currentValue))
            except getopt.error as err:
                print(str(err))
