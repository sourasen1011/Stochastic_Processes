# Imports
import numpy as np
import matplotlib.pyplot as plt

# define hpp function
def gen_nhpp(lmbda_bar = 8 ,  T = 140):
    '''
    param lmbda_bar: rate parameter that 
    dominates the rate param of the NHPP
    T : maximum time
    '''
    # inits
    s = [0]
    t = [0]

    # begin loop
    while s[-1] < T:
        # generate uniform r.v. ~ Unif[0,1]
        u = np.random.uniform(0,1)
        # generate w ~ Exponential(lambda) 
        w = - np.log(u)/lmbda_bar 
        s.append(s[-1] + w)
        # geenrate D ~ Unif[0,1]
        D = np.random.uniform(0,1)
        # acceptance criterion
        if D < (1.01)**s[-1] / lmbda_bar:
            t.append(s[-1])
        
        if t[-1] > T:
            num_events = np.arange(len(t[:-1]))
            print(f'Breakpoint 1: the number of events is {num_events[-1]}, and the time taken to reach them is {t[:-1][-1]}')
            # get time to event & count the 
            # number of events
            return t[:-1] , num_events
    else:
        num_events = np.arange(len(t))
        print(f'Breakpoint 2: the number of events is {num_events[-1]}, and the time taken to reach them is {t[-1]}')
        # get time to event & count the number 
        # of events
        return t , num_events

# main namespace
if __name__ == '__main__': 
    # generate the time(s) to event(s) 
    # AND count of events
    nhpp_event_times , events = gen_nhpp() 
    # Make plots
    fig , ax = plt.subplots()
    # step graph
    ax.step(nhpp_event_times , events , 
            label = f'$\lambda(t) = (1.01)^t$') 
    # Integrating the rate function to get E[N(t)]
    x = np.arange(140)
    y = 1.01**x/np.log(1.01) - (1.01)**0/np.log(1.01)
    ax.plot(x , y , label = r'E[N(t)] = $\frac{1.01^t}\
            {ln(1.01)}$ - 100.499')
    # Auxiliaries
    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$N(t)$')
    ax.set_title('Non-Homogeneous \
                 Poisson process')
    ax.legend(loc='best')
    plt.show()