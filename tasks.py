# 208539270 yardenbakish
# 208983700 tamircohen1

"""tasks.py - invoke tasks file. This file oversees building our C extension and
running our entire program and execute it."""

"""MAX CAPACITY - upon countles errors and trials with the n,k values handled over a span of several weeks, the best
outcome for the max_capacity, mainly measured by the running times (under 5 minutes), but also by the quality of the clustering
was n=435, k=20. the dimentions had zero to None effect on the running-times."""


from invoke import task, call

#our main wrapper task
@task
def run(c, k=None, n=None, Random = True):
    """if Random is True n and k doesnt matter - pass along arbitrary values"""
    if (Random==True):
        k=2
        n=3
    """if Random is False the following must not happen. if it does,we print message and exit"""
    if (Random==False):
        if k==None: #if Random is False - you must insert k
            print("k argument was not supplied")
            exit(0)
        if n==None: #if Random is False - you must insert n
            print("n argument was not supplied")
            exit(0)
        if (int(k) >= int(n)):
            print("k cannot be greater or equal to n")
            exit(0)
        if ((int(k)<=0) or (int(n)<=0)):
            print("k and n cannot be equal or less than 0")
            exit(0)
    #informative message stating maximum capacity for each dimention
    print("Maximum capacity:")
    print("k = 20 and n = 435 for 3-dimensional")
    print("k = 20 and n = 435 for 2-dimensional")
    c.run("python3.8.5 setup.py build_ext --inplace")
    print("Done building")
    #pass integer to main module - if Random is True pass 1, otherwise pass 0
    if (Random==True):
        c.run(f"python3.8.5 main.py {k} {n} {1}")
    else:
        c.run(f"python3.8.5 main.py {k} {n} {0}")

    
#deleting any previous .so file or our C extension
@task(aliases=['del'])
def clear(c):
     c.run("rm *mykmeanssp*.so")
