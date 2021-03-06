#-------------------------------------------------------------------------------
# The participant manager
#-------------------------------------------------------------------------------

init 1: 
    python: 
        
        ##
        # The chat manager
        class ParticipantManager:
            
            ##
            # Constructor
            # @param (object) The chat resource manager
            def __init__(self, resourceManager):
                 
                # Create the participant manager
                #self.chatRecMan = ChatResourceManager
                self.chatRecMan = resourceManager
                self.participants = {}            # A dictionary of Roles that contains arrays of Participants
                
            ##
            # Generate a participant
            # @param role (string) The role that the participant should play
            def generateParticipant(self, role):
                # Pick a headshot
                pic = self.chatRecMan.GetRandomHeadshot(role=role)

                # Pick a name with the restrictions from the image
                name = self.chatRecMan.GetRandomName(male=pic.male, family=pic.family)
                    
                # Pick a colour
                colour = game.generateColour()
                
                # Create the participant as a character
                tmpPart = GameCharacter(name.name, pic.family, "none", Character("{image=" + pic.image + "}" + name.name, kind=nvl, window_background=Solid(colour), window_xfill=True), pic.image, True, False, "")
                
                # Add the character to all applicable role catagories
                for role in pic.roles: 
                    # Check to see if the role exists
                    if role not in self.participants:
                        self.participants[role] = []  # Create the role
                    
                    # Append!
                    self.participants[role].append(tmpPart)
                
                return tmpPart
                
            ##
            # Fetch a pre-defined participant or generate one if needed
            # @param role (string) The role the participant should play
            # @param noNew (boolean) (default=False) Controles whether we can generate a new participant or not
            def getParticipant(self, role, noNew=False): 
                
                # Check if there is even a character to pick from
                if role not in self.participants:
                    # We need to generate a character
                    return self.generateParticipant(role)
                
                if noNew == True: 
                    # Choose a random participant
                    return self.participants[role][renpy.random.randint(0, len(self.participants[role] - 1))]
                else: # Create a new character if the random number is larger than the array size- likelihood of new character creation falls off with the number of existing characters
                    # Choose a random participant index
                    index = renpy.random.randint(0, len(self.participants[role]))
                        
                    # Check if this index is off the array
                    if index <= len(self.participants[role]): 
                        return self.generateParticipant(role)
                    else: 
                        return self.participants[role][index]