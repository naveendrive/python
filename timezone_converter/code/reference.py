#file:///C:/Users/Naveen/Desktop/pytz%20source.html
import pytz
from datetime import datetime

date_object=datetime.now()
current_timezone=pytz.timezone("Asia/Kolkata")
new=current_timezone.localize(date_object)
target_timezone=pytz.timezone("UTC")
final_output=new.astimezone(target_timezone)
print(final_output.strftime("%d-%M-%y %H:%M:%S:%F:%Z"))


#Rference : file:///C:/Users/Naveen/Desktop/pytz%20source.html
