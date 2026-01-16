with open('testfile.txt', 'a') as f:
    f.write("nicasdasde!")

with open('testfile.txt') as f:
    print(f.read())