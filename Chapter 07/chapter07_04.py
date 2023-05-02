
my_text = """\
Extract from Hamlet, by William Shakespeare

To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heartache and the thousand natural shocks
That flesh is heir to,-'tis a consummation
Devoutly to be wished. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;
...
"""

with open("./testing_files/sample3.txt", mode="a") as f:
    f.write(my_text)
