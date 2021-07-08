# Drunk-Model
## Information
You can run the file then click "?" at the right bottom side
Or these are the text that help you learn about this model:
```
Suppose that a drunk drank too much and could not go along a straight line.
He starts his 'journey' from a street lamp.
Suppose his moving follows the following rules:

1.Turn to a random direction.
2.Move forward for 1 metre.
3.Back to 1.

Suppose after a n times' moving,
His distance to the street lamp is L.
What is the numerical relation between n and L?

Because the moving have a random progress,
The L is unpredictable.                 _
So we can only say the relation between L (the average value of all possible L-s) and n.

After calculation we found out that:
_    _
L = √n
Now This model is used to calculate if this is right.

Also, this model can also explain the Brown Motion.
```
By the way, if you want to know how do we calculate, look at this:  
[^text]

## About us
We are a team (only one person) that provides good products.  
You may say: `You are lying!`  
Well, it's a pity that you are ~~right~~ <b>WRONG</b>!  
For example, this is one of our products (A simulater which simulate the genetic):
```
"""
DNA_nuc:four kinds of DNA (Deoxyribonucleic Acid) nucleobases
notice:in this program,a person has only 4600 nucleobases!
"""

import random as r
import time as t

a = t.perf_counter()
DNA_nuc = ["A", "G", "C", "T"]
def string(list):
    s = ""
    for i in list:
        for j in i:
            s += j
        s += "\n\t\t\t"
    return s

def rand_chromosome():
    dna = []
    for i in range(100):
        dna.append(DNA_nuc[r.randint(0, 3)])
    return dna

class DNA:
    def __init__(self):
        self.dna1 = []
        for i in range(23):
            self.dna1.append(rand_chromosome())
        self.dna2 = []
        for i in range(23):
            self.dna2.append(rand_chromosome())
        self.dna = [self.dna1, self.dna2]

    def index(self, num):
        return self.dna[num]

class Person:
    def __init__(self, dna):
        self.dna = dna

    def child_dna(self):
        return self.dna[r.randint(0, 1)]
people = []

def __main__(contemporary):
    if contemporary == 1:
        people.append([Person([people[-1][0].child_dna, people[-1][1].child_dna])])
    else:
        p = []
        for i in range(2**contemporary):
            p.append(Person([people[-1][2*i-2].child_dna(), people[-1][2*i-1].child_dna()]))
        people.append(p)
        __main__(contemporary-1)

contem = int(input("how many contemporaries?(>1)"))
p = []
print('<?xml version="1.0" encoding="UTF-8"?>\n<doc>\n\t<ancestor>')
for i in range(2**contem):
    dna = DNA().dna
    p.append(Person(dna))
    print("\t\t<person>\n\t\t\t"+string(dna[0])+",\n\t\t\t"+string(dna[1])+"\n\t\t</person>")
people.append(p)
print("\t</ancestor>")
__main__(contem-1)
for i in people[0:-1]:
    print('\t<posterity num="'+str(people.index(i))+'">')
    for j in i:
        print("\t\t<person>\n\t\t\t"+string(j.dna[0])+","+string(j.dna[1])+"\n\t\t</person>")
    print("\t</posterity>")
print("</doc>")
b = t.perf_counter()
print("time:"+str(b-a)+"s")
```
(You can see it at <a href="https://github.com/BlueSilenceLiu/Genetic/tree/main">Genetic</a>  
Want to find more?<a href="https://github.com/BlueSilenceLiu?tab=repositories">Click me!</a>


[^text] Suppose the moving is spreaded to two direction: Motion of x-axis and Motion of y-axis.  
Then suppose they are X and Y.
Suppose each step is l and on x and y axis are $$\overline{x} and \overline{y}$$
Then 
$$ X = x_{1} + x_{2} + ... + x_{n} 
Y = y_{1} + y_{2} + ... + y_{n} $$
Acording to the *Pythagoras Theorem*
$$ 
( \overline{L} )^{2} = X^{2} + Y^{2}
=(x_{1} + x_{2} + ... + x_{n} )^{2} + ( y_{1} + y_{2} + ... + y_{n} )^{2}
=x^{2}_{1} + x^{2}_{2} + ... + x^{2}_{n} + 2 x_{1} x_{2} + 2 x_{1}x_{3} + ... + 2 x_{n-1} x_{n} + y^{2}_{1}......
=x^{2}_{1} + x^{2}_{2} + ... + x^{2}_{n} + y^{2}_{1} + y^{2}_{2} + ... + y^{2}_{n}     (everyone of \{x_{n},n \in \mathbb{N} \} multiply another is either positive or negative, as a result, in an average situation the sum of the products is zero)
=n \overline{x}^{2} + n \overline{y}^{2}
=n(\overline{x}^{2} + \overline{y}^{2})
=n l^{2}

\because \overline{L} ^{2} = n l^{2}
\therefore \overline{L} = \sqrt{n l^{2}}
=\sqrt{n} l
$$
Now because l = 1
therefore, $$\overline{L} = \sqrt{n}$$
