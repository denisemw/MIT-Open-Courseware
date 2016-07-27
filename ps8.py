# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSloadSubjectsubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and parses the name,
    # value, and work of each subject and creates a dictionary mapping the name
    # to (value, work).

    inputFile = open(filename)
    subj_dir = {}
    for line in inputFile:
        line = line.strip()
        s = line.split(',')
        name = s[0]
        value = int(s[1])
        work = int(s[2])
        subj_dir[name] = (value, work)
    return subj_dir
        

    # TODO: Instead of printing each line, modify the above to 
def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """

    mutable_subjects = list(subjects.keys())
    d = {}
    
    while maxWork >= 0:
        maxVal = mutable_subjects[0]

        for subject in mutable_subjects:
            if comparator(subjects[subject], subjects[maxVal]):
                maxVal = subject

        if (maxWork - subjects[maxVal][1]) < 0:
            break
        d[maxVal] = subjects[maxVal]
        maxWork -= d[maxVal][1]
        mutable_subjects.remove(maxVal)

    return d


def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects



def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime(subjects):
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """

    for maxWork in range(1, 15, 1):
        startTime = time.time()
        subs = bruteForceAdvisor(subjects, maxWork)
        endTime = time.time()
        print 'Subjects selected = ', subs
        print("Total time for %.2f using brute force was %.2f" % (maxWork, endTime-startTime))
    

# Problem 3 Observations
# ======================
#
# It seemed to become unreasonable at max work = 9 (taking 10.98 seconds to compute)




#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    memo = {}
    nameList = subjects.keys()
    subjects = subjects.values()
    workList = []
    valueList = []
    for s in subjects:
        workList.append(s[WORK])
        valueList.append(s[VALUE])
        
    values, courses = \
            dpAdvisorHelper(workList, valueList, maxWork, len(subjects)-1, memo)

    selected_subjects = {}
    for course in courses:
        selected_subjects[nameList[course]] = (valueList[course], workList[course])

    return selected_subjects       




def dpAdvisorHelper(workList, valueList, workLeft, i, memo):


    try: return memo[(i, workLeft)]

    except KeyError:

        ## base case, edge of tree reached
        if i == 0:
            # item can be selected
            if workList[i] <= workLeft:
                memo[(i, workLeft)] = (valueList[i], [i])
                return valueList[i], [i]
            
            # item not selected
            else:
                memo[(i, workLeft)] = (0, [])
                return 0, []
        else:
            # calculate scenario with and without i
            value_without_i, course_list = dpAdvisorHelper(workList, valueList, workLeft, i-1, memo)
            
            if workList[i] > workLeft:
                memo[(i, workLeft)] = (value_without_i, course_list)
                return value_without_i, course_list
            
            else:
                value_with_i, course_list_with_i = \
                              dpAdvisorHelper(workList, valueList, workLeft - workList[i], i-1, memo)
                value_with_i += valueList[i]

            if value_with_i > value_without_i:
                maxVal = value_with_i
                course_list = [i] + course_list_with_i
                
            else:
                maxVal = value_without_i
                
            memo[(i, workLeft)] = (maxVal, course_list)
            return maxVal, course_list
            
    

#
# Problem 5: Performance Comparison
#
def dpTime(subjects):
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    for maxWork in range(1, 15, 1):
        startTime = time.time()
        subs = dpAdvisor(subjects, maxWork)
        endTime = time.time()
        print 'Subjects selected = ', subs
        print("Total time for %.2f using dynamic programming was %.2f" % (maxWork, endTime-startTime))



# Problem 5 Observations
# ======================
#
# My observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor:

##Total time for 1.00 using brute force was 0.00
##Total time for 2.00 using brute force was 0.00
##Total time for 3.00 using brute force was 0.01
##Total time for 4.00 using brute force was 0.05
##Total time for 5.00 using brute force was 0.17
##Total time for 6.00 using brute force was 0.48
##Total time for 7.00 using brute force was 1.43
##Total time for 8.00 using brute force was 4.30
##Total time for 9.00 using brute force was 11.10
##Total time for 10.00 using brute force was 29.21
##Total time for 11.00 using brute force was 75.28
##Total time for 12.00 using brute force was 182.14
##Total time for 13.00 using brute force was 433.07
##Total time for 14.00 using brute force was 1021.20
##Total time for 1.00 using dynamic programming was 0.01
##Total time for 2.00 using dynamic programming was 0.00
##Total time for 3.00 using dynamic programming was 0.00
##Total time for 4.00 using dynamic programming was 0.00
##Total time for 5.00 using dynamic programming was 0.00
##Total time for 6.00 using dynamic programming was 0.00
##Total time for 7.00 using dynamic programming was 0.00
##Total time for 8.00 using dynamic programming was 0.00
##Total time for 9.00 using dynamic programming was 0.01
##Total time for 10.00 using dynamic programming was 0.01
##Total time for 11.00 using dynamic programming was 0.01
##Total time for 12.00 using dynamic programming was 0.01
##Total time for 13.00 using dynamic programming was 0.01
##Total time for 14.00 using dynamic programming was 0.01


if __name__ == '__main__':
    subjects = loadSloadSubjectsubjects(SUBJECT_FILENAME)
    smallCatalog = {'6.00': (16, 8), '1.00': (7, 7), '6.01': (5, 3), '15.01': (9, 6)}
    bruteForceTime(subjects)
    dpTime(subjects)

    
    
