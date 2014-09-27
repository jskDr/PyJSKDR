for x in range(2, 10):
    print "{0} Level".format( x)
    for y in range( 2, 10):
        z = x*y
        print "{0} x {1} = {2}".format( x, y, z)
    print