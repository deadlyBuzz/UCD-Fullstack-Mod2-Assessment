from datetime import datetime, timedelta
# from app import Score


# debug function for testing.
# Add a bunch of match results so that we can see the table and the matches
# being displayed.
# TODO: Remove before Launch
def dbgPopulateMatches(matches, Score):
    # ==========================================
    #                 ROUND 1                 
    # ==========================================

    # Match 1 (ID 1): Benetton vs Dragons
    matches[0].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[0].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[0].updateScore(Score("PT", 7, datetime.now(), "away")) # Integrated Penalty Try
    matches[0].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[0].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[0].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[0].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[0].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[0].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[0].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[0].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[0].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[0].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[0].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[0].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[0].updateScore(Score("C", 2, datetime.now(), "home"))

    # Match 2 (ID 2): Connacht vs Stormers
    matches[1].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[1].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[1].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[1].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[1].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[1].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[1].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[1].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[1].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[1].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[1].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[1].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[1].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[1].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[1].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[1].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[1].updateScore(Score("P", 3, datetime.now(), "home"))

    # Match 3 (ID 3): Ulster vs Edinburgh
    matches[2].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[2].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[2].updateScore(Score("PT", 7, datetime.now(), "away")) # Integrated Penalty Try
    matches[2].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[2].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[2].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[2].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[2].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[2].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[2].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[2].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[2].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[2].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[2].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[2].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[2].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[2].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[2].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[2].updateScore(Score("C", 2, datetime.now(), "home"))

    # Match 4 (ID 4): Lions vs Leinster
    matches[3].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[3].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[3].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[3].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[3].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[3].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[3].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[3].updateScore(Score("PT", 7, datetime.now(), "away")) # Integrated Penalty Try
    matches[3].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[3].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[3].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[3].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[3].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[3].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[3].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[3].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[3].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[3].updateScore(Score("C", 2, datetime.now(), "away"))

    # Match 5 (ID 5): Sharks vs Ospreys
    matches[4].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[4].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[4].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[4].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[4].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[4].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[4].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[4].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[4].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[4].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[4].updateScore(Score("T", 5, datetime.now(), "home"))

    # Match 6 (ID 6): Zebre Parma vs Bulls
    matches[5].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[5].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[5].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[5].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[5].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[5].updateScore(Score("PT", 7, datetime.now(), "away")) # Integrated Penalty Try
    matches[5].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[5].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[5].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[5].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[5].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[5].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[5].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[5].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[5].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[5].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[5].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[5].updateScore(Score("C", 2, datetime.now(), "away"))

    # Match 7 (ID 7): Munster vs Glasgow Warriors
    matches[6].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[6].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[6].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[6].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[6].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[6].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[6].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[6].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[6].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[6].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[6].updateScore(Score("C", 2, datetime.now(), "away"))

    # Match 8 (ID 8): Scarlets vs Cardiff
    matches[7].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[7].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[7].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[7].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[7].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[7].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[7].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[7].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[7].updateScore(Score("C", 2, datetime.now(), "home"))

    # ==========================================
    #                 ROUND 2                 
    # ==========================================

    # Match 9 (ID 9): Benetton vs Connacht
    matches[8].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[8].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[8].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[8].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[8].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[8].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[8].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[8].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[8].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[8].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[8].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[8].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[8].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[8].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[8].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[8].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[8].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[8].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[8].updateScore(Score("P", 3, datetime.now(), "home"))

    # Match 10 (ID 10): Cardiff vs Zebre Parma
    matches[9].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[9].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[9].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[9].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[9].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[9].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[9].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[9].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[9].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[9].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[9].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[9].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[9].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[9].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[9].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[9].updateScore(Score("P", 3, datetime.now(), "home"))

    # Match 11 (ID 11): Edinburgh vs Stormers
    matches[10].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[10].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[10].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[10].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[10].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[10].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[10].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[10].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[10].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[10].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[10].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[10].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[10].updateScore(Score("P", 3, datetime.now(), "home"))

# Match 12 (ID 12): Lions vs Ospreys
    matches[11].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[11].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[11].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[11].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[11].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[11].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[11].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[11].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[11].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[11].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[11].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[11].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[11].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[11].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[11].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[11].updateScore(Score("C", 2, datetime.now(), "away"))

# Match 13 (ID 13): Dragons vs Scarlets
    matches[12].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[12].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[12].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[12].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[12].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[12].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[12].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[12].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[12].updateScore(Score("C", 2, datetime.now(), "home"))

