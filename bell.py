import cirq

q0 = cirq.GridQubit(0, 0)
q1 = cirq.GridQubit(1, 0)
qubits = [q0, q1]

circuit = cirq.Circuit()

circuit.append(cirq.H(q0))
circuit.append(cirq.CNOT.on(q0, q1))
circuit.append(cirq.measure(*qubits, key='x'))
print("Here's the circuit that constructs the Bell pair and measures it:")
print(circuit)

simulator = cirq.Simulator()

results = simulator.run(circuit, repetitions=100)
print("\nThe result of measuring 100 times:")
print(results.histogram(key='x'))

print("\nIf we wanted to measure q0 first, and then q1, the circuit will look like the following:")


circuit = cirq.Circuit()

circuit.append(cirq.H(q0))
circuit.append(cirq.CNOT.on(q0, q1))
circuit.append(cirq.measure(q0, key='x'))
# below line inserts measurement gate at the next moment
circuit.append(cirq.measure(q1, key='y'), strategy=cirq.InsertStrategy.NEW_THEN_INLINE)

print(circuit)

simulator = cirq.Simulator()

results = simulator.run(circuit, repetitions=100)
print("\nThe result of measuring 100 times:")
print(f"Measuring first qubit: {results.histogram(key='x')}")
print(f"Measuring second qubit: {results.histogram(key='y')}")
print("Observe how the results of second qubit must match first qubit because they're entangled")
