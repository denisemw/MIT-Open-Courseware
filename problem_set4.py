def nestEggFixed (salary, save, growthRate, years):
    l = [salary*save*0.01]
    for i in range(1,years):
        l.append(l[i-1]*(1+0.01*growthRate) + salary*save*.01)
    return l

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    l = [salary*save*0.01]
    for i in range(1,len(growthRates)):
        l.append(l[i-1]*(1+0.01*growthRates[i]) + salary*save*.01)
    return l
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    l = [savings*(1+0.01*growthRates[0]) - expenses]
    for i in range(1,len(growthRates)):
        l.append(l[i-1]*(1+0.01*growthRates[i]) - expenses)
    return l

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.

      Use the idea of binary search to

      find a value for the amount of expenses you can withdraw each year from your retirement fund,
      such that at the end of your retirement, the absolute value of the amount remaining
      in your retirement fund is less than epsilon

      (note that you can overdraw by a small amount).


      PSEUDOCODE:

      find some value x, such that:
      growthRates = preRetireGrowthRates + postRetireGrowthRates

      choose a guess for x
      
      while True:
          if epsilon >= abs(postRetirement(savings, growthRates, x)):
              break
          elif postRetirement(savings, growthRates, x) > epsilon:
              choose new guess in the middle of guess - savings
          else:
              choose new guess in the middle of 0-guess
    """
    low = 0
    high = salary
    savings = nestEggVariable(salary, save, preRetireGrowthRates)[-1]

    while True:
        guess = (low+high)/2.0
        value = postRetirement(savings, postRetireGrowthRates, guess)
        print guess
        raw_input()
        if value[-1] < 0:
            high = guess
        else:
            low = guess
        if epsilon > abs(value[-1]):
            return guess     


def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
