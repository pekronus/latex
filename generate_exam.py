import sys
import numpy as np

gnames = ["John", "Sally", "Esther", "Juan", "Daniel", "Monica", "Julia", "Brian", "Jessica", "Adam", "Michael"]

class BasicTime:
    """A class for basic hour minute manipulations. Does not under satmd days """
    mins = 0 # 0-59
    hours = 12 # 0-23

    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins
        
    def __str__(self):
        ph = self.hours if self.hours <= 12 else self.hours - 12
        return str (ph) + ":" + ("%02d" % self.mins) + ("pm" if self.hours >=12 else "am")
        
    def add_mins(self, mins):
        ah, rm = divmod(self.mins + mins, 60)
        rh = self.hours + ah
        if rh > 23 or rh < 0 or rm < 0 or rm > 59:
            raise ValueError
        return BasicTime(rh, rm)

class NumberLine:
    
    dflt_tick_size = 0.2
    def __init__(self, tlen, start_label, end_label, points_pos, ndivs, scale_fact = 4):
        self.tlen = tlen
        self.start_label = start_label
        self.end_label = end_label
        self.points_pos = points_pos
        self.ndivs = ndivs
        self.scale_fact = scale_fact

    def draw_tick(self, x, tick_size=dflt_tick_size):
        return "\\draw (%5.2f, %5.2f) -- (%5.2f, %5.2f );" % (x*self.scale_fact, -tick_size/2, x*self.scale_fact, tick_size/2)

    def draw_ticks(self, f, tick_size = dflt_tick_size):
        ticks = np.linspace(0, self.tlen, self.ndivs+1)
        for t in ticks:
            f.write(self.draw_tick(t, tick_size) + "\n");

    def draw_label(self, pos, radius, label):
        return "\\fill[black] (%5.2f,0) circle(%5.2fcm) node [align=center, above, yshift=0.1cm]{%s};" % (self.scale_fact*pos, radius, label)

    def create_labels(self, n, shuffle = True):
        ret = []
        rr = np.arange(n)
        if shuffle:
            np.random.shuffle(rr)
            
        for i in rr:
            ret.append(chr(ord('A')+i))
        
        return ret
                       
    def draw_labels(self, f, radius = 0.1):
        lbls = self.create_labels(len(self.points_pos))
                       
        for lbl, pos in zip(lbls, self.points_pos):
            f.write(self.draw_label(pos, radius, lbl) + "\n");

    def draw_start_end_labels(self, f):
        f.write("\\draw (0,0)  node [align=center, below]{%s} node[align=center, above, yshift=0.1cm]{0};\n" % self.start_label)
        f.write("\\draw (%5.2f,0) node [align=center, below]{%s} node[align=center, above, yshift=0.1cm]{%d};\n" % (self.tlen*self.scale_fact, self.end_label, self.tlen))
            
    def draw(self, f):
        f.write("\\begin{tikzpicture}\n")
        f.write("\\draw (0,0) -- (%5.2f,0);\n" % (self.tlen*self.scale_fact))
        self.draw_ticks(f)
        self.draw_labels(f)
        self.draw_start_end_labels(f)
        f.write("\\end{tikzpicture}\n")


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

def print_answers(f, qs, a, shuffle = True):
    f.write("\\begin{question}\n")
    f.write (qs)
    f.write("\n")
    rr = np.arange(len(a))
    if shuffle:
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
    print_answers(f, qs, a)
    
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
    print_answers(f, qs, a)

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
    print_answers(f, qs, a)

#------------------------------
def mult1(m, n, swhat):
    qs = "There are %d students who brough %d %s to class. Which expression can be used to find the total number of toys that were brought to the play date?" % (m,n, swhat)
    a = [];
    corr = "$%d \\times %d$" % (m, n)
    a.append(corr)
    a.append("$%d + %d$" % (m,n) )
    a.append("$%d \\times %d$" % (m,m))
    a.append("$%d \\times %d$" % (n,n))
    print_answers(f, qs, a)

#------------------------------
def cover1(n, side):
    qs = "A rectangle can be covered completely by %d square pieces of paper without gaps or overlaps. If each piece of paper has the side length of %d feet, what is the total area of the rectangle?" % (n,side)
    a = [];
    corr = side*side*n
    a.append(corr)
    a.append(n*n*side)
    a.append(n*side)
    a.append(n)
    print_answers(f, qs, a)

def time1(hh, mm, diff):
    tm = BasicTime(hh, mm)
    rr = np.arange(len(gnames))
    np.random.shuffle(rr)
    n1 = gnames[rr[0]]
    n2 = gnames[rr[1]]
    earlier_or_later = "earlier" if diff < 0 else "later"
    qs = "%s and %s both run the same race.  %s finished %d minutes %s than %s. If %s finished at %s, what time did %s finish the race?" % (n1, n2, n1, abs(diff), earlier_or_later, n2, n2, str(tm), n1)
    a = [];
    corr = tm.add_mins(diff)
    a.append(str(corr))
    a.append(str(tm.add_mins(-diff)))
    a.append(str(tm.add_mins(diff+1)))
    a.append(str(tm.add_mins(diff-2)))
    print_answers(f, qs, a)

def dist1(tlen, label_names, ndivs, loc_pos, dist_to_0 = True, scale_fact=4):
    # create random points
    pts = np.arange(ndivs)
    
    pts = np.delete(pts, [0, loc_pos])
    locs = np.random.choice(pts, 3, replace=False)
    print(locs, loc_pos)
    locs = np.append(locs, loc_pos)
    # pick a name
    rr = np.arange(len(gnames))
    np.random.shuffle(rr)
    n1 = gnames[rr[0]]
    
    distance_str = "mile" if tlen == 1 else "miles"
    f.write("\\begin{question}\n")
    f.write("The distance between %s's %s and her %s is exactly %d %s as shown on the number line below " % (n1, label_names[0].lower(), label_names[1].lower(), tlen, distance_str))
    f.write("\\vspace{0.1in}\n")
    f.write("\\begin{center}\n")
    nl = NumberLine(1, label_names[0], label_names[1], locs/float(ndivs), ndivs, scale_fact)
    nl.draw(f)
    f.write("\\end{center}\n")
    qdist = loc_pos if dist_to_0 else ndivs - loc_pos
    frac_str = "$\\frac{%d}{%d}$ miles" % (qdist, ndivs)
    to_str = label_names[0] if dist_to_0 else label_names[1]
    f.write("%s buys %s at %s which is exactly %s from %s. What point on the number line show the location of the %s?\n" % (n1, label_names[2].lower(), label_names[3], frac_str, to_str.lower(), label_names[3]))
    f.write("\\begin{choices}\n")
    for a in ['A', 'B', 'C', 'D']:
        f.write("\\choice %s\n" % a)
    f.write("\\end{choices}\n")
    f.write("\\end{question}\n")

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

roundq(274, "The distance between two cities", "miles", 2)

eqn_true(6, 4, dv=True)

mult1(7, 3, "toy cars")

cover1(12, 2)

time1(14, 2,-7)

dist1(1, ["Home", "School", "ice cream", "store"], ndivs=8, loc_pos=3, dist_to_0 = True, scale_fact=4)
dist1(1, ["Home", "Grandparents", "candy", "store"], ndivs=8, loc_pos=6, dist_to_0 = False, scale_fact=4)
#nl = NumberLine(1, "Home", "School", [1/8.0, 3/8.0, 5/8.0, 7/8.0], 8, scale_fact=4)
#nl.draw(f)

end(f)
f.close()
