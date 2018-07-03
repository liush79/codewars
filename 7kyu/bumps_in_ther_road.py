from common import Test as test


def bumps(road):
    return 'Car Dead' if len([r for r in road if r is 'n']) > 15 else 'Woohoo!'


def best_practice_bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"


test.describe("Example tests")
test.assert_equals(bumps("n"), "Woohoo!")
test.assert_equals(bumps("_nnnnnnn_n__n______nn__nn_nnn"), "Car Dead")
test.assert_equals(bumps("______n___n_"), "Woohoo!")


'''
Your car is old, it breaks easily.
The shock absorbers are gone and you think it can handle about 15 more bumps before it dies totally.

Unfortunately for you, your drive is very bumpy! Given a string showing either flat road ("_") or bumps ("n"), 
work out if you make it home safely. 15 bumps or under, return "Woohoo!", over 15 bumps return "Car Dead".
'''