# Match 14 (ID 14): Sharks vs Leinster
    matches[13].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[13].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[13].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[13].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[13].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[13].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[13].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[13].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[13].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[13].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[13].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[13].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[13].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[13].updateScore(Score("P", 3, datetime.now(), "away"))

# Match 15 (ID 15): Glasgow Warriors vs Ulster
    matches[14].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[14].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[14].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[14].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[14].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[14].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[14].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[14].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[14].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[14].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[14].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[14].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[14].updateScore(Score("P", 3, datetime.now(), "home"))

# Match 16 (ID 16): Munster vs Bulls
    matches[15].updateScore(Score("PT", 7, datetime.now(), "away"))  # Integrated Penalty Try
    matches[15].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[15].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[15].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[15].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[15].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[15].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[15].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[15].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[15].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[15].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[15].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[15].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[15].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[15].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[15].updateScore(Score("P", 3, datetime.now(), "away"))

    # ==========================================
    #                 ROUND 3
    # ==========================================
     
    # Match 17 (ID 17): Dragons vs Ospreys
    matches[16].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[16].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[16].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[16].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[16].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[16].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[16].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[16].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[16].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[16].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[16].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[16].updateScore(Score("P", 3, datetime.now(), "away"))

# Match 18 (ID 18): Glasgow Warriors vs Connacht
    matches[17].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[17].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[17].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[17].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[17].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[17].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[17].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[17].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[17].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[17].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[17].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[17].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[17].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[17].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[17].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[17].updateScore(Score("P", 3, datetime.now(), "away"))

# Match 19 (ID 19): Bulls vs Lions
    matches[18].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[18].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[18].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[18].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[18].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[18].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[18].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[18].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[18].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[18].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[18].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[18].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[18].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[18].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[18].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[18].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[18].updateScore(Score("P", 3, datetime.now(), "away"))

# Match 20 (ID 20): Stormers vs Sharks
    matches[19].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[19].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[19].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[19].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[19].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[19].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[19].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[19].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[19].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[19].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[19].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[19].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[19].updateScore(Score("C", 2, datetime.now(), "away"))

# Match 21 (ID 21): Zebre Parma vs Edinburgh
    matches[20].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[20].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[20].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[20].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[20].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[20].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[20].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[20].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[20].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[20].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[20].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[20].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[20].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[20].updateScore(Score("P", 3, datetime.now(), "home"))

# Match 22 (ID 22): Scarlets vs Benetton
    matches[21].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[21].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[21].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[21].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[21].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[21].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[21].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[21].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[21].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[21].updateScore(Score("P", 3, datetime.now(), "away"))
    matches[21].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[21].updateScore(Score("P", 3, datetime.now(), "away"))

# Match 23 (ID 23): Ulster vs Munster
    matches[22].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[22].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[22].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[22].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[22].updateScore(Score("PT", 7, datetime.now(), "away")) # Integrated Penalty Try
    matches[22].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[22].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[22].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[22].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[22].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[22].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[22].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[22].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[22].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[22].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[22].updateScore(Score("P", 3, datetime.now(), "away"))

# Match 24 (ID 24): Leinster vs Cardiff
    matches[23].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[23].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[23].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[23].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[23].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[23].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[23].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[23].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[23].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[23].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[23].updateScore(Score("P", 3, datetime.now(), "home"))
    matches[23].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[23].updateScore(Score("C", 2, datetime.now(), "away"))
    matches[23].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[23].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[23].updateScore(Score("P", 3, datetime.now(), "home"))

