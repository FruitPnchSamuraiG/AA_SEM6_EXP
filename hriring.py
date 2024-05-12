import random

candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hcost = 10
icost = 1
candidates_random = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(candidates_random)

def deter(candidates, hcost, icost):
    hired_candidates = []
    fired_candidates = []

    max=-1
    hiring_cost=0
    interview_cost=0
    totalcost=0
    for i in range(len(candidates)):
        if candidates[i] > max:
            max=candidates[i]
            if i!=0:
                fired_candidates.append(hired_candidates[0])
                hired_candidates.pop()
            hired_candidates.append(candidates[i])

            hiring_cost += hcost
            interview_cost += icost
            totalcost = interview_cost + hiring_cost

            print("Candidate selected: ", candidates[i])
            print("Hired candidates:", hired_candidates)
            print("Fired candidates:", fired_candidates)
            print("Total Cost:", totalcost)
           
        else:
            interview_cost+=icost
            totalcost = interview_cost + hiring_cost
            print("Didnt hire: ", candidates[i])
            print("Hired candidates: ", hired_candidates)
            print("Fired candidates:", fired_candidates)
            print("Total Cost:", totalcost)
           
        print("")

def rand(candidates, hcost, icost):
    interviewed_candidates = []
    hired_candidates = []
    fired_candidates = []
   
    hiring_cost=0
    interview_cost=0

    for i in range(len(candidates)):
        selected_candidate = random.choice(candidates)
        interviewed_candidates.append(selected_candidate)
        candidates.remove(selected_candidate)

    max=-1
    for i in range(len(interviewed_candidates)):
       
        if interviewed_candidates[i] > max:
            max=interviewed_candidates[i]
            if i!=0:
                fired_candidates.append(hired_candidates[0])
                hired_candidates.pop()
            hired_candidates.append(interviewed_candidates[i])

            hiring_cost += hcost
            interview_cost += icost
            totalcost = interview_cost + hiring_cost

    #print("Interviewed candidates:", interviewed_candidates)
            print("")
            print("Selected Candidate: ",interviewed_candidates[i])
            print("Hired candidates:", hired_candidates)
            print("Fired candidates:", fired_candidates)
            print("Total Cost:", totalcost)
           
        else:
            print("")
            print("Didnt select:",interviewed_candidates[i])
            print("Hired candidates:",hired_candidates)
            print("Fired candidates:", fired_candidates)
            print("Total Cost:", totalcost)
           

print("In deterministic approach:")
deter(candidates, hcost, icost)

print(candidates_random)
print("\nIn randomised approach:")
deter(candidates_random, hcost, icost)
###################################################################################################################
