

def draw(map):
    black = "○"
    black_promoted = "⦻"
    
    white = "●"
    white_promoted = "✪"
    h_line= '───'
    v_line= '│'
    cross='┼'
    midline = " "+(cross+h_line)*8+cross
    print("","A","B","C","D","E","F","G","H",sep="   ")
    for i,row in enumerate(map): 
        print(midline,end="")
        print()
        print(8-i,end="")
        for column in row:
            cell = " "
            if column == 4:
                cell=black_promoted
            elif column == 3:
                cell=white_promoted
            elif column == 2:
                cell=black
            elif column == 1:
                cell=white
            else:
                cell=" "
            print(f"| {cell} " , end="")
        print(v_line,8-i)
    print(midline)
    print("","A","B","C","D","E","F","G","H",sep="   ")
        