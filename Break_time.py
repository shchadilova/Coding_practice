import webbrowser
import time

total_breaks = 1
break_count = 0


print("Break proagram started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count = break_count + 1
