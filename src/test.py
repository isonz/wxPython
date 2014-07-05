def baseN(num,b):
   return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

print 9876543210/-7
print 9876543210%-7