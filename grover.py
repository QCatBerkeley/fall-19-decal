import cirq

# Make circuit and qubits.
c = cirq.Circuit()

input_qubits = [cirq.LineQubit(i) for i in range(2)]
output_qubit = cirq.LineQubit(2)

# Initialize.
c.append([
    cirq.X(output_qubit),
    cirq.H(output_qubit), # |-> for P.K.
    cirq.H.on_each(*input_qubits)
    ])

# Append oracle (rotation about |a perp>)
c.append([
    cirq.X(input_qubits[1]),
    cirq.TOFFOLI(input_qubits[0], input_qubits[1], output_qubit),
    cirq.X(input_qubits[1])
    ])

# check:
print(c)

# Switch to Hadamard basis
c.append(cirq.H.on_each(*input_qubits))


#  Append diffusion oracle (rotation about |0> in Hadamard basis)
c.append([
    cirq.X.on_each(*input_qubits),
    cirq.H(input_qubits[1]),
    cirq.CNOT(*input_qubits),
    cirq.H(input_qubits[1]),
    cirq.X.on_each(*input_qubits)
    ])

# Switch to computational basis
c.append(cirq.H.on_each(*input_qubits))


# Measure
c.append(cirq.measure(*input_qubits, key='x'))

# check:
print(c)

# Simulate 1000 times:
s = cirq.Simulator()
results = s.run(c, repetitions=1000)
print(results.histogram(key='x'))
