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
gef.expr1_mult(12, 8, 4)

gef.roundq(274, "The distance between two cities", "miles", 2)

gef.eqn_true(6, 4, dv=True)

gef.mult1(12, 6, "mechanical pencils")

gef.cover1(14, 2)

gef.time1(14, 2,-7)

gef.dist1(1, ["Home", "School", "ice cream", "store"], ndivs=6, loc_pos=2, dist_to_0 = True, scale_fact=4)
gef.dist1(1, ["Home", "Grandparents", "candy", "store"], ndivs=8, loc_pos=6, dist_to_0 = False, scale_fact=4)
#nl = NumberLine(1, "Home", "School", [1/8.0, 3/8.0, 5/8.0, 7/8.0], 8, scale_fact=4)
#ss = io.StringIO()
#nl.draw(ss)
#print(ss.getvalue())
gef.which_nl(1, 4, ndivs=8, scale_fact = 8)
gef.which_nl(2, 3, ndivs=6, scale_fact = 8)

gef.last_and_this_week(4, 3, 5, 2)

gef.what_situation(10, 5, "+")

gef.time1(14, 58, 5)

gef.roundq(849, "The cost of an iPhone X", "dollars", 2)

gef.pattern(6, 3)

gef.mult_basic("shopping center", 5, "floors", 25, "stores", end_q="")

gef.small_and_big(1, 3, 2)

gef.frac_comparison(2, 6, 2, 5)

gef.expr1_mult(6, 4, 3)

gef.what_situation(18, 9, "/")

gef.pattern(3, 4)

gef.what_situation(6, 5, "*")

gef.bar_chart({"Blue" : 2, "Grey": 7, "Brown" : 9, "Green" : 1}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True)

gef.bar_chart({"Blue" : 3, "Grey": 6, "Brown" : 9, "Green" : 0}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True, put_qmark_last = True)

gef.time2(14, 28, 30, arrive = True)

gef.end()
f.close()
