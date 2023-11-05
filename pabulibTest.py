from pabutools.election import Project, Instance, ApprovalBallot, Cost_Sat, ApprovalProfile
from pabutools.rules import greedy_utilitarian_welfare, sequential_phragmen, method_of_equal_shares
# Creating a project object and giving it a cost
p1 = Project("p1", 1000)
p2 = Project("p2", 2000)
p3 = Project("p3", 3000)

# Create an instance of a pb election
instance = Instance()
instance.add(p1)
instance.update([p2,p3])
instance.budget_limit = 3000

# Create a ballot
b1 = ApprovalBallot([p1,p2])
b1.add(p2)
b2 = ApprovalBallot({p1,p2,p3})
b3 = ApprovalBallot({p3})

# Create an approval profile
profile = ApprovalProfile([b1, b2])   # Initialize the profile with two ballots
profile.append(b3)   # Use list methods to handle the profile

#
outcome1 = sequential_phragmen(instance, profile)
outcome2 = method_of_equal_shares(instance, profile, sat_class=Cost_Sat)
print(outcome2)