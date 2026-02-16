def get_semifinal_matchups(teams):
    teams_points = {}
    for team in teams:
        name, points = team.split(":")
        points = [int(p) * (3 - i) for i, p in enumerate(points.split("-"))]
        teams_points[sum(points)] = name
    teams = sorted(teams_points.items(), key=lambda x: x[0], reverse=True)

    return "The semi-final games will be {} vs {} and {} vs {}.".format(
        teams[0][1], teams[3][1], teams[1][1], teams[2][1]
    )


if __name__ == "__main__":
    # Function call 1
    print(
        get_semifinal_matchups(
            [
                "CAN: 2-2-0-1",
                "FIN: 2-2-1-0",
                "GER: 1-0-1-3",
                "SUI: 0-1-3-1",
                "SWE: 1-1-2-1",
                "USA: 2-1-0-2",
            ]
        )
    )

    # Function call 2
    print(
        get_semifinal_matchups(
            [
                "CAN: 2-1-1-1",
                "CZE: 1-1-1-2",
                "FIN: 1-2-1-1",
                "NOR: 0-1-1-3",
                "SLO: 1-0-1-3",
                "USA: 5-0-0-0",
            ]
        )
    )

    # Function call 3
    print(
        get_semifinal_matchups(
            [
                "CAN: 3-2-0-0",
                "CZE: 2-1-2-0",
                "LAT: 0-0-1-4",
                "ITA: 1-1-1-2",
                "DEN: 1-0-0-4",
                "USA: 3-1-1-0",
            ]
        )
    )

    # Function call 4
    print(
        get_semifinal_matchups(
            [
                "AUT: 2-2-1-0",
                "DEN: 1-0-0-4",
                "ITA: 1-1-1-2",
                "JPN: 3-2-0-0",
                "KOR: 2-1-2-0",
                "LAT: 0-0-1-4",
            ]
        )
    )
