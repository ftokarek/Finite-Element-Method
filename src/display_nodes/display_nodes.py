def read_global_data(filename):
    global_data = {}
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            
            if line.startswith('*'):
                break
            
            if ' ' in line:
                parts = line.split()
                key = parts[0]
                
                if key == 'SimulationTime':
                    global_data['SimulationTime'] = float(parts[1])
                elif key == 'SimulationStepTime':
                    global_data['SimulationStepTime'] = float(parts[1])
                elif key == 'Conductivity':
                    global_data['Conductivity'] = float(parts[1])
                elif key == 'Alfa':
                    global_data['Alfa'] = float(parts[1])
                elif key == 'Tot':
                    global_data['Tot'] = float(parts[1])
                elif key == 'InitialTemp':
                    global_data['InitialTemp'] = float(parts[1])
                elif key == 'Density':
                    global_data['Density'] = float(parts[1])
                elif key == 'SpecificHeat':
                    global_data['SpecificHeat'] = float(parts[1])
                elif key == 'Nodes':
                    global_data['nN'] = int(parts[2])
                elif key == 'Elements':
                    global_data['nE'] = int(parts[2])
    
    return global_data


def read_fem_file(filename):
    nodes, elements, section = {}, {}, None
    
    with open(filename) as f:
        
        for line in f:
            line = line.strip()
            
            if line.startswith('*Node'):
                section = 'nodes'
                
            elif line.startswith('*Element'):
                section = 'elements'
                
            elif line.startswith('*'):
                section = None
                
            elif section == 'nodes':
                p = line.split(',')
                if len(p) >= 3:
                    nodes[int(p[0])] = (float(p[1]), float(p[2]))
                    
            elif section == 'elements':
                p = line.split(',')
                if len(p) >= 5:
                    elements[int(p[0])] = [int(p[i]) for i in range(1, 5)]
                    
    return nodes, elements


global_data = read_global_data('../../data/test_01/Test1_4_4.txt')
nodes, elements = read_fem_file('../../data/test_01/Test1_4_4.txt')

print("")
print("-"*50)
print("Global Data")
print("-"*50)
print(f"SimulationTime:     {global_data['SimulationTime']}") # czas symulacji
print(f"SimulationStepTime: {global_data['SimulationStepTime']}") # czas kroku 
print(f"Conductivity:       {global_data['Conductivity']}") # przewodnosc cieplna
print(f"Alfa:               {global_data['Alfa']}") # wspolczynnik wymiany ciepła
print(f"Tot:                {global_data['Tot']}") # Tot = temp otoczenia
print(f"InitialTemp:        {global_data['InitialTemp']}") # temp początkowa
print(f"Density:            {global_data['Density']}") # gestosc
print(f"SpecificHeat:       {global_data['SpecificHeat']}") # cieplo wlasciwe
print(f"nN (nodes):         {global_data['nN']}") # liczba wezlow
print(f"nE (elements):      {global_data['nE']}") # liczba elementow
print()

print("-"*50)
print("Node")
print("-"*50)
print(f"{'ID':<10} {'X':<20} {'Y':<20}")
print("-"*50)

for i in sorted(nodes):
    print(f"{i:<10} {nodes[i][0]:<20.10f} {nodes[i][1]:<20.10f}")

print("-"*50)
print(f"Total nodes: {len(nodes)}")
print()

print("-"*50)
print("Element, type = DC2D4")
print("-"*50)
print(f"{'ID':<15} {'Node IDs':<45}")
print("-"*50)

for i in sorted(elements):
    print(f"{i:<15} {elements[i]}")

print("-"*50)
print(f"Total elements: {len(elements)}")
print()

