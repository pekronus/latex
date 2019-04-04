import sys
import numpy as np
import io

goperations  = ["/", "+", "-", "*"]

boys_names = {"John", "Juan", "Daniel", "Brian",  "Adam", "Michael"}
girl_names = {"Sally", "Esther",  "Monica", "Julia",  "Jessica"}
gnames = list(boys_names.union(girl_names))
f = None # file handle

def his_or_her(name):
    return "his" if name in boys_names else "her"

def set_file_handle(ff):
    global f
    f = ff

def print_show_work(vspace):
    show_work_str = """
Show your work.
\\vskip %din
\\begin{tikzpicture}
\\draw (5,0) -- (10,0);
\\draw (5,0) node[align=center, left]{Answer:};
\\end{tikzpicture}
\\vspace{10in} 
""" % vspace
    f.write(show_work_str)

#--------------------
def concat_items(item_list):
    mnames_cc = ""
    if (not item_list):
        return ""
    
    fst = True
    for n in item_list:
        if (not fst):
            mnames_cc += "and "
        fst = False
        mnames_cc += n.lower() + " "
    return mnames_cc[:-1]


def get_names(n):
    rr = np.arange(len(gnames))
    np.random.shuffle(rr)
    ret = []
    for i in np.arange(n):
        ret.append(gnames[rr[i]])
    return ret

def get_op():
    return goperations[np.random.choice(np.arange(4))]

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
            
    def draw(self, f, custom_labels={}):
        f.write("\\begin{tikzpicture}\n")
        f.write("\\draw (0,0) -- (%5.2f,0);\n" % (self.tlen*self.scale_fact))
        self.draw_ticks(f)
        if len(custom_labels) == 0:
            self.draw_labels(f)
        else:
            for pos, lbl in custom_labels.items():
                f.write(self.draw_label(pos, 0.01, lbl)+"\n")
        self.draw_start_end_labels(f)
        f.write("\\end{tikzpicture}\n")


def start():
    f.write("\\documentclass{exam}\n")
    f.write("\\newcommand{\\qm}{\\underline{\\hspace{0.3cm}?\hspace{0.3cm}}}\n");
    f.write("\\usepackage{tikz}\n")
    f.write("\\usepackage{amsmath}\n")
    f.write("\\usepackage{pgfplots}\n")
    f.write("\\begin{document}\n")
    f.write("""\\begin{center}
	\\fbox{\\fbox{\\parbox{5.5in}{\centering
				Read the questions carefully. For multiple choice circle the letter corresponding to the answer}}}
\\end{center}\n\n""")
    f.write("""\\vspace{0.1in}
\\makebox[\\textwidth]{Student name:\\enspace\\hrulefill}\n\n""")
    f.write("\\begin{questions}\n")

#--------------------
def end():
    f.write("""\end{questions}
\end{document}\n""")

def print_choices(a, shuffle=True):
    rr = np.arange(len(a))
    if shuffle:
        np.random.shuffle(rr)
    f.write("\\begin{choices}\n")
    for i in rr:
        f.write("\\choice %s\n" % a[i])
    f.write("\\end{choices}\n")
    
def print_answers(f, qs, a, shuffle = True):
    f.write("\\begin{question}\n")
    f.write (qs)
    f.write("\n")

    print_choices(a, shuffle)
    
    f.write("\\end{question}\n\n")
#--------------------
def expr1_mult(x, y, d):
    qs = "What expression is another way of showing $ %d \\times %d $"  % (x,y)
    a = []
    a.append("$(%d \\times %d \\times %d ) $" % (x, y, d))
    a.append("$(%d \\times %d) \\times %d  $" % (x/d+1, d, y))
    a.append("$(%d \\times %d) \\times %d  $" % (x/d, d+1, y))
    a.append("$(%d \\times %d) \\times %d  $" % (x/d, d, y)) # correct
    print_answers(f, qs, a)

def mult_basic(something, n, name_of_container, m, name_of_object, end_q):
    qs = "A %s has %d %s that each can hold %d %s. What is the total number of %s %s?" % (something, n, name_of_container, m, name_of_object, name_of_object, end_q)
    a = []
    adds = np.random.choice(np.arange(-10, 10), 2, replace = False)
    a.append(str(m*n))
    a.append(str(m+n))
    a.append(str(m*n + adds[0]))
    a.append(str(m*n + adds[1]))
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
    qs = "There are %d students who brough %d %s to class. Which expression can be used to find the total number of %s that were brought to the class by the students?" % (m,n, swhat, swhat)
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

