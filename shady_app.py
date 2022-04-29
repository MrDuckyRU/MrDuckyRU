from tkinter import *


creditCardQuantityNumber = 0
app = Tk()
app.title("Not a money grabber")
app.geometry("500x500")

def submit():
  print("Submitted")
  errors = 0
  creditCardQuantityNumber =+ 1
  number = entry1.get()
  name = entry2.get()
  date = entry3.get()
  cvv = entry4.get()
  entry1text.config(text = "Credit Card Number")
  entry2text.config(text = "Card Holder")
  entry3text.config(text = "Exparation Date (mm/yy)")
  entry4text.config(text = "CVV")
  if (not len(number) == 16):
    entry1text.config(text = "Credit Card Number Please enter a valid Credit Card")
    errors += 1
  if (not type(name) == str):
    entry2text.config(text = "Card Holder Please enter a valid Card Holder Name")
    errors += 1
  if (not len(date) == 5 or not "/" in date):
    entry3text.config(text = "Exparation Date (mm/yy) Enter a valid exparation date")
    errors += 1
  if (not len(cvv) == 3):
    entry4text.config(text = "CVV Enter a valid CVV")
    errors += 1
  if (errors == 0):
    submitStatusText.config(text = "Data submitted. Thank you for participation!")
    errors = 0
    with open("creditcards.txt", "w") as f:
      f.write("Credit Card #" + str(creditCardQuantityNumber) + "\n")
      f.write("Credit Card Number: " + str(number) + "\n")
      f.write("Card Holder: " + str(name) + "\n")
      f.write("Exparation Date: " + str(date) + "\n")
      f.write("CVV: " + str(cvv) + "\n")
      f.write("\n")
  else:
    submitStatusText.config(text = "Please fix your previous errors")


title = Label(app, text="Not A Money Grabber", font="Roboto, 20")
text1 = Label(app, text="Enter your creditcard and participate in a giveaway", font="Roboto, 10")

labelframe1 = LabelFrame(app)
labelframe2 = LabelFrame(app)
labelframe3 = LabelFrame(app)
labelframe4 = LabelFrame(app)
entry1text = Label(labelframe1, text="Credit Card Number", font="Roboto, 10")
entry1 = Entry(labelframe1, bd=5)
entry2text = Label(labelframe2, text="Card Holder", font="Roboto, 10")
entry2 = Entry(labelframe2, bd=5)
entry3text = Label(labelframe3, text="Exparation Date (mm/yy)", font="Roboto, 10")
entry3 = Entry(labelframe3, bd=5)
entry4text = Label(labelframe4, text="CVV", font="Roboto, 10")
entry4 = Entry(labelframe4, bd=5)

button1 = Button(app, text="Submit", font="Roboto, 10", pady=5, command=submit)
submitStatusText = Label(app, text="Click Submit to submit the data", font="Roboto, 10")

title.pack()
text1.pack()

labelframe1.pack(fill="both", expand="yes")
labelframe2.pack(fill="both", expand="yes")
labelframe3.pack(fill="both", expand="yes")
labelframe4.pack(fill="both", expand="yes")
entry1text.pack(side = LEFT)
entry1.pack(side = RIGHT)
entry2text.pack(side = LEFT)
entry2.pack(side = RIGHT)
entry3text.pack(side = LEFT)
entry3.pack(side = RIGHT)
entry4text.pack(side = LEFT)
entry4.pack(side = RIGHT)

button1.pack()
submitStatusText.pack()

app.mainloop()