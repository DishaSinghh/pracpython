# marks={"name":"disha",
#        "age":19,
#        "plang":["pyth",00,99]}
# marks.update({"name":"azairah", "nam":"disha"})
# print(marks)

# dict={"madad":"help",
#       "mai":"me"}
# w=input("enter to translate")
# print(dict[w])
e = set()
while len(e) < 8:
    w = input("Enter a value: ")
    e.add(w)  # If it's a duplicate, set won't grow, so loop continues
print("Final set:", e)

