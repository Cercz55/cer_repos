#!/bin/bash

 function creator () {​​​​
 
if [[ -z "$1" ]];

 then

     echo "No ingresaste ninguna dirección. Bye"

 else

     echo $1 | cat > archivo_dir.txt

     echo "dir agregada"
 
fi

 }​​​​
 
creator "Ejemplo: Juan Escutia, 4312, Las Palmas, Monterrey, Mexico\n"