def time2(hh, mm, travel_time, arrive = True):
    tm = BasicTime(hh, mm)
    rr = np.arange(len(gnames))
    np.random.shuffle(rr)
    n1 = gnames[rr[0]]
    pronoun1 = "He" if n1 in boys_names else "She"
    n2 = gnames[rr[1]]
    if arrive:
        qs = "%s met %s at the library at exactly %s.  It takes %s %d minutes to walk from school to the library. What time did %s leave the school?" % (n1, n2, str(tm), n1, travel_time, n1)
    else:
        qs = "It takes %s %d minutes to walk from school to home. %s left the school at %s. At what time will %s get home?" % (n1, travel_time, str(tm), pronoun1, str(tm), n1)
    a = [];
    corr = tm.add_mins(-travel_time) if arrive else tm.add_mins(travel_time)
    incorr = tm.add_mins(travel_time) if arrive else tm.add_mins(-travel_time)
    adds = np.random.choice([-5, -4, -3, -2,-1, 1, 2, 3, 4, 5], 2, replace = False)
    a.append(str(corr))
    a.append(str(incorr))
    a.append(str(corr.add_mins(adds[0])))
    a.append(str(corr.add_mins(adds[1])))
    print_answers(f, qs, a)

def dist1(tlen, label_names, ndivs, loc_pos, dist_to_0 = True, scale_fact=4):
    # create random points
    pts = np.arange(ndivs)
    pts = np.delete(pts, [0, loc_pos])
    locs = np.random.choice(pts, 3, replace=False)
    locs = np.append(locs, loc_pos)
    # pick a name
    rr = np.arange(len(gnames))
    np.random.shuffle(rr)
    n1 = gnames[rr[0]]
    pronoun1 = "his" if n1 in boys_names else "her"
    
    distance_str = "mile" if tlen == 1 else "miles"
    f.write("\\question\n")
    f.write("The distance between %s's %s and %s %s is exactly %d %s as shown on the number line below " % (n1, label_names[0].lower(), pronoun1, label_names[1].lower(), tlen, distance_str))
    f.write("\\vspace{0.1in}\n")
    f.write("\\begin{center}\n")
    nl = NumberLine(1, label_names[0], label_names[1], locs/float(ndivs), ndivs, scale_fact)
    nl.draw(f)
    f.write("\\end{center}\n")
    qdist = loc_pos if dist_to_0 else ndivs - loc_pos
    frac_str = "$\\frac{%d}{%d}$ miles" % (qdist, ndivs)
    to_str = label_names[0] if dist_to_0 else label_names[1]
    f.write("%s buys %s at %s which is exactly %s from %s. What point on the number line shows the location of the %s?\n" % (n1, label_names[2].lower(), label_names[3], frac_str, to_str.lower(), label_names[3]))
    f.write("\\begin{choices}\n")
    for a in ['A', 'B', 'C', 'D']:
        f.write("\\choice %s\n" % a)
    f.write("\\end{choices}\n")


def which_nl(num, denom, ndivs, scale_fact = 8):
    corr_pos = num*ndivs/denom
    # create random points
    pts = np.arange(ndivs)
    pts = np.delete(pts, [0, int(corr_pos)])
    locs = np.random.choice(pts, 3, replace=False)
    locs = np.append(locs, corr_pos)

    lbl = "$\\frac{%s}{%s}$" % (num, denom)
    qs = "Which number line shows the fraction %s correctly?" % (lbl)

    a = [];
    nl = NumberLine(1, "", "", [], ndivs, scale_fact)
    for l in locs:
        custom_labels = {float(l)/ndivs : lbl}
        ss = io.StringIO()
        nl.draw(ss, custom_labels)
        a.append(ss.getvalue())
        ss.close()

    print_answers(f, qs, a)
    
