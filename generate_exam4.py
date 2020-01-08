import generate_exam_fns as gef
import sys
import numpy as np
import io

## Main---------------------------
if len(sys.argv) <= 1:
    print("Need a file name");
    sys.exit()
    
Ngen = 20
if len(sys.argv) >= 3:
    Ngen = int(sys.argv[2])

seed = 0
if len(sys.argv) >= 4:
    seed = int(sys.argv[3])
np.random.seed(seed)
    
f = open(sys.argv[1], "w")
gef.set_file_handle(f)

gfuncs = [gef.mult_or_div,
          gef.frac_multiply,
          gef.multiple_less_than,
          gef.true_comparison,
          gef.multi_part_diff,
          gef.basic_shapes
]

gef.start()

fchoices = np.random.choice(np.arange(len(gfuncs)), Ngen)
print(fchoices)
for i in fchoices:
    gfuncs[i]()

#gef.bar_chart({"Blue" : 2, "Grey": 7, "Brown" : 9, "Green" : 1}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True)

#gef.bar_chart({"Blue" : 3, "Grey": 6, "Brown" : 9, "Green" : 0}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True, put_qmark_last = True)

gef.end()
f.close()
