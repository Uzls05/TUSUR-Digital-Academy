def count_protected_pawns(pawns):
    protected_pawns = 0
    for pawn in pawns:
        file = ord(pawn[0]) - 97  # Convert file letter to number (a=0, b=1,..., h=7)
        rank = int(pawn[1]) - 1  # Convert rank number to 0-based index (1=0, 2=1,..., 8=7)

        # Check if pawn is protected by another pawn
        if (file - 1 >= 0 and rank - 1 >= 0 and chr(file - 1 + 97) + str(rank) in pawns) or \
                (file + 1 < 8 and rank - 1 >= 0 and chr(file + 1 + 97) + str(rank) in pawns):
            protected_pawns += 1

    return protected_pawns


print(count_protected_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(count_protected_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))
