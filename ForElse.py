fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        #break
    print 'A', f
else:#this won't execute if a break is hit otherwise it will after the for
    print 'A fine selection of fruits!'
