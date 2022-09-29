def make_sandwiches(*items):
    """A function that accepts several items a person wants on a sandwich"""
    print('Items Ordered:')
    for item in items:
        print(f'\t- {item}')


make_sandwiches('mozzarella', 'bacon', 'tomatoes')
make_sandwiches('turkey', 'lettuce')
make_sandwiches('roast beef', 'cheese', 'bacon', 'ketchup', 'onions')
