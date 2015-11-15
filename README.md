# StableMarriage
Stable Marriage Creation

The problem of stable marriages are seeking a stable matching between men and women, having given the preferences every man and woman.
This project uses the [Gale-Shapley algorithm](https://en.wikipedia.org/wiki/Stable_marriage_problem).

These preferences are given via JSON format files. These files have the form:

{
  "men_rankings": {
    "abe": ["cat", "bea", "ada"],
    "bob": ["ada", "cat", "bea"],
    "cal": ["ada", "bea", "cat"]
  },

  "women_rankings": {
    "ada": ["abe", "cal", "bob"],
    "bea": ["bob", "abe", "cal"],
    "cat": ["cal", "abe", "bob"]
  }
}
