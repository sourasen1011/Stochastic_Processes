# Imports
import numpy as np
import matplotlib.pyplot as plt

# define hpp function
def gen_hpp(lmbda ,  N):
    '''
    param lmbda: rate parameter
    N: Number of events
    '''
    # inits
    t = [0]

    # begin loop
    while True:
        u = np.random.uniform(0,1) # generate uniform r.v. ~ Unif[0,1]
        w = - np.log(u)/lmbda # generate w ~ Exponential(lambda)
        t.append(t[-1] + w)
        if len(t) > N:
            return t , np.arange(len(t)) # get time to event & count the number of events

if __name__ == '__main__': # main namespace
    l , N = 8 , 1000
    hpp_event_times , events = gen_hpp(lmbda = l , N = N) # generate the time(s) to event(s) AND count of events 
    print(max(events) , max(hpp_event_times)) # debug
    
    # Make plots
    fig , ax = plt.subplots()
    ax.step(hpp_event_times , events , label = f"$\lambda$ = {l}") # step graph
    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$N(t)$')
    ax.set_title('Homogeneous Poisson process')
    ax.legend(loc='best')
    plt.show()