## Events organization
Events: E1, E2, E3, E4, E5
People: P1, P2, P3, P4

### Preferences:
- P1 want to go to E1, E4
- P2 want to go to E2, E3
- P3 want to go to E4, E5
- P4 want to go to E3, E4

### Binary variables:
- x_i = 0 is the i-th event is on Saturday
- x_i = 1 is the i-th event is on Sunday

### Formulation:
f(x1,x2,x3,x4,x5) = 4 + x_1 + x_2 + 2x_3 + 3x_4 + x_5 - 2x_1x_4 - 2x_2x_3 - 2x_4x_5 - 2x_3x_4

### Change of variable
x_i = 1/2(1 - z_i)

- z_i = 1 is the i-th event is on Saturday
- z_i = -1 is the i-th event is on Sunday

### New formulation:
f(z1,z2,z3,z4,z5) = 6 - 1/2z_1z_4 - 1/2z_2z_3 - 1/2z_4z_5 - 1/2z_3z_4