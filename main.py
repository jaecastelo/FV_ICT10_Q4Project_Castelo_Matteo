from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

days = np.array(['Monday','Tuesday','Wednesday','Thursday','Friday'])
absences = np.array([1,0,7,4,9])

def attendance_tracker(e):
    document.getElementById("output").innerHTML = ""

    day = document.getElementById("day").value
    value = document.getElementById("absence").value

    if value == "":
        document.getElementById("output").innerHTML = "Enter a number"
        return

    index = np.where(days == day)[0][0]
    absences[index] = int(value)

    plt.close()
    plt.plot(days, absences, marker='o')
    plt.title("Weekly Attendance")
    plt.xlabel("Day")
    plt.ylabel("Absences")
    plt.grid()

    display(plt.gcf(), target="output")