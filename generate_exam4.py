import generate_exam_fns as gef
import sys
import numpy as np
import io

def preprocess_funcs(fdict):
    flist = []
    for f, mult in fdict.items():
        for _ in np.arange(mult):
            flist.append(f)
    return flist
    

    
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

gfuncs_dict = {gef.mult_or_div : 2,
               gef.frac_multiply : 2,
               gef.multiple_less_than : 1,
               gef.true_comparison : 2,
               gef.multi_part_diff : 1,
               gef.basic_shapes : 1,
               gef.frac_box : 1,
               gef.rnd_roundq : 1, 
               gef.angle_math : 2,
               gef.closest_answer : 2,
               gef.perimeter_rect : 2,
               gef.angle_math_circle : 1,
               gef.compass : 1
}

gfuncs = preprocess_funcs(gfuncs_dict)

gef.start()

fchoices = np.random.choice(np.arange(len(gfuncs)), Ngen)
print(fchoices)
for i in fchoices:
    gfuncs[i]()

#gef.bar_chart({"Blue" : 2, "Grey": 7, "Brown" : 9, "Green" : 1}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True)

#gef.bar_chart({"Blue" : 3, "Grey": 6, "Brown" : 9, "Green" : 0}, "Eye color", ["Grey", "Brown"], ["Blue", "Green"], "eyes", show_work = True, put_qmark_last = True)

gef.end()
f.close()
