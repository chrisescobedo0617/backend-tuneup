#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "chrisescobedo0617"

import cProfile
import pstats
import functools


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr)
        ps.strip_dirs().sort_stats('cumulative').print_stats()
        return result
    return wrapper


#def read_movies(src):
   # """Returns a list of movie titles."""
    #print(f'Reading file: {src}')
    #with open(src, 'r') as f:
        #return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        movies = f.read().splitlines()
    duplicates = {}
    dups = []
    for movie in movies:
        if duplicates.get(movie) == None:
            duplicates[movie] = 1
        else:
            duplicates[movie] += 1
    for key, value in duplicates.items():
        if 2 == value:
            dups.append(key)
    #while movies:
        #movie = movies.pop()
        #if is_duplicate(movie, movies):
            #duplicates.append(movie)
    return dups


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    from timeit import Timer
    runs_per_repeat = 5
    num_repeats = 7
    t = Timer(lambda: main())
    result = t.repeat(repeat=num_repeats,number=runs_per_repeat)
    best_time = min(result) / float(runs_per_repeat)
    print(f"Best time across 7 repeats of 5 runs per repeat: {best_time} sec")


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))
    


if __name__ == '__main__':
    main()