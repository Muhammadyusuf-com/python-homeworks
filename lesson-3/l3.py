# =======================
# List Tasks
# =======================

def count_occurrences(lst, element):
    return lst.count(element)

def sum_of_elements(lst):
    return sum(lst)

def max_element(lst):
    return max(lst) if lst else None

def min_element(lst):
    return min(lst) if lst else None

def check_element(lst, element):
    return element in lst

def first_element(lst):
    return lst[0] if lst else None

def last_element(lst):
    return lst[-1] if lst else None

def slice_list(lst):
    return lst[:3]

def reverse_list(lst):
    return lst[::-1]

def sort_list(lst):
    return sorted(lst)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def insert_element(lst, element, index):
    lst.insert(index, element)
    return lst

def index_of_element(lst, element):
    return lst.index(element) if element in lst else -1

def check_empty_list(lst):
    return len(lst) == 0

def count_even_numbers(lst):
    return sum(1 for x in lst if x % 2 == 0)

def count_odd_numbers(lst):
    return sum(1 for x in lst if x % 2 != 0)

def concatenate_lists(lst1, lst2):
    return lst1 + lst2

def find_sublist(lst, sublist):
    for i in range(len(lst) - len(sublist) + 1):
        if lst[i:i+len(sublist)] == sublist:
            return True
    return False

def replace_element(lst, old, new):
    if old in lst:
        lst[lst.index(old)] = new
    return lst

def find_second_largest(lst):
    unique = sorted(set(lst), reverse=True)
    return unique[1] if len(unique) >= 2 else None

def find_second_smallest(lst):
    unique = sorted(set(lst))
    return unique[1] if len(unique) >= 2 else None

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def list_length(lst):
    return len(lst)

def create_copy(lst):
    return lst.copy()

def get_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None
    mid = n // 2
    return lst[mid] if n % 2 == 1 else lst[mid-1:mid+1]

def find_max_of_sublist(lst, start, end):
    return max(lst[start:end]) if lst[start:end] else None

def find_min_of_sublist(lst, start, end):
    return min(lst[start:end]) if lst[start:end] else None

def remove_element_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    return lst

def check_if_sorted(lst):
    return lst == sorted(lst)

def repeat_elements(lst, times):
    return [x for x in lst for _ in range(times)]

def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)

def find_all_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

def rotate_list(lst):
    return [lst[-1]] + lst[:-1] if lst else []

def create_range_list(start, end):
    return list(range(start, end + 1))

def sum_positive_numbers(lst):
    return sum(x for x in lst if x > 0)

def sum_negative_numbers(lst):
    return sum(x for x in lst if x < 0)

def check_palindrome(lst):
    return lst == lst[::-1]

def create_nested_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def get_unique_elements_in_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# =======================
# Tuple Tasks
# =======================

def tuple_count_occurrences(tpl, element):
    return tpl.count(element)

def tuple_max_element(tpl):
    return max(tpl) if tpl else None

def tuple_min_element(tpl):
    return min(tpl) if tpl else None

def tuple_check_element(tpl, element):
    return element in tpl

def tuple_first_element(tpl):
    return tpl[0] if tpl else None

def tuple_last_element(tpl):
    return tpl[-1] if tpl else None

def tuple_length(tpl):
    return len(tpl)

def slice_tuple(tpl):
    return tpl[:3]

def concatenate_tuples(t1, t2):
    return t1 + t2

def check_tuple_empty(tpl):
    return len(tpl) == 0

def get_all_indices_tuple(tpl, element):
    return [i for i, x in enumerate(tpl) if x == element]

def tuple_second_largest(tpl):
    unique = sorted(set(tpl), reverse=True)
    return unique[1] if len(unique) >= 2 else None

def tuple_second_smallest(tpl):
    unique = sorted(set(tpl))
    return unique[1] if len(unique) >= 2 else None

def create_single_element_tuple(element):
    return (element,)

def convert_list_to_tuple(lst):
    return tuple(lst)

def check_tuple_sorted(tpl):
    return tpl == tuple(sorted(tpl))

