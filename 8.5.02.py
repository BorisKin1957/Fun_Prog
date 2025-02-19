def merge_generators(*args):
    for gen in args:
        yield from gen
        # for value in gen:
        #     yield value



gen_1 = (x for x in range(3))
gen_2 = (x for x in "abc")

merged_gen = merge_generators(gen_1, gen_2)
for value in merged_gen:
    print(value)

gen_1 = (x for x in range(3))
gen_2 = (x for x in "abc")
gen_3 = (x for x in [True, False])

merged_gen = merge_generators(gen_3, gen_1, gen_2, )
print(list(merged_gen))