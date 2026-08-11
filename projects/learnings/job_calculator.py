current_ctc = 23
expected_ctc = 35

hike = expected_ctc - current_ctc
hike_percentage = hike/current_ctc * 100

print(f"{current_ctc}lpa")
print(f"{expected_ctc}lpa")
print(f"{hike}lpa")
print(f"{hike_percentage:.2f}%")

if hike_percentage >= 50:
    print("Fantastic Job! You are a Hard Worker")
elif hike_percentage >= 30:
    print("Congrats! Can still do better.")
else:
    print("Unbelievable Achievement")

count = 1
while current_ctc < expected_ctc:
    current_ctc += (5/100 * current_ctc)
    print(f"Switched {count} times {current_ctc:.2f}")

    count += 1