def find_max_of_subtuple(tpl, start, end):
    return max(tpl[start:end]) if tpl[start:end] else None

def find_min_of_subtuple(tpl, start, end):
    return min(tpl[start:end]) if tpl[start:end] else None

def remove_element_by_value_tuple(tpl, element):
    lst = list(tpl)
    if element in lst:
        lst.remove(element)
    return tuple(lst)

def create_nested_tuple(tpl, size):
    return tuple(tuple(tpl[i:i+size]) for i in range(0, len(tpl), size))

def repeat_elements_tuple(tpl, times):
    return tuple(x for x in tpl for _ in range(times))

def create_range_tuple(start, end):
    return tuple(range(start, end + 1))

def reverse_tuple(tpl):
    return tpl[::-1]

def check_tuple_palindrome(tpl):
    return tpl == tpl[::-1]

def get_unique_elements_tuple(tpl):
    seen = set()
    return tuple(x for x in tpl if not (x in seen or seen.add(x)))

# =======================
# Set Tasks
# =======================

def union_of_sets(s1, s2):
    return s1.union(s2)

def intersection_of_sets(s1, s2):
    return s1.intersection(s2)

def difference_of_sets(s1, s2):
    return s1.difference(s2)

def check_subset(s1, s2):
    return s1.issubset(s2)

def check_set_element(s, element):
    return element in s

def set_length(s):
    return len(s)

def convert_list_to_set(lst):
    return set(lst)

def remove_element_set(s, element):
    s.discard(element)
    return s

def clear_set(s):
    return set()

def check_set_empty(s):
    return len(s) == 0

def symmetric_difference(s1, s2):
    return s1.symmetric_difference(s2)

def add_element_to_set(s, element):
    s.add(element)
    return s

def pop_element_from_set(s):
    return s.pop() if s else None

def find_max_in_set(s):
    return max(s) if s else None

def find_min_in_set(s):
    return min(s) if s else None

def filter_even_set(s):
    return {x for x in s if x % 2 == 0}

def filter_odd_set(s):
    return {x for x in s if x % 2 != 0}

def create_range_set(start, end):
    return set(range(start, end + 1))

def merge_and_deduplicate(lst1, lst2):
    return set(lst1 + lst2)

def check_disjoint_sets(s1, s2):
    return s1.isdisjoint(s2)

def remove_duplicates_from_list(lst):
    return list(set(lst))

def count_unique_elements(lst):
    return len(set(lst))

# =======================
# Dictionary Tasks
# =======================

def get_value(d, key):
    return d.get(key)

def check_key(d, key):
    return key in d

def count_keys(d):
    return len(d)

def get_all_keys(d):
    return list(d.keys())

def get_all_values(d):
    return list(d.values())

def merge_dictionaries(d1, d2):
    return {**d1, **d2}

def remove_key(d, key):
    d.pop(key, None)
    return d

def clear_dictionary():
    return {}

def check_dict_empty(d):
    return len(d) == 0

def get_key_value_pair(d, key):
    return (key, d[key]) if key in d else None

def update_value(d, key, value):
    d[key] = value
    return d

def count_value_occurrences(d, value):
    return list(d.values()).count(value)

def invert_dictionary(d):
    return {v: k for k, v in d.items()}

def find_keys_with_value(d, value):
    return [k for k, v in d.items() if v == value]

def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

def check_nested_dict(d):
    return any(isinstance(v, dict) for v in d.values())

def get_nested_value(d, outer_key, inner_key):
    return d.get(outer_key, {}).get(inner_key)

def create_default_dict(default_value):
    from collections import defaultdict
    return defaultdict(lambda: default_value)

def count_unique_values(d):
    return len(set(d.values()))

def sort_dict_by_key(d):
    return dict(sorted(d.items()))

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

def filter_dict_by_value(d, condition):
    return {k: v for k, v in d.items() if condition(v)}

def check_common_keys(d1, d2):
    return bool(set(d1.keys()) & set(d2.keys()))

def create_dict_from_tuple(tuples):
    return dict(tuples)

def get_first_key_value(d):
    return next(iter(d.items())) if d else None
