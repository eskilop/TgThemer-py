def read_file(inputfile):
    source = open(inputfile+'.attheme', 'r')
    contents = source.read()
    source.close()
    return contents


def to_file(contents, outfile):
    result = open(outfile+'.attheme', 'w')
    result.write(contents)
    result.close()
