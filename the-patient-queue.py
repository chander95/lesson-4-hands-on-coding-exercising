patient_queue = ["Ronald", "Victoria", "Phionna", "Alex", "Ursula", "Darien", "Dany", "Jayden"]

for name in patient_queue:
    while patient_queue.index(name) < len(patient_queue):
        print("Next up, " + name + ".")
        break
print("There are no more patients in the queue!")
