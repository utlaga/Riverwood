#-------------------------------------------------------------------------------
# This shows changes to the skills
#-------------------------------------------------------------------------------
screen skillShowBox(skill, score):
    $scoreStr = 0
    $scoreStr = str(score)           # Assign the score to a string
    if score > 0:                    # Check if it is a positive number
        $scoreStr = "+" + str(score) # Append '+' if it is (+1)
    frame at easeTransform:
        text skill + " " + scoreStr     # Print the string
            
    timer 3.0 action Hide("skillShowBox")
    
screen challenegeShowBox(skill, result): 
    $resultStr = "Failed"
    if result:                          # Check if it is a positive number
        $resultStr = "Sucess"           # Append '+' if it is (+1)
    frame at easeTransform:
        text skill + ": " + resultStr    # Print the string
            
    timer 3.0 action Hide("challenegeShowBox")

transform easeTransform:
    yalign 0.1
    
    on show:
        parallel:
            alpha 0
            easein 0.5 alpha 1.0
        parallel:
            xalign 0.0
            easein 0.5 xalign .05
    on hide:
        parallel:
            easeout 0.5 alpha 0
        parallel:
            easeout 0.5 xalign 0.0