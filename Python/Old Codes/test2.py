states = {
    "Andhra Pradesh": {
        "official": ["Telugu", "English"],
        "spoken": ["Urdu", "Hindi", "Banjara", "Tamil", "Kannada", "Marathi", "Oriya"]
    },
    "Karnataka": {
        "official": ["Kannada", "English"],
        "spoken": ["Urdu", "Telugu", "Tamil", "Marathi"]
    },
    "Kerala": {
        "official": ["Malayalam", "English"],
        "spoken": ["Hindi", "Kannada", "Tamil", "Tulu"]
    },
    "Tamilnadu": {
        "official": ["Tamil", "English"],
        "spoken": ["Telugu", "Kannada", "Urdu", "Malayalam", "Hindi"]
    },
    "Telangana": {
        "official": ["Telugu", "Urdu"],
        "spoken": ["Hindi", "Tamil", "Kannada", "Marathi", "Oriya"]
    }
}

def max_languages():
    max_count = 0
    max_state = ""
    
    for state, languages in states.items():
        
        total = len(languages["official"]) + len(languages["spoken"])
        
        if total > max_count:
            
            max_count = total
            max_state = state
    
    return max_state

def spoken_languages(state):
    
    if state in states:
        
        return len(states[state]["spoken"])
    else:
        
        return "Invalid state name"

def language_states(language):
    
    result = []
    
    for state, languages in states.items():
        if language in languages["spoken"] and language not in languages["official"]:
            
            result.append(state)
    
    return result

def unique_languages():
      counts = {}
    
      for state, languages in states.items():
        
          for language in languages["official"] + languages["spoken"]:
            
              counts[language] = counts.get(language, 0) + 1
   
      result = []
    
      for language, count in counts.items():
        
          if count == 1:
            
              result.append(language)
    
      return result


def menu():
    
    print("1. Which is the state that uses the maximum number of languages?")
    print("2. When a state name is given as additional input, list the number of spoken languages in that state, excluding official languages.")
    print("3. When a language name is given as input, display the state names where it is a spoken language and not an official language.")
    print("4. List the unique languages - a language used only in one of the states.")
    print("Enter your choice (1-4):")
    
    choice = input()
    
    return choice


def main():
    
    choice = menu()
   
    if choice in ["1", "2", "3", "4"]:
        
        if choice == "1":
            
            print(max_languages())
        
        elif choice == "2":
            
            state = input("Enter the state name:")
            
            print(spoken_languages(state))
       
        elif choice == "3":
           
            language = input("Enter the language name:")
            
            result = language_states(language)
           
            if result:
               
                print(" ".join(result))
            else:
                
                print("No state found with the given language")
        
        else:
            
            result = unique_languages()
            
            for language in result:
                
                print(language)
    else:
        
        print("Error")

main()

