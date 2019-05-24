def rnd(a): # Function to print floats rounded as strings
    return str("{:.0f}".format(a))



def price(q1, q2, a, b): #Overall inverse demand function as a function of all quantities and the relevant parameters
    price = a-b*(q1+q2)
    return price

def cost(q, c): #A cost function for a given firm
    cost = q*c
    return cost

def profit(q1, q2, a, b, c): #Profit for a given firm with production q1 and costs c
    profit = price(q1, q2, a, b)*q1-cost(q1, c)
    return profit


def best_response(q2, c1, a, b): #best response for firm 1 - found by maximising profits taking q2 as given
    from scipy import optimize
    q1 =  optimize.fminbound(lambda x: -profit(x, q2, a, b, c1), # minimizing minus profits
                             0, #lower bound is zero
                             a, #upper bound is a (should maybe include a-b*x ?)
                             full_output=True,
                            disp=True)
    return q1[0]

def best_reponse_plot(a, b, c1): #plots the best response function
    from scipy import optimize, arange
    import matplotlib.pyplot as plt
    
    range_q2 = arange(0, a, 0.01)
    range_q1 = [best_response(q2, c1, a, b) for q2 in range_q2]
    
    plt.plot(range_q1, range_q2)
    plt.xlabel("best response q1")
    plt.ylabel('q2')
    plt.title("Firm 1's best response to firm 2")


def help_br(q, c, a, b): #defining a help function that finds where the Best response functions - q are equal to 0 (i.e. fixed points)
    return [q[0]-best_response(q[1], c[0], a, b),q[1]-best_response(q[0], c[1], a, b)]


def production_eq(c, initial_guess, a, b): #Equilibrium function - solves fixed points in equilibrium
    from scipy import optimize
    Q = optimize.fsolve(lambda q: help_br(q, c, a, b), initial_guess)
    return Q


def summary(c, a, b, initial_guess):
    q1,q2 = production_eq(c, initial_guess, a, b) #Equilibrium productions   
     
    output = print('\n Industry output is ' + str("{:.0f}".format(q1+q2)) + ' with firm 1 producing ' + str("{:.0f}".format(q1)) + ' units and firm 2 producing ' +
                   str("{:.0f}".format(q2)) + ' units.' + 
                   '\n The equilibrium price per unit becomes ' + str("{:.0f}".format(price(q1, q2, a, b))) +
                  "\n Firm 1's profit will be " + str("{:.0f}".format(profit(q1, q2, a, b, c[0]))) + " while firm 2's profit will be " + str("{:.0f}".format(profit(q1, q2, a, b, c[1]))))
    return output

################################################################################################################################################################################################## Analytical solutions ##################################################################################################################################################################################################

def price_eq(a, n, c): #Returns equilibirum price
    
    price = max((a-sum(c))/(1+n), 0)
    return price


def qi_eq(a, b, n, c, i): #Returns equilibrium quantity for firm i
    
    q_i = max((1/b)*((a-n*c[i]+(sum(c)-c[i]))/(1+n)), 0)
    if q_i < 1: #To avoid solutions with low quantities
        q_i = 0
        
    return q_i


def Q_eq(a, b, n, c): #Returns industry quantity
    
    #Q_alt = (n*a-sum(c))/(b*(1+n))
    Q = []
    for i in range(0, n+1, 1):
        Q.append(qi_eq(a, b, n, c, i))
        
    return sum(Q)

def profit_eq(a, b, n, c, i): #Returns profit for firm i
    
    if qi_eq(a, b, n, c, i) == 0: #Profits set to zero if no production
        profit = 0
    else:
        profit = max((1/b)*(((a-n*c[i]+(sum(c)-c[i]))/(1+n))**2), 0)
        
    return profit



def sim_general(a, b, N, c_low, c_high): # N is the max number of firms. c_low and c_high denotes to range of the uniformly distributed costs
    #Dependencies
    import numpy as np
    import random
    import matplotlib.pyplot as plt
    
    n = random.randint(2, N) #Number of firms - can be from monopoly to perfect competition depending on the draw (and N)
    
    #Assymmetric costs for each firm:
    c = []
    for i in range(0, n+1, 1):
        c_i = random.uniform(c_low, c_high)
        c.append(c_i)
    
    price = price_eq(a, n, c) #equilibrium price
    
    #individual quantities and profits
    qi_list = []
    profiti_list = []
    for i in range(0, n+1, 1):
        qi_list.append(qi_eq(a, b, n, c, i))
        profiti_list.append(profit_eq(a, b, n, c, i))
   
    
    #Industry quantity
    Q = Q_eq(a, b, n, c)

    
    #Mark-ups - the multiplier on marginal costs
    markup_i = []
    for i in range(0, n+1, 1):
        markup_i.append(price/c[i])
    
    
    
    #Plots of each firm's profit
    plt.bar(x=range(0, n+1, 1), height=profiti_list)
    plt.xlabel("Firm i")
    plt.ylabel('Profit for firm i')
    plt.title("Profits for each firm")
    

    #Text summuary
    output = print('\n The industry consists of ' + rnd(n) + ' competiting firms.' + 
                  '\n Industry quantity produced is ' + rnd(Q) + ' with an equilibrium price of ' + rnd(price) + 
                   '\n The average profits are ' + rnd(np.array(profiti_list).mean()) + ' with an average mark-up over marginal costs of ' + 
                   str("{:.2f}".format(np.array(markup_i).mean())) +
                   '\n'
                   
                  )
    
    return output