#------------------------------
def last_and_this_week(n1,d1,n2,d2):
    name = get_names(1)[0]
    pronoun = "he" if name in boys_names else "she"
    qs = "Last week %s ate %d chocolates a day for %d days.  This week, %s ate %d chocolates a day for %d days. Which expression can be used to represent the total number of chocolates %s ate in the last two weeks?\n" % (name, n1, d1, pronoun, n2, d2, name)
    a = [];
    corr = "$%d \\times %d + %d \\times %d$" % (n1,d1,n2,d2)
    a.append(corr)
    a.append("$(%d + %d) \\times (%d + %d)$" % (n1,d1,n2,d2))
    a.append("$%d \\times %d \\times %d \\times %d$" % (n1,d1,n2,d2))
    a.append("$%d + %d + %d + %d$" % (n1,d1,n2,d2))
    print_answers(f, qs, a)

def small_and_big(num, den, num2, den2):
    name = get_names(1)[0]
    pronoun = "He" if name in boys_names else "She"
    pronoun2="his" if name in boys_names else "her"
    plural = "s" if num2/den2 > 1 else ""
    bottle_vlm_str = str(int(num2/den2)) if (num2 % den2 == 0) else "$\\frac{%d}{%d}$" % (num2, den2)
    qs = "%s has a cup that holds exactly $\\frac{%d}{%d}$ liters of water. %s has a bottle that holds %s liter%s of water. How many times does %s need to pour %s cup into the bottle to fill it completely?" % (name, num, den, pronoun, bottle_vlm_str, plural, pronoun.lower(), pronoun2)
    a = []
    add = np.random.choice(np.arange(1, 4), 1)
    a.append(str(int((num2*den)/num/den2)))
    a.append(str(1))
    a.append("$\\frac{%d}{%d}$" % (num, den))
    a.append(str(int((num2*den)/num/den2 + add[0])))
    print_answers(f, qs, a)

def frac_comparison(n1, d1, n2, d2):
    names = get_names(2)
    pronoun1 = "his" if names[0] in boys_names else "her"
    pronoun2 = "his" if names[1] in boys_names else "her"
    qs = "%s and %s got identical pizzas. %s ate $\\frac{%d}{%d}$ of %s pizza, while %s  ate $\\frac{%d}{%d}$ of %s pizza. Which statement shows a correct comparisons of the portions of pizza that % and %s ate?" % (names[0], names[1], names[0], n1, d1, pronoun1, names[1], n2, d2, pronoun2, names[0], names[1])
    a = []
    a.append("$\\frac{%d}{%d} = \\frac{%d}{%d}$" % (n1,d1,n2,d2))
    a.append("$\\frac{%d}{%d} < \\frac{%d}{%d}$" % (n1,d1,n2,d2))
    a.append("$\\frac{%d}{%d} > \\frac{%d}{%d}$" % (n1,d1,n2,d2))
    a.append("$\\frac{%d}{%d} + \\frac{%d}{%d}$" % (n1,d1,n2,d2))
    print_answers(f, qs, a)

def what_situation(n1, n2, op = '/'):
    sop = op
    if op == "/":
        sop = "\\div"
    elif op == "*":
        sop = "\\times"

    name = get_names(1)[0]
    pronoun ="his" if name in boys_names else "her"
    
    qs = "What situation can be solved by using the expression $%d %s %d$?" % (n1, sop, n2)
    a = []
    a.append("Finding the total number of cars where there are %d groups of %d cars" % (n1, n2))
    a.append("Finding the number of candies when there is a group of %d candies and a group of %d candies" % (n1, n2))
    a.append("Finding the number of boys in a class when there is a total of %d students and %d of them are girls" % (n1, n2))
    a.append("Finding the number of hours it takes for %s to bike to school if %s school is %d miles away and %s's speed on %s bike is %d miles per hour" % (name, pronoun, n1, name, pronoun, n2))
    print_answers(f, qs, a)

def rnd_what_situation():
    ns = np.random.choice(np.arange(3, 12),2, replace=False)
    n1 = ns[0]*ns[1]
    n2 = ns[1]
    ops = get_op()
    what_situation(n1, n2, ops)
    
#------------------------------
def pattern(start, add):
    p = np.arange(6)*add + start
    pstr = ""
    for n in p:
        pstr += str(n) + ","
    qs = """A number pattern is shown below:

%s

Which rule could have been used to make the pattern?""" % pstr[:-1]
    a = []
    a.append("Start with %d. Add %d each time to get the next number." % (start, add)) # correct
    a.append("Start with %d. Add %d each time to get the next number." % (start+1, add-1)) 
    a.append("Start with %d. Add %d each time to get the next number." % (start, add+1)) 
    a.append("Start with %d. Add %d each time to get the next number." % (0, add)) 
    print_answers(f, qs, a)


