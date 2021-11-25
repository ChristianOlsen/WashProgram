from datetime import timedelta

class Program:
    
    programTypes= {}
    """
    programTypes nested dictionary on form
    exampleTypes = {
        'kokvask': {
            'name': 'Kokvask',
            'temperature': 60,
            'duration': 90,
        },
        'tøyvask': {
            'name': 'Tøyvask',
            'temperature': 40,
            'duration': 60,
        },
    """
    
    def __init__(self, programType):
        if programType not in Program.programTypes:
            raise ValueError(f'{programType} is not a program.') 
        
        self.description = Program.programTypes[programType]['description']
        self.temperature = Program.programTypes[programType]['temperature']
        self.duration = Program.programTypes[programType]['duration']
    
    def addProgramType(programType, description, temperature, duration):
        newType = { 
            programType: {
                'description': description,
                'temperature': temperature,
                'duration': duration,
            },
        }
        Program.programTypes.update(newType)

    def getPrograms():
        s = ''
        pt = Program.programTypes
        for p in pt:
            s += f'{pt[p]["description"]}: {pt[p]["temperature"]} °C, {pt[p]["duration"]} minutes.\n'
        return s
        
