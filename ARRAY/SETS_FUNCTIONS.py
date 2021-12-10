set1 = set([1,2,4,5,6])
set2 = set([4,5,6,7,8])

# sets are sorted list

set1.pop()  # remove 1st element of set

set1.add(3) # add element in set at sorted manner

set1.intersection(set2)     # return element whcih are present in both sets
                            # or intersenction of sets

set3 = set1.copy()  # return copy of set


set1.difference(set2)   # return elements which are not present in
                        # another set

set1.remove(6)      # delete specific gien element in set

set1.add(6)

set1.union(set2)     # return elements which are unique
                    # in set1 and set2  & join eements which are
                     # both in set 1 and set2 or return union of sets

set1.discard(6)   #  saame as pop method


set1.update([6,39])     # add iterable to set and if element of iterable
                        # is present in set then it make it 1 by
                        # joining those values or same as union

set3 = set([3,4,5])

set3.issubset(set1)     # return true if all element of used set is in
                        # given set     ------ given set is bigger

set1.issuperset(set3)   # return true if all element of given set is in
                        # used set     ------ used set is bigger


set1.symmetric_difference(set2)     # return all element which are not
                                # same in both sets but in unsorted or
                                # first set 1 elements and then set2 elem

set3 = set([45,890])

set1.isdisjoint(set3)     # return true if elements of set1
                        # set 2 are completely diffrent not
                        # 1 element  is same in both sets

set1.clear()    # clear all element in  set

