import generate_exam_fns as gef
import sys
import numpy as np
import io

## Main---------------------------
if len(sys.argv) <= 1:
    print("Need a file name");
seed = 0
if len(sys.argv) >= 3:
    seed = int(sys.argv[2])
np.random.seed(seed)
    
f = open(sys.argv[1], "w")
gef.set_file_handle(f)

gef.start()

inp = np.random.choice(np.arange(2,12), 3, replace=False)
gef.expr1_mult(inp[0]*inp[2], inp[1], inp[2])

inp = np.random.choice(np.arange(11,89), 1)
inp = 100*np.random.choice(np.arange(1,10), 1) + inp
gef.roundq(inp[0], "The distance between two cities", "miles",  np.random.choice([1,2],1)[0])

inp = np.random.choice(np.arange(4,9), 2, replace=False)
gef.eqn_true(inp[0], inp[1], dv = True)

inp = np.random.choice(np.arange(4,13), 2, replace=False)
gef.mult1(inp[0], inp[1], np.random.choice(["mechanical pencils", "toy cars", "tennis balls"]))

gef.cover1(np.random.choice(np.arange(6,20)), np.random.choice([1,2]))

hh = np.random.choice(np.arange(12,16))
mm = np.random.choice(np.arange(1,25))
diff = -np.random.choice(np.arange(mm,mm+10))
gef.time1(hh, mm, diff)

ndivs = np.random.choice([6, 8,10])
loc_pos = np.random.choice([1,2,3])
what = np.random.choice(["ice_cream", "candy", "toy", "donuts", "juice"])
gef.dist1(1, ["Home", "School", what, "store"], ndivs, loc_pos, dist_to_0 = np.random.choice([True, False]), scale_fact=4)
ndivs = np.random.choice([6, 8,10])
loc_pos = np.random.choice([1,2,3])
what = np.random.choice(["ice_cream", "candy", "toy", "donuts", "juice"])
gef.dist1(1, ["Home", "School", what, "store"], ndivs, loc_pos, dist_to_0 = np.random.choice([True, False]), scale_fact=4)

#nl = NumberLine(1, "Home", "School", [1/8.0, 3/8.0, 5/8.0, 7/8.0], 8, scale_fact=4)
#ss = io.StringIO()
#nl.draw(ss)
#print(ss.getvalue())
ndivs = np.random.choice([6, 8, 10])
denom = int(ndivs / np.random.choice([1,2]))
num = np.random.choice(np.arange(1, denom))
gef.which_nl(num, denom, ndivs, scale_fact = 8)

ndivs = np.random.choice([6, 8, 10])
denom = int(ndivs / np.random.choice([1,2]))
num = np.random.choice(np.arange(1, denom))
gef.which_nl(num, denom, ndivs, scale_fact = 8)

gef.last_and_this_week(4, 3, 5, 2)

gef.rnd_what_situation()

hh = np.random.choice(np.arange(12,16))
mm = np.random.choice(np.arange(1,25))
diff = -np.random.choice(np.arange(mm,mm+10))
gef.time1(hh, mm, diff)

inp = np.random.choice(np.arange(11,89))
inp = 100*np.random.choice(np.arange(1,10)) + inp
gef.roundq(inp, "The cost of a new phone", "dollars", 2)

gef.pattern(np.random.choice(np.arange(1,10)), np.random.choice([2,3,4,5]))

gef.mult_basic("shopping center", 5, "floors", 25, "stores", end_q="")

gef.small_and_big(1, 3, 2, 1)
gef.small_and_big(1, 3, 2, 3)

denoms = np.random.choice(np.arange(2,9),2, replace = False)
num1 = np.random.choice(np.arange(1,denoms[0]))
num2 = np.random.choice(np.arange(1,denoms[1]))
gef.frac_comparison(num1, denoms[0], num2, denoms[1])

inp = np.random.choice(np.arange(2,12), 3, replace=False)
gef.expr1_mult(inp[0]*inp[2], inp[1], inp[2])

gef.rnd_what_situation()

gef.pattern(np.random.choice(np.arange(1,10)), np.random.choice([2,3,4,5]))

gef.rnd_what_situation()

gef.bar_chart({"Blue" : 2, "Grey": 7, "Brown" : 9, "Green" : 1}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True)

gef.bar_chart({"Blue" : 3, "Grey": 6, "Brown" : 9, "Green" : 0}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True, put_qmark_last = True)

gef.time2(14, 28, 30, arrive = True)

gef.garden_area(5,9,4,6, True)

gef.end()
f.close()
