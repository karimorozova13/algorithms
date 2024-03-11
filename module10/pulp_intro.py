import pulp

model_max = pulp.LpProblem("Max_Model", pulp.LpMaximize)
model_min = pulp.LpProblem("Min_Model", pulp.LpMinimize)

print(model_max)
print(model_min)

x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
y = pulp.LpVariable('y', 3, 7)


# 2x + 3y
model_max += 2*x + 3*y, "Problem"

# constraints Обмеження 
# x + 2y <= 8; y >= 2

model_max += x + 2*y <= 8, 'Constraint1'
model_max += 2*y >= 0, "Constraint2"
# print(model_max)

model_max.solve()
print(pulp.LpStatus[model_max.status])
print(pulp.LpStatus[model_min.status])

for var in model_max.variables():
    print(f'{var.name} = {var.varValue}')
    
print(f'Total cost: {pulp.value(model_max.objective)}')
