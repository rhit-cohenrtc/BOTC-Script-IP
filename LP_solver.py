#
# Model made by Tristan Cohen Rider
# 

from __future__ import division
from pyomo.environ import *
from pyomo.opt import SolverFactory

# Instantiate and name the model
M = AbstractModel()
M.name = "Worst Game of Blood on the Clocktower"

# Sets
M.NumCharacters = Param(within=NonNegativeIntegers)
M.Characters = RangeSet(1,M.NumCharacters)
M.A = Set(within=M.Characters)
M.B = Set(within=M.Characters)
M.C = Set(within=M.Characters)
M.D = Set(within=M.Characters)

# Parameters
M.ValidJinx = Param(M.Characters, M.Characters, within=Binary)
M.MinA = Param(within=NonNegativeIntegers)
M.MinB = Param(within=NonNegativeIntegers)
M.MinC = Param(within=NonNegativeIntegers)
M.MinD = Param(within=NonNegativeIntegers)
M.MaxA = Param(within=NonNegativeIntegers)
M.MaxB = Param(within=NonNegativeIntegers)
M.MaxC = Param(within=NonNegativeIntegers)
M.MaxD = Param(within=NonNegativeIntegers)
M.MinTotal = Param(within=NonNegativeIntegers)
M.MaxTotal = Param(within=NonNegativeIntegers)

# Variables
M.Character = Var(M.Characters, within=Binary)
M.Jinx = Var(M.Characters, M.Characters, within=Binary)

# Objective
def MaxJinxes(M):
    return 0.5 * sum(M.ValidJinx[i,j] * M.Jinx[i,j] for i in M.Characters for j in M.Characters)
M.MaxJinxes = Objective(rule=MaxJinxes, sense=maximize)

# Constaints
def EnsureSubgraphEdges(M,i,j):
    return 2 * M.Jinx[i,j] <= M.Character[i] + M.Character[j]
M.EnsureSubgraphEdges = Constraint(M.Characters, M.Characters, rule=EnsureSubgraphEdges)

def EnsureAPicksMin(M):
    return M.MinA <= sum(M.Character[i] for i in M.A)
M.EnsureAPicksMin = Constraint(rule=EnsureAPicksMin)

def EnsureAPicksMax(M):
    return sum(M.Character[i] for i in M.A) <= M.MaxA
M.EnsureAPicksMax = Constraint(rule=EnsureAPicksMax)

def EnsureBPicksMin(M):
    return M.MinB <= sum(M.Character[i] for i in M.B)
M.EnsureBPicksMin = Constraint(rule=EnsureBPicksMin)

def EnsureBPicksMax(M):
    return sum(M.Character[i] for i in M.B) <= M.MaxB
M.EnsureBPicksMax = Constraint(rule=EnsureBPicksMax)

def EnsureCPicksMin(M):
    return M.MinC <= sum(M.Character[i] for i in M.C)
M.EnsureCPicksMin = Constraint(rule=EnsureCPicksMin)

def EnsureCPicksMax(M):
    return sum(M.Character[i] for i in M.C) <= M.MaxC
M.EnsureCPicksMax = Constraint(rule=EnsureCPicksMax)

def EnsureDPicksMin(M):
    return M.MinD <= sum(M.Character[i] for i in M.D)
M.EnsureDPicksMin = Constraint(rule=EnsureDPicksMin)

def EnsureDPicksMax(M):
    return sum(M.Character[i] for i in M.D) <= M.MaxD
M.EnsureDPicksMax = Constraint(rule=EnsureDPicksMax)

def EnsureTotalPicksMin(M):
    return M.MinTotal <= sum(M.Character[i] for i in M.Characters)
M.EnsureTotalPicksMin = Constraint(rule=EnsureTotalPicksMin)

def EnsureTotalPicksMax(M):
    return sum(M.Character[i] for i in M.Characters) <= M.MaxTotal
M.EnsureTotalPicksMax = Constraint(rule=EnsureTotalPicksMax)

# def EnsureBoffin(M):
#     return M.Character[61] + M.Character[22] == 2
# M.EnsureBoffin = Constraint(rule=EnsureBoffin)

# Create a problem instance
instance = M.create_instance("data_file.dat")

# Indicate which solver to use
Opt = SolverFactory("gurobi")
#Opt = SolverFactory("appsi_highs")

# Generate a solution
Soln = Opt.solve(instance)
instance.solutions.load_from(Soln)

# Print the output
print(f"Termination Condition was {Soln.Solver.Termination_condition}")
display(instance)