#--------------------
def draw_bar_chart(categories, x_label, y_label, put_qmark_last = False):

    symb_str = ""
    plot_data_str =""
    for key, val in categories.items():
        symb_str += key + ","
        plot_data_str += "(" + key + ", " + str(val) + ") "

    symb_str = symb_str[:-1]

    w = 1.5*len(categories.keys()) + 2
    width = int(max(min(15, w), 12))
    qloc = width - 2.5
    ostr = """\\begin{tikzpicture}
\\begin{axis}[
ybar,
symbolic x coords={%s},
xtick=data,
bar width = 1.5cm,
xlabel=%s,
ylabel=%s,
width=%dcm,
ymajorgrids = true
]
\\addplot coordinates{%s};

\\end{axis}


""" % (symb_str, x_label, y_label, width, plot_data_str)
    if put_qmark_last:
        ostr += "\n\\draw (%3.2f,2)  node [align=center, above] {\\Huge \\bf ?};\n" % qloc
    ostr += "\\end{tikzpicture}\n"

    f.write(ostr)

    
    
#------------------------------
def bar_chart(categories, cat_type, pnames, mnames, obj_name, show_work = True, put_qmark_last = False):
    if show_work:
        f.write("\\newpage\n")
        f.write("\\question\n")
    ostr = "The chart below shows the information third grade students collected about the %s of students in their classroom. " % cat_type.lower()
    f.write(ostr + "\n\n");

    draw_bar_chart(categories, cat_type, "Number of students", put_qmark_last)

    cm = concat_items(mnames)
    cp = concat_items(pnames)
    mcombined = "combined" if len(mnames) > 1 else ""
    pcombined = "combined" if len(pnames) > 1 else ""

    if put_qmark_last:
        fewerby = np.random.choice(np.arange(1,3), 1)
        qs = "Find the number of students with %s %s if the total number of students that have %s %s  is %d fewer than the number of students with %s %s\n" % (mnames[-1].lower(), obj_name, cm, obj_name, fewerby, cp, obj_name)  
    else:
        qs1 = "How many fewer students have %s %s %s than students that have %s %s %s?\n" % (cm, obj_name, mcombined, cp, obj_name, pcombined)
        qs2 = "How many more students have %s %s %s than students that have %s %s %s?\n" % (cp, obj_name, pcombined, cm, obj_name, mcombined)
        qs = qs1 if np.random.choice([1,2] ,1) == 1 else qs2
    
    f.write("\n" + qs)
    if show_work:
        print_show_work(3)


def garden_area(wmin, wmax, hmin, hmax, no_scale = False):
    name = get_names(1)[0]
    f.write("\\question The shape of %s's garden is shown below.\n" % name)

    dmax = max(wmax, hmax)
    scale = 1 if no_scale else round(10.0/dmax, 1);
    s1 = """\\begin{center}
\\begin{tikzpicture}	
\\draw (0,0) -- (%5.2f,0) -- (%5.2f, %5.2f) -- (%5.2f,%5.2f) -- (%5.2f,%5.2f) -- (0, %5.2f) -- (0,0);
""" % tuple([scale*n for n in (wmax,  wmax, hmax, wmax - wmin, hmax, wmax - wmin, hmin, hmin)])
    f.write(s1 + "\n")

    s2 = """\\draw (%s,0) node[align=center, below, yshift=-0.2cm]{%d ft};
\\draw (%s,%s ) node[align=center, right, xshift=0.2cm, rotate=-90]{%d ft};
\\draw (%s,%s) node[align=center, above]{%d ft};
\draw (0,%s) node[align=center, left, rotate=90, yshift = 0.2cm]{4 ft};
\\end{tikzpicture}	
\\end{center}

What is the area, in square feet, of %s's garden?
""" % tuple([scale*n for n in (wmax/2,wmax,  wmax,hmax/2,hmax, wmin/2,hmin,wmin, hmin/2,hmin)])
    f.write(s2 + "\n")

    a = []
    a.append(str(hmin*wmax + (wmax-wmin)*(hmax-hmin))) # correct
    a.append(str(wmax*hmax))
    a.append(str(wmin*hmin))
    a.append(str(hmin*wmax))

    print_choices(a, shuffle=True)
    
def rnd_garden_area():
    pass
