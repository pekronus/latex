import sys
import numpy as np


def start(f):
    f.write("\\documentclass{exam}\n")
    f.write("\\newcommand{\\qm}{\\underline{\\hspace{0.3cm}?\hspace{0.3cm}}}\n");
    f.write("\\usepackage{tikz}\n")
    f.write("\\usepackage{amsmath}\n")
    f.write("\\begin{document}\n")
    f.write("""\\begin{center}
	\\fbox{\\fbox{\\parbox{5.5in}{\centering
				Read the questions carefully. For multiple choice circle the letter corresponding to the answer}}}
\\end{center}\n\n""")
    f.write("""\\vspace{0.1in}
\\makebox[\\textwidth]{Student name:\\enspace\\hrulefill}\n\n""")
    f.write("\\begin{questions}\n")

#--------------------
def end(f):
    f.write("""\end{questions}
\end{document}\n""")

def shuffle_answers(f, qs, a):
    f.write("\\begin{question}\n")
    f.write (qs)
    f.write("\n")
    rr = np.arange(len(a))
    np.random.shuffle(rr)
    f.write("\\begin{choices}\n")
    for i in rr:
        f.write("\\choice %s\n" % a[i])
    f.write("\\end{choices}\n")
    
    f.write("\\end{question}\n\n")
#--------------------
def expr1_mult(f, x, y, d):
    qs = "What expression is another way of showing $ %d \\times %d $"  % (x,y)
    a = []
    a.append("$(%d \\times %d \\times %d ) $" % (x, y, d))
    a.append("$(%d + %d) \\times %d  $" % (x, x/d, y))
    a.append("$(%d \\times %d) + %d  $" % (x, y,  x/d))
    a.append("$(%d \\times %d) \\times %d  $" % (x/d, d, y)) # correct
    shuffle_answers(f, qs, a)
    
#------------------------------
def roundq(val, qstart, unit, d):
    r_str = "hundred" if d == 2 else "ten" if d == 1 else "thousand"
    qs = "%s is %d %s. Round it to the nearest %s" % (qstart, val, unit, r_str)
    a = [];
    corr = int(round(val/10000, 4-d)*10000)
    a.append(corr)
    a.append(val)
    a.append(corr - 10**d if corr > val else corr + 10**d)
    a.append(int(round(val/10000, 4-(d-1))*10000))
    shuffle_answers(f, qs, a)

##------------------------------
def eqn_true(x, y, dv = True):
    s = "\\div " if dv else "\\times "
    qs = "What number makes the equation true $ %d = %s %s %d$ ?" % (x, "\\qm ", s ,y)
    a = [];
    corr = x*y if dv else x/y
    incorr = int(x/y) if dv else x*y
    a.append(corr)
    a.append(corr + 1)
    a.append(y)
    a.append(incorr)
    shuffle_answers(f, qs, a)

## Main---------------------------
if len(sys.argv) <= 1:
    print("Need a file name");
seed = 0
if len(sys.argv) >= 3:
    seed = int(sys.argv[2])
np.random.seed(seed)
    
f = open(sys.argv[1], "w")
start(f)
expr1_mult(f, 8, 8, 4)

roundq(578, "The distance between two cities", "miles", 2)

eqn_true(6, 4, dv=True)
end(f)
f.close()
