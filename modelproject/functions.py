

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



def help_br(q, c, a, b): #defining a help function that finds where the Best response functions - q are equal to 0 (i.e. fixed points)
    return [q[0]-best_response(q[1], c[0], a, b),q[1]-best_response(q[0], c[1], a, b)]


def production_eq(c, initial_guess, a, b): #Equilibrium function 
    Q = optimize.fsolve(lambda q: help_br(q, c, a, b), initial_guess)
    return Q