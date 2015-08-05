import sys
from collections import defaultdict

def get_md5sum( infile ):
    """Receives a tab-separated file of md5sums and filenames,
       stores them in a dictionary"""
    filemap = dict()

    with open(infile) as f:

        for line in f:
            try:
                md5sum,filename = line.strip().split()
            except:
                continue

            filename = filename.split("/")[-1]
            filemap[ filename ] = md5sum

    return filemap


def get_md5sum_pairs( file1, file2 ):
    """Receives two files with md5sums and returns a dictionary
       of { filename : ( md5sum1, md5sum2 ) } """

    filemap = defaultdict( lambda:[None,None] )

    for filename,md5sum in get_md5sum(file1).iteritems():
        filemap[filename][0] = md5sum
    for filename,md5sum in get_md5sum(file2).iteritems():
        filemap[filename][1] = md5sum

    return filemap




if __name__=="__main__":

    try:
        file1,file2 = sys.argv[1:]
    except:
        sys.exit("\nUsage:\n\tcheck_sum.py <md5sum_file1> <md5sum_file2> \n")

    sum_pairs = get_md5sum_pairs( file1,file2 )

    print "------------------"
    print "Mismatched md5sums"
    print "------------------"
    for filename,(sum1,sum2) in sum_pairs.iteritems():
        if sum1 and sum2:
            if sum1 != sum2:
                print filename
    print
    print "-------------"
    print "Missing files"
    print "-------------"
    for filename,(sum1,sum2) in sum_pairs.iteritems():
        if not sum1:
            print filename, "missing in", file1
        if not sum2:
            print filename, "missing in", file2
    print
