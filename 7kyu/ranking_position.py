from common import Test


def ranking(people):
    rank = last_points = 0

    people.sort(key=lambda p: (-p['points'], p['name']))

    for i, person in enumerate(people):
        if last_points != person['points']:
            rank = i + 1
            last_points = person['points']
        person['position'] = rank

    return people


input_ = [
      {
        "name": "John",
        "points": 100,
      },
      {
        "name": "Bob",
        "points": 130,
      },
      {
        "name": "Mary",
        "points": 120,
      },
      {
        "name": "Kate",
        "points": 120,
      },
]

output = [
      {
        "name": "Bob",
        "points": 130,
        "position": 1,
      },
      {
        "name": "Kate",
        "points": 120,
        "position": 2,
      },
      {
        "name": "Mary",
        "points": 120,
        "position": 2,
      },
      {
        "name": "John",
        "points": 100,
        "position": 4,
      }
]

Test.assert_equals(ranking(input_), output)

input_ = [
      {
        "name": "Bob",
        "points": 130,
      },
      {
        "name": "Mary",
        "points": 120,
      },
      {
        "name": "John",
        "points": 100,
      },
]

output = [
      {
        "name": "Bob",
        "points": 130,
        "position": 1,
      },
      {
        "name": "Mary",
        "points": 120,
        "position": 2,
      },
      {
        "name": "John",
        "points": 100,
        "position": 3,
      },
]

Test.assert_equals(ranking(input_), output)

input_ = [
      {
        "name": "Bob",
        "points": 100,
      },
      {
        "name": "Mary",
        "points": 100,
      },
      {
        "name": "John",
        "points": 100,
      },
]

output = [
      {
        "name": "Bob",
        "points": 100,
        "position": 1,
      },
      {
        "name": "John",
        "points": 100,
        "position": 1,
      },
      {
        "name": "Mary",
        "points": 100,
        "position": 1,
      },
]

Test.assert_equals(ranking(input_), output)

input_ = [{"name": "Joe", "points": 100}]

output = [{"name": "Joe", "points": 100, "position": 1}]

Test.assert_equals(ranking(input_), output)

Test.assert_equals(ranking([]), [])

'''
In some ranking people collects points. The challenge is sort by points and calculate position for every person.
But remember if two or more persons have same number of points,
they should have same position number and sorted by name (name is unique).
'''