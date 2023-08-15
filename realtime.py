from datetime import datetime

#--> Real Time
DAYnow = datetime.now().day
MOUnow = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][datetime.now().month - 1]
YEAnow = datetime.now().year
HOUnow = datetime.now().hour
MINnow = datetime.now().minute
SECnow = datetime.now().second
timenow = f"{DAYnow} {MOUnow} {YEAnow} - {HOUnow:02}:{MINnow:02}:{SECnow:02}"