"""
allMatches: a Dictionary of all the matches and fixtures to set up the League
"""
allMatches = [
    {"ID": "1", "Round": 1, "Home": "Benetton", "Away": "Dragons", "Date": "Fri 25 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "2", "Round": 1, "Home": "Connacht", "Away": "Stormers", "Date": "Fri 25 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "3", "Round": 1, "Home": "Ulster", "Away": "Edinburgh", "Date": "Fri 25 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "4", "Round": 1, "Home": "Lions", "Away": "Leinster", "Date": "Sat 26 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "5", "Round": 1, "Home": "Sharks", "Away": "Ospreys", "Date": "Sat 26 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "6", "Round": 1, "Home": "Zebre Parma", "Away": "Bulls", "Date": "Sat 26 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "7", "Round": 1, "Home": "Munster", "Away": "Glasgow Warriors", "Date": "Sat 26 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "8", "Round": 1, "Home": "Scarlets", "Away": "Cardiff", "Date": "Sat 26 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "9", "Round": 2, "Home": "Benetton", "Away": "Connacht", "Date": "Fri 02 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "10", "Round": 2, "Home": "Cardiff", "Away": "Zebre Parma", "Date": "Fri 02 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "11", "Round": 2, "Home": "Edinburgh", "Away": "Stormers", "Date": "Fri 02 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "12", "Round": 2, "Home": "Lions", "Away": "Ospreys", "Date": "Sat 03 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "13", "Round": 2, "Home": "Dragons", "Away": "Scarlets", "Date": "Sat 03 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "14", "Round": 2, "Home": "Sharks", "Away": "Leinster", "Date": "Sat 03 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "15", "Round": 2, "Home": "Glasgow Warriors", "Away": "Ulster", "Date": "Sat 03 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "16", "Round": 2, "Home": "Munster", "Away": "Bulls", "Date": "Sat 03 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "17", "Round": 3, "Home": "ragons", "Away": "Ospreys", "Date": "Fri 9 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "18", "Round": 3, "Home": "Glasgow Warriors", "Away": "Connacht", "Date": "Fri 9 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "19", "Round": 3, "Home": "Bulls", "Away": "Lions", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "20", "Round": 3, "Home": "Stormers", "Away": "Sharks", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "21", "Round": 3, "Home": "Zebre Parma", "Away": "Edinburgh", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "22", "Round": 3, "Home": "Scarlets", "Away": "Benetton", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "23", "Round": 3, "Home": "Ulster", "Away": "Munster", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "24", "Round": 3, "Home": "Leinster", "Away": "Cardiff", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "25", "Round": 4, "Home": "Cardiff", "Away": "Sharks", "Date": "Fri 23 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "26", "Round": 4, "Home": "Connacht", "Away": "Zebre Parma", "Date": "Fri 23 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "27", "Round": 4, "Home": "Edinburgh", "Away": "Lions", "Date": "Fri 23 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "28", "Round": 4, "Home": "Bulls", "Away": "Ulster", "Date": "Sat 24 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "29", "Round": 4, "Home": "Benetton", "Away": "Glasgow Warriors", "Date": "Sat 24 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "30", "Round": 4, "Home": "Stormers", "Away": "Scarlets", "Date": "Sat 24 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "31", "Round": 4, "Home": "Leinster", "Away": "Munster", "Date": "Sat 24 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "32", "Round": 4, "Home": "Ospreys", "Away": "Dragons", "Date": "Sat 24 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "33", "Round": 5, "Home": "Connacht", "Away": "Leinster", "Date": "Fri 30 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "34", "Round": 5, "Home": "Glasgow Warriors", "Away": "Lions", "Date": "Fri 30 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "35", "Round": 5, "Home": "Stormers", "Away": "Ulster", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "36", "Round": 5, "Home": "Benetton", "Away": "Edinburgh", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "37", "Round": 5, "Home": "Bulls", "Away": "Scarlets", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "38", "Round": 5, "Home": "Dragons", "Away": "Zebre Parma", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "39", "Round": 5, "Home": "Munster", "Away": "Sharks", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "40", "Round": 5, "Home": "Ospreys", "Away": "Cardiff", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "41", "Round": 6, "Home": "Edinburgh", "Away": "Dragons", "Date": "Fri 04 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "42", "Round": 6, "Home": "Ospreys", "Away": "Leinster", "Date": "Fri 04 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "43", "Round": 6, "Home": "Lions", "Away": "Bulls", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "44", "Round": 6, "Home": "Sharks", "Away": "Stormers", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "45", "Round": 6, "Home": "Cardiff", "Away": "Ulster", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "46", "Round": 6, "Home": "Scarlets", "Away": "Connacht", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "47", "Round": 6, "Home": "Zebre Parma", "Away": "Munster", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "48", "Round": 6, "Home": "Glasgow Warriors", "Away": "Benetton", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "49", "Round": 7, "Home": "Munster", "Away": "Scarlets", "Date": "Fri 18 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "50", "Round": 7, "Home": "Ulster", "Away": "Ospreys", "Date": "Fri 18 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "51", "Round": 7, "Home": "Stormers", "Away": "Lions", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "52", "Round": 7, "Home": "Zebre Parma", "Away": "Benetton", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "53", "Round": 7, "Home": "Cardiff", "Away": "Dragons", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "54", "Round": 7, "Home": "Sharks", "Away": "Bulls", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "55", "Round": 7, "Home": "Leinster", "Away": "Glasgow Warriors", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "56", "Round": 7, "Home": "Connacht", "Away": "Edinburgh", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "57", "Round": 8, "Home": "Dragons", "Away": "Cardiff", "Date": "Sat 26 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "58", "Round": 8, "Home": "Ospreys", "Away": "Scarlets", "Date": "Sat 26 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "59", "Round": 8, "Home": "Benetton", "Away": "Zebre Parma", "Date": "Sun 27 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "60", "Round": 8, "Home": "Edinburgh", "Away": "Glasgow Warriors", "Date": "Sun 27 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "61", "Round": 8, "Home": "Ulster", "Away": "Connacht", "Date": "Sun 27 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "62", "Round": 8, "Home": "Munster", "Away": "Leinster", "Date": "Sun 27 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "63", "Round": 8, "Home": "Lions", "Away": "Sharks", "Date": "Sat 20 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "64", "Round": 8, "Home": "Bulls", "Away": "Stormers", "Date": "Sun 21 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "65", "Round": 9, "Home": "Sharks", "Away": "Lions", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "66", "Round": 9, "Home": "Zebre Parma", "Away": "Glasgow Warriors", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "67", "Round": 9, "Home": "Scarlets", "Away": "Dragons", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "68", "Round": 9, "Home": "Connacht", "Away": "Munster", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "69", "Round": 9, "Home": "Cardiff", "Away": "Ospreys", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "70", "Round": 9, "Home": "Edinburgh", "Away": "Benetton", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "71", "Round": 9, "Home": "Leinster", "Away": "Ulster", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "72", "Round": 9, "Home": "Stormers", "Away": "Bulls", "Date": "Sun 03 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "73", "Round": 10, "Home": "Glasgow Warriors", "Away": "Scarlets", "Date": "Fri 22 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "74", "Round": 10, "Home": "Ulster", "Away": "Sharks", "Date": "Fri 22 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "75", "Round": 10, "Home": "Lions", "Away": "Zebre Parma", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "76", "Round": 10, "Home": "Stormers", "Away": "Cardiff", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "77", "Round": 10, "Home": "Ospreys", "Away": "Edinburgh", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "78", "Round": 10, "Home": "Benetton", "Away": "Bulls", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "79", "Round": 10, "Home": "Leinster", "Away": "Dragons", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "80", "Round": 10, "Home": "Munster", "Away": "Connacht", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "81", "Round": 11, "Home": "Dragons", "Away": "Munster", "Date": "Fri 29 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "82", "Round": 11, "Home": "Glasgow Warriors", "Away": "Ospreys", "Date": "Fri 29 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "83", "Round": 11, "Home": "Lions", "Away": "Cardiff", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "84", "Round": 11, "Home": "Stormers", "Away": "Zebre Parma", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "85", "Round": 11, "Home": "Scarlets", "Away": "Edinburgh", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "86", "Round": 11, "Home": "Leinster", "Away": "Bulls", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "87", "Round": 11, "Home": "Benetton", "Away": "Sharks", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "88", "Round": 11, "Home": "Connacht", "Away": "Ulster", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "89", "Round": 12, "Home": "Dragons", "Away": "Ulster", "Date": "Fri 26 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "90", "Round": 12, "Home": "Munster", "Away": "Benetton", "Date": "Fri 26 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "91", "Round": 12, "Home": "Lions", "Away": "Stormers", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "92", "Round": 12, "Home": "Bulls", "Away": "Sharks", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "93", "Round": 12, "Home": "Cardiff", "Away": "Glasgow Warriors", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "94", "Round": 12, "Home": "Zebre Parma", "Away": "Scarlets", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "95", "Round": 12, "Home": "Ospreys", "Away": "Connacht", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "96", "Round": 12, "Home": "Edinburgh", "Away": "Leinster", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "97", "Round": 13, "Home": "Sharks", "Away": "Edinburgh", "Date": "Fri 19 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "98", "Round": 13, "Home": "Connacht", "Away": "Cardiff", "Date": "Fri 19 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "99", "Round": 13, "Home": "Glasgow Warriors", "Away": "Stormers", "Date": "Fri 19 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "100", "Round": 13, "Home": "Bulls", "Away": "Dragons", "Date": "Sat 20 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "101", "Round": 13, "Home": "Ulster", "Away": "Zebre Parma", "Date": "Sat 20 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "102", "Round": 13, "Home": "Munster", "Away": "Ospreys", "Date": "Sat 20 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "103", "Round": 13, "Home": "Scarlets", "Away": "Lions", "Date": "Sat 20 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "104", "Round": 13, "Home": "Leinster", "Away": "Benetton", "Date": "Sat 20 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "105", "Round": 14, "Home": "Glasgow Warriors", "Away": "Zebre Parma", "Date": "Fri 26 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "106", "Round": 14, "Home": "Scarlets", "Away": "Leinster", "Date": "Fri 26 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "107", "Round": 14, "Home": "Bulls", "Away": "Edinburgh", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "108", "Round": 14, "Home": "Connacht", "Away": "Lions", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "109", "Round": 14, "Home": "Sharks", "Away": "Dragons", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "110", "Round": 14, "Home": "Cardiff", "Away": "Munster", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "111", "Round": 14, "Home": "Benetton", "Away": "Ulster", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "112", "Round": 14, "Home": "Ospreys", "Away": "Stormers", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "113", "Round": 15, "Home": "Dragons", "Away": "Glasgow Warriors", "Date": "Fri 16 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "114", "Round": 15, "Home": "Edinburgh", "Away": "Cardiff", "Date": "Fri 16 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "115", "Round": 15, "Home": "Lions", "Away": "Munster", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "116", "Round": 15, "Home": "Stormers", "Away": "Benetton", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "117", "Round": 15, "Home": "Ospreys", "Away": "Bulls", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "118", "Round": 15, "Home": "Leinster", "Away": "Connacht", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "119", "Round": 15, "Home": "Zebre Parma", "Away": "Sharks", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "120", "Round": 15, "Home": "Ulster", "Away": "Scarlets", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "121", "Round": 16, "Home": "Zebre Parma", "Away": "Ospreys", "Date": "Fri 23 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "122", "Round": 16, "Home": "Ulster", "Away": "Leinster", "Date": "Fri 23 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "123", "Round": 16, "Home": "Cardiff", "Away": "Bulls", "Date": "Fri 23 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "124", "Round": 16, "Home": "Lions", "Away": "Benetton", "Date": "Sat 24 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "125", "Round": 16, "Home": "Scarlets", "Away": "Sharks", "Date": "Sat 24 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "126", "Round": 16, "Home": "Stormers", "Away": "Munster", "Date": "Sat 24 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "127", "Round": 16, "Home": "Glasgow Warriors", "Away": "Edinburgh", "Date": "Sat 24 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "128", "Round": 16, "Home": "Connacht", "Away": "Dragons", "Date": "Sat 24 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "129", "Round": 17, "Home": "Dragons", "Away": "Lions", "Date": "Fri 07 May 2027 ", "Scores": [ ]} ,
    {"ID": "130", "Round": 17, "Home": "Edinburgh", "Away": "Zebre Parma", "Date": "Fri 07 May 2027 ", "Scores": [ ]} ,
    {"ID": "131", "Round": 17, "Home": "Sharks", "Away": "Connacht", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "132", "Round": 17, "Home": "Bulls", "Away": "Glasgow Warriors", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "133", "Round": 17, "Home": "Munster", "Away": "Ulster", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "134", "Round": 17, "Home": "Scarlets", "Away": "Ospreys", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "135", "Round": 17, "Home": "Benetton", "Away": "Cardiff", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "136", "Round": 17, "Home": "Leinster", "Away": "Stormers", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "137", "Round": 18, "Home": "Edinburgh", "Away": "Benetton", "Date": "Fri 14 May 2027 ", "Scores": [ ]} ,
    {"ID": "138", "Round": 18, "Home": "Ospreys", "Away": "Benetton", "Date": "Fri 14 May 2027 ", "Scores": [ ]} ,
    {"ID": "139", "Round": 18, "Home": "Ulster", "Away": "Lions", "Date": "Fri 14 May 2027 ", "Scores": [ ]} ,
    {"ID": "140", "Round": 18, "Home": "Bulls", "Away": "Connacht", "Date": "Sat 15 May 2027 ", "Scores": [ ]} ,
    {"ID": "141", "Round": 18, "Home": "Sharks", "Away": "Glasgow Warriors", "Date": "Sat 15 May 2027 ", "Scores": [ ]} ,
    {"ID": "142", "Round": 18, "Home": "Cardiff", "Away": "Scarlets", "Date": "Sat 15 May 2027 ", "Scores": [ ]} ,
    {"ID": "143", "Round": 18, "Home": "Zebre Parma", "Away": "Leinster", "Date": "Sat 15 May 2027 ", "Scores": [ ]} ,
    {"ID": "144", "Round": 18, "Home": "Dragons", "Away": "Stormers", "Date": "Sat 15 May 2027 ", "Scores": [ ]} ,
]


class WeekNo:
    """
    A Class to contain a match week or round

    Parameters:
    ----------
    startDate: str
        The Starting Date for the round (inclusive)

    endDate: str
        The Ending Date for the round (Exclusive)
        Note, the endDate for this round and start of next
        should be the same.

    round: int
        the round number (week number) for the weekNo object

    Attributes:
    ---------
    startDateString: str
        The Starting Date for the round (inclusive)

    endDateString: str
        The Ending Date for the round (Exclusive)
        Note, the endDate for this round and start of next
        should be the same.

    startDate: datetime
        the startDate parameter passed converted into a datetime object.

    endDate: datetime
        the endDate parameter passed converted into a datetime object.

    Round: int
        the round number (week number) for the weekNo object

    """
    def __init__(self, startDate, endDate, round):
        self.startDateString = startDate
        self.endDateString = endDate
        self.startDate = datetime.strptime(startDate, "%d %b %Y")
        self.endDate = datetime.strptime(endDate, "%d %b %Y")
        self.Round = round


class Calendar:
    """
    Class to represent all of the weekNo;s in the league Calendar
    ...
    
    Attributes
    ----------
    rounds: []
        A list of weekNo objects for each round.

    Methods
    ----------
    getCalendar()
        returns the list of WeekNo objects for the round.

    getRound(weekNoDateTime)
        takes a datetime object and finds the corresponding round for it.

    """
    def __init__(self):
        self.rounds = []
        self.rounds.append(WeekNo("01 Sep 2026", "02 Oct 2026", 1))
        self.rounds.append(WeekNo("02 Oct 2026", "09 Oct 2026", 2))
        self.rounds.append(WeekNo("09 Oct 2026", "23 Oct 2026", 3))
        self.rounds.append(WeekNo("23 Oct 2026", "30 Oct 2026", 4))
        self.rounds.append(WeekNo("30 Oct 2026", "04 Dec 2026", 5))
        self.rounds.append(WeekNo("04 Dec 2026", "18 Dec 2026", 6))
        self.rounds.append(WeekNo("18 Dec 2026", "26 Dec 2026", 7))
        self.rounds.append(WeekNo("26 Dec 2026", "02 Jan 2027", 8))
        self.rounds.append(WeekNo("02 Jan 2026", "22 Jan 2027", 9))
        self.rounds.append(WeekNo("22 Jan 2027", "29 Jan 2027", 10))
        self.rounds.append(WeekNo("29 Jan 2027", "26 Feb 2027", 11))
        self.rounds.append(WeekNo("26 Feb 2027", "19 Mar 2027", 12))
        self.rounds.append(WeekNo("19 Mar 2027", "26 Mar 2027", 13))
        self.rounds.append(WeekNo("26 Mar 2027", "16 Apr 2027", 14))
        self.rounds.append(WeekNo("16 Apr 2027", "23 Apr 2027", 15))
        self.rounds.append(WeekNo("23 Apr 2027", "07 May 2027", 16))
        self.rounds.append(WeekNo("07 May 2027", "14 May 2027", 17))
        self.rounds.append(WeekNo("14 May 2027", "16 May 2027", 18))

    def getCalendar(self):
        """
        returns the list of WeekNo objects for the round.
        """
        return self.rounds

    def getRound(self, weekNoDateTime):
        """
        Takes in a DateTime object and returns the relevant 
        weekNo object for that dateTime.
        ...

        Attributes
        ----------
        weekNoDateTime: datetime
            A datetime for a date you wish to find the corresponding weekNo for.

        Returns
        --------
        the weekNo object that corresponds to the selected date in weekNoDateTime

        """
        for round in self.rounds:
            if (round.startDate <= weekNoDateTime < round.endDate):
                return round

        return self.rounds[0]

    def getDates(self, weekNo):
        """
        Takes in a week/round number and returns the corresponding date
        """
        if 0 <= weekNo <= 18:
            return next(round for round in self.rounds if round.Round == weekNo)

        return self.rounds[0]
    
