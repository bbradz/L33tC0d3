"""
    A cute file as I ease back in (6-19-23) from 4 days now of having been
    bedbound sick with headaches and a cold... inspired by Mathemaniac's YT
    video on the James-Stein estimator as a simple estimator of the means of
    multiple random samples taken from 3 or more possibly correlated Gaussian
    distributions. 

    The scalar will usually lie between 0 & 1 which causes the many points
    farther from the origin than the actual means to be brought closer towards
    the origin and their true mean which results in new estimates for the means
    which are provably dominant to naively using the samples found as the means
    for 3 or higher samples

    This only works for 3 or higher samples because the space between the mean
    and the origin makes up less and less of the space of samples as the
    dimensions of that sample space increases
"""

def main(*args):
    if len(args) >= 3:
        scalar = 1 - (1/sum([arg ^ 2 for arg in args]))
        result = [data_point * scalar for data_point in args]
        return result
    else: 
        return args

"""
    if __name__ idiom to indicate the file is a script + to ensure against
    errors & for easier access by other functions
"""
if __name__ == '__main__':
    main()

