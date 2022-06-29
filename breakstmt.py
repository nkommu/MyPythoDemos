while True:
    msg=input("> ").lower()
    
    if msg[0]=="#":
        continue
    
    print(msg)
    if msg=="quit":
        print("break the flow")
        break
    print("done")
print("extra line")