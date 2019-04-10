import generate_exam_fns as gef
import sys
import numpy as np
import io

## Main---------------------------
if len(sys.argv) <= 1:
    print("Need a file name");
    
Ngen = 20
if len(sys.argv) >= 3:
    Ngen = int(sys.argv[2])

seed = 0
if len(sys.argv) >= 4:
    seed = int(sys.argv[3])
np.random.seed(seed)
    
f = open(sys.argv[1], "w")
gef.set_file_handle(f)

gfuncs = [gef.rnd_expr_mult1,
          gef.rnd_mult_basic,
          gef.rnd_roundq,
          gef.rnd_eqn_true,
          gef.rnd_mult1,
          gef.rnd_cover1,
          gef.rnd_time1,
          gef.rnd_time2,
          gef.rnd_dist1,
          gef.rnd_which_nl,
          gef.rnd_which_nl,
          gef.rnd_last_and_this_week,
          gef.rnd_small_and_big,
          gef.rnd_frac_comparison,
          gef.rnd_what_situation,
          gef.rnd_pattern,
          gef.rnd_garden_area,
          gef.rnd_equiv_frac,
          gef.rnd_spinner_game,
          gef.rnd_bar_chart,
          gef.rnd_buying,
          gef.rnd_roundq2
]

gef.start()

fchoices = np.random.choice(np.arange(len(gfuncs)), Ngen)
for i in fchoices:
    gfuncs[i]()

#gef.bar_chart({"Blue" : 2, "Grey": 7, "Brown" : 9, "Green" : 1}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True)

#gef.bar_chart({"Blue" : 3, "Grey": 6, "Brown" : 9, "Green" : 0}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True, put_qmark_last = True)

gef.end()
f.close()
