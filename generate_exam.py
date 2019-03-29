import sys
import numpy as np


def start(f):
    f.write("\\documentclass{exam}\n")
    f.write("\\newcommand{\\qm}{\\underline{\\hspace{0.3cm}?\hspace{0.3cm}}}\n");
    f.write("\\usepackage{tikz}\n")
    f.write("\\usepackage{amsmath}\n")
    f.write("\\begin{document}\n")
    f.write("""\\begin{center}
	\\fbox{\\fbox{\\parbox{5.5in}{\c\entering
				Read the questions carefully. For multiple choice circle the letter corresponding to the answer}}}
\\end{center}\n\n""")
    f.write("""\\vspace{0.1in}
\\makebox[\\textwidth]{Student name:\\enspace\\hrulefill}\n\n""")
    f.write("\\begin{questions}\n")

#--------------------
def end(f):
    f.write("""\end{questions}
\end{document}\n""")

    
#--------------------
def expr1_mult(f, x, y, d):
    f.write("\\begin{question}\n")
    f.write ("What expression is another way of showing $ %d \\times %d $\n"  % (x,y))
    a = []
    a.append("$(%d \\times %d \\times %d ) $\n" % (x, y, d))
    a.append("$(%d + %d) \\times %d  $\n" % (x, x/d, y))
    a.append("$(%d \\times %d) + %d  $\n" % (x, y,  x/d))
    a.append("$(%d \\times %d) \\times %d  $\n" % (x/d, d, y)) # correct
    rr = np.arange(4)
    np.random.shuffle(rr)
    f.write("\\begin{choices}\n")
    for i in rr:
        f.write("\\choice %s" % a[i])
    f.write("\\end{choices}\n")
    
             
    
    f.write("\\end{question}\n\n")
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

end(f)
f.close()
