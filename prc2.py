import argparse
import getopt
import logging
import os
import sys
from zipfile import ZipFile

import boto3
from actions_toolkit import core
from botocore.exceptions import ClientError, ParamValidationError
from s3transfer import logger

S3_BUCKET_NAME = 'abcd'
S3_BASE_PATH = '/xyz'
internet_access='No'
intranet_access='No'
execution_role='oo'
handlerr='lambda_handler'
run_time='python3.11'
os.environ['INPUT_NAME'] = 'Actions Toolkit'
class LambdaFunction:
    def __init__(self,name=''):
        if name=='' or None:
            raise Exception('No function name given')

    def role(self,rolename):
        if rolename=='' or None:
            rolename=execution_role
        else:
            self.role=rolename
    
    def run(self,runtime):
        if runtime=='' or None:
            runtime=run_time
            return runtime
        else:
            self.run=runtime
            return self.run
            
    def hand(self,handler):
        if handler=='' or None:
            handler=handlerr
            return handler
        else:
            self.hand=handler
            return self.hand
    
    def internetacc(self,internetaccess):
        if internetaccess=='' or None:
            internetaccess=internet_access
            return internetaccess
        else:
            self.internetacc=internetaccess
            return self.internetacc

    def intranetacc(self,intranetaccess):
        if intranetaccess=='' or None:
            intranetaccessc=intranet_access
            return intranetaccess
        else:
            self.intranetacc=intranetaccess
            return self.intranetacc
    
    # def newn(self,newname):
    #     if newname==''or None:
    #         raise Exception('No function name given')
    
    def getzip(self,dir):
        file_path = []
        for root,directories, files in os.walk(dir):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_path.append(filepath)
        with ZipFile('output.zip', 'w') as zipf:
            for file in file_path:
                zipf.write(file)
        return zipf
            
    def create_function(self,function_name,role_name,runtime,handler):
        dir='/Users/prakritipriya/Desktop/testpy'
        zipl = self.getzip(dir)
        lambda_client = boto3.client('lambda')
        try:
            response = lambda_client.create_function(
            FunctionName=function_name,
            Role=role_name,
            Runtime=runtime,
            Handler=handler,
            Code={'Zipfile':zipl}
        )
        except ClientError as e:
            logger.error("Couldn't create function %s. error is => %s", function_name,str(e))
        except ParamValidationError as e:
            logger.error("Param Validation Error")
        except BaseException as e :
            pass
    # def layers(self,layer_name,version):
    #     no=int(input('Enter number of files: '))
    #     py=input('Enter output zip file: ')
    #     zi=self.getzip(no,py)
    #     # logger.info(zi)
    #     # logger.info(layer_name)
    #     # logger.info(version)
        
    def update_function(self,function_name):
        dir='/Users/prakritipriya/Desktop/testpy'
        zipl = self.getzip(dir)
        lambda_client = boto3.client('lambda')
        try:
            response = lambda_client.update_function(
            FunctionName=function_name,
            Code={'Zipfile':zipl}
        )
        except ClientError as e:
            logger.error("Couldn't create function %s. error is => %s", function_name,str(e))
        except ParamValidationError as e:
            logger.error("Param Validation Error")
        except BaseException as e :
            pass

        
        
    
for i in sys.argv:
    print(f"Arg is: {i}")
    if "=" in i:
        key=i.split('=')[0]
        val=i.split('=')[1]
        if key=='type':
            type=val
        if key=='name':
            name=val
        if key=='rolename':
            rolename=val
        if key=='handler':
            handler=val
        if key=='internetaccess':
            internetaccess=val
        if key=='intranetaccess':
            intranetaccess=val
        if key=='runtime':
            runtime=val
        if key=='layer_name':
            layer_name=val
        if key=='version':
            version=val
        if key=='layername':
            layername=val
        if key=='newname':
            newname=val
            if type=='lambda':
                new=LambdaFunction(name=name)
                new.role(rolename=rolename)
                new.hand(handler=handler)
                new.internetacc(internetaccess=internetaccess)
                new.intranetacc(intranetaccess=intranetaccess)
                new.run(runtime=runtime)
                new.create_function(function_name=name,role_name=rolename,runtime=runtime,handler=handler)
                # if key=='newname' and key='name':
                #     newname=val
                #     name=val
                # if update=='Yes':
                # parser= argparse.ArgumentParser()
                # parser.add_argument('newname',help='function name',action='store_true')
                # args = parser.parse_args()
                if newname!='':
                        if newname!=name:
                            new.update_function(function_name=newname)
                        else:
                            print('Function name already exists')
                            break
                else:
                    break
        print(f"key is {i.split('=')[0]}, Value is {i.split('=')[1]}")
    if i=='-h' or i=='-m' or i=='-o':
        argumentList = sys.argv[1:]
        options = "hmo:"
        long_options = ["Help","File" "Output="]
        try:
            arguments, values = getopt.getopt(argumentList, options, long_options)
            for currentArgument, currentValue in arguments:
                if currentArgument in ("-h", "--Help"):
                    print ("Displaying Help")
                    print ("""prc2.py type=lambda name=prak rolename=ss handler=lambda_handler
                            internetaccess=No intranetaccess=No
                            runtime=python3.11
                            src=/Users/prakritipriya/Desktop/testpy layer=se newname=prak """)
                elif currentArgument in ("-m", "--File"):
                    print ("Displaying file_name:", sys.argv[0])
                elif currentArgument in ("-o", "--Output"):
                    print (("Enabling special output mode (% s)") % (currentValue))
        except getopt.error as err:
            print (str(err))
        
        








