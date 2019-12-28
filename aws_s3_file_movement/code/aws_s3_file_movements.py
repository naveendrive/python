"""
# Module name   : AWS S3 File movement
# Author        : Naveenkumar Murugesan

# Module Info
    1.This component used to rearrange the file structure as per the requirement
    2.Source and destination directories has been mentioned in the config file and based on the config information the program rearrange the files
"""

import subprocess
import configparser

#command formation
cmd_form_1="aws s3 ls  "
cmd_form_2="aws s3 mv "
cmd_form_3=" | awk '{print $4}' "

#Read the information and path details from config file
def config_reader():
    global SOURCE,CSV_PATH,JSON_PATH,REJECTED_PATH
    config= configparser.ConfigParser()
    config.read("aws_s3_file_movement.config")

    #source and desitination path details
    SOURCE=str(config.get("config","source_bucket_path"))
    CSV_PATH=str(config.get("config","csv_bucket_path"))
    JSON_PATH=str(config.get("config","json_bucket_path"))
    REJECTED_PATH=str(config.get("config","rejectd_path"))

#S3 file movement function
def s3_file_move():
    lis=cmd_form_1+SOURCE+cmd_form_3
    s3_file_read=subprocess.check_output(lis,shell=True).decode().split("\n")
    while ('' in s3_file_read):
        s3_file_read.remove('')

    for file in s3_file_read:
        if file.endswith(".csv"):
            move_file=cmd_form_2+"s3://"+SOURCE+file+"  s3://"+CSV_PATH
            subprocess.call(move_file, shell=True)

        elif file.endswith(".json"):
            move_file1=cmd_form_2+"s3://"+SOURCE+file+"  s3://"+JSON_PATH
            subprocess.call(move_file1,shell=True)
        else:
            move_rejected_file=cmd_form_2+"s3://"+SOURCE+file+"  s3://"+REJECTED_PATH
            subprocess.call(move_rejected_file,shell=True)

#Module starts from the main
if __name__=="__main__":
    config_reader()
    s3_file_move()
    print("Files has been successfully rearranged")