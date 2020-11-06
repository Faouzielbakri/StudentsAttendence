from functions import *
from realtimeqr import *

cam = 0
if input('realtime press 1 for url press 0 : '):
   link = doIt(cam)
else:
    link = input('please give form link : ')

id = getformid(link)
url = getformurl(id)
data = get_values(get_offsets(url))

send_attendance(url,data)

