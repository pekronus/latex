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

gef.rnd_expr_mult1()

gef.rnd_roundq("The distance between two cities", "miles")


gef.rnd_eqn_true()
gef.rnd_eqn_true()
gef.rnd_eqn_true()

gef.rnd_mult1()

gef.rnd_cover1()

gef.rnd_time1()

gef.rnd_dist1()

gef.rnd_dist1()

gef.rnd_which_nl()

gef.rnd_which_nl()

gef.rnd_which_nl()

gef.rnd_last_and_this_week()

gef.rnd_what_situation()

gef.rnd_time1()

gef.rnd_roundq("The cost of a new phone", "dollars")

gef.rnd_pattern()

gef.mult_basic("shopping center", 5, "floors", 25, "stores", end_q="")

gef.rnd_small_and_big()
gef.rnd_small_and_big()

gef.rnd_frac_comparison()
gef.rnd_frac_comparison()

gef.rnd_expr_mult1()

gef.rnd_what_situation()

gef.rnd_pattern()

gef.rnd_what_situation()

gef.bar_chart({"Blue" : 2, "Grey": 7, "Brown" : 9, "Green" : 1}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True)

gef.bar_chart({"Blue" : 3, "Grey": 6, "Brown" : 9, "Green" : 0}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True, put_qmark_last = True)

gef.rnd_time2()
gef.rnd_time2()

gef.rnd_garden_area()

gef.rnd_garden_area()

gef.end()
f.close()
