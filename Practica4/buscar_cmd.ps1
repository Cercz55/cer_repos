function Get-MrParameterCount {
    param (
        [string[]]$ParameterName
    )

    foreach ($Parameter in $ParameterName) {
        $Results = Get-Command -ParameterName $Parameter -ErrorAction SilentlyContinue

        [pscustomobject]@{
            ParameterName = $Parameter
            NumberOfCmdlets = $Results.Count
        }
    }
}

# busca en todos los comandos lo que pongas en argumentos
# y te muestra cuantas coincidencias hay, en este caso busca ping

Get-MrParameterCount -ParameterName ping
