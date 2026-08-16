volume_celular = 100
while volume_celular >0:
    volume = input("Volume:")

    if volume == 0:
        print("Volume mudo")
    
    
    if volume == "abaixar":
        volume_celular -= 5
        
    elif volume == "aumentar":
        volume_celular += 5
    break
