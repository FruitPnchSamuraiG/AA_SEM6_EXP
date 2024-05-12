import random

candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
hcost = 10
icost = 1


def ascending(candidates, hcost, icost):
    hired_candidates = []

    # Hire the best candidate so far
    max=-1
    for i in range(len(candidates)):
        if candidates[i] > max:
            max=candidates[i]
            hired_candidates.append(candidates[i])

    hiring_cost = len(hired_candidates) * hcost
    interview_cost = len(candidates) * icost
    totalcost = interview_cost + hiring_cost

    print("Interviewed candidates:", candidates)
    print("Hired candidates:", hired_candidates)
    print("Number of candidates hired:", len(hired_candidates))
    print("Interview cost:", interview_cost)
    print("Hiring cost:", hiring_cost)
    print("Total Cost:", totalcost)


def rand(candidates, hcost, icost):
    interviewed_candidates = []
    hired_candidates = []

    # Randomly select and interview candidates
    for i in range(len(candidates)):
        selected_candidate = random.choice(candidates)
        interviewed_candidates.append(selected_candidate)
        candidates.remove(selected_candidate)

    # Hire the best candidate so far
    max=-1
    for i in range(len(interviewed_candidates)):
        if interviewed_candidates[i] > max:
            max=interviewed_candidates[i]
            hired_candidates.append(interviewed_candidates[i])

    hiring_cost = len(hired_candidates) * hcost
    interview_cost = len(interviewed_candidates) * icost
    totalcost = interview_cost + hiring_cost

    print("Interviewed candidates:", interviewed_candidates)
    print("Hired candidates:", hired_candidates)
    print("Number of candidates hired:", len(hired_candidates))
    print("Interview cost:", interview_cost)
    print("Hiring cost:", hiring_cost)
    print("Total Cost:", totalcost)

print("In ascending order:")
ascending(candidates, hcost, icost)

print("\nIn random order:")
rand(candidates, hcost, icost)

