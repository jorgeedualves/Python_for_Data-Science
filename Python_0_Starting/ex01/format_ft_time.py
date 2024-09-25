from time import  time, gmtime, strftime

current_time = time()

print("Seconds since January 1, 1970:", f"{current_time:,.4f}", "or", f"{current_time:e}", "in scientific notation")
print(strftime("%b %d %Y"))
