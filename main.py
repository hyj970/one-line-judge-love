"""One line to make the judge fall in love.

The entry is a single line of at most 240 characters, written to
/output/entry.txt. It is about a person, caught in one specific
particular only someone who loves her would notice: she folds the
corner of every page she loves. The turn comes at the end, when the
bent corners stop being a habit and become a trail of small flags
marking the way back to her.
"""

LINE = "She still folds the corner of every page she loves, and twenty years later I keep finding them, one bent corner at a time, like she left a trail of small flags marking the way back to her."


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
