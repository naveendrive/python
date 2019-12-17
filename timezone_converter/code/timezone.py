#This module used to convert the given timezone.
#steps to work with multiple timezones using pytz module
#****************************************************************************************************
# Step-1 : create a datetime object
# Step-2: create a source timezone object
# Step-3 : assign source timezone object into datetime object
# Step-4 : create target timezone object
# Step-5 : convert source timezone object to target timezone object
#********************************************************************************************************

s
#Importing required modules:
from datetime import datetime
import pytz
global convert_from,convert_to,strftime_format

convert_from="Asia/Kolkata"
convert_to="UTC"
strftime_format="%Y-%m-%d %H.%M.%S.%Z"


def timezone_converter(convert_from,convert_to,strftime_format):
    # step-1
    date_object=datetime.now()
    # step-2
    #to all the timezones use pytz.all_timezones
    source_tz_object=pytz.timezone(convert_from)
    # step-3
    source_tz_final_object=source_tz_object.localize(date_object)
    #step-4
    target_tz_object=pytz.timezone(convert_to)
    #step-5
    outcome=source_tz_final_object.astimezone(target_tz_object)
    expected_output=outcome.strftime(strftime_format)
    return expected_output

#use as built in function
converter=timezone_converter(convert_from,convert_to,strftime_format)
print(converter)

converter_1=timezone_converter("UTC","Asia/Kolkata","%Y-%m-%d %H.%M.%S.%Z")
print(converter_1)

converter_2=timezone_converter("Asia/Kolkata","UTC","%Y-%m-%d %H.%M.%S.%Z")
print(converter_2)





