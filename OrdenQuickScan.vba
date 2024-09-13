Sub ProcesarTodosLosCSV()
    Dim folderPath As String
    Dim fileName As String
    Dim wb As Workbook
    Dim ws As Worksheet
    Dim fso As Object
    Dim folder As Object
    Dim file As Object

    ' Ruta de la carpeta que contiene los archivos CSV
    folderPath = "E:\LPS Ingenieria Estructural\LPS Ingenieria Estructural - Ferroscan\Informes Entrega Final\CR NATURA - MADRID\Datos"

    ' Crear un objeto FileSystemObject
    Set fso = CreateObject("Scripting.FileSystemObject")
    Set folder = fso.GetFolder(folderPath)

    ' Recorrer todos los archivos en la carpeta
    For Each file In folder.Files
        If LCase(Right(file.Name, 4)) = ".csv" Then
            ' Abrir el archivo CSV
            Set wb = Workbooks.Open(file.Path)
            Set ws = wb.Sheets(1) ' Asumiendo que el CSV tiene una sola hoja

            ' Ejecutar el código en el archivo CSV
            Call OrdenarObjetos(ws)

            ' Guardar y cerrar el archivo
            wb.Close SaveChanges:=True
        End If
    Next file

    ' Limpiar objetos
    Set fso = Nothing
    Set folder = Nothing
    Set file = Nothing
End Sub

Sub OrdenarObjetos(ws As Worksheet)
    Dim lastrow As Long
    With ws
        lastrow = .Cells(.Rows.Count, "A").End(xlUp).Row
        
        .Range("L2").Value = lastrow - 3
        Dim sumRange As Range
        Dim avgValue As Double

        Set sumRange = .Range("D4:D" & lastrow)
        sumRange.Replace "mm", "", xlPart
        avgValue = WorksheetFunction.Average(sumRange)

        .Range("L3") = "Diametro Medio"
        .Range("L4") = avgValue
        
        Dim sumRangeCover As Range
        Dim avgValueCover As Double
        Set sumRangeCover = .Range("C4:C" & lastrow)
        avgValueCover = WorksheetFunction.Average(sumRangeCover)
        
        .Range("M3") = "Promedio Cover"
        .Range("M4") = avgValueCover
        
        Dim userInput As Integer
        userInput = InputBox("Please enter a value between 1 and 5:" & fileName)
        If userInput >= 1 And userInput <= 5 Then
            Dim i As Long
            Dim cel As Long
            cel = 4
            For i = 4 To lastrow
                If .Cells(i, "I").Value = userInput Then
                    .Cells(cel, "P").Value = .Cells(i, "B").Value
                    cel = cel + 1
                End If
            Next i
        Else
            MsgBox "Invalid input. Please enter a value between 1 and 5."
        End If
        cel = cel - 4
        .Range("O3") = "Numero de objetos encontrados"
        .Range("O4") = cel
        
        Dim lastCell As Range
        Dim nextColumnCell As Range
        Dim lastValue As Double

        ' Encuentra la última celda utilizada en la columna Q
        Set lastCell = Cells(Rows.Count, "P").End(xlUp)
        lastValue = CDbl(lastCell.Value)

        ' Moverse a la siguiente columna (R)
        Set nextColumnCell = lastCell.Offset(0, 1)
    
        ' Escribir la fórmula en la celda de la siguiente columna
        nextColumnCell.FormulaR1C1 = "=RC[-1]-R[-1]C[-1]"

        ' Definir el rango de destino desde la nueva celda hasta la fila 4
        Dim fillRange As Range
        Set fillRange = Range(nextColumnCell, Cells(4, nextColumnCell.Column))

        ' Rellenar automáticamente la fórmula desde la nueva celda hasta la fila 4
        nextColumnCell.AutoFill Destination:=fillRange, Type:=xlFillDefault

        ' Calcular el promedio de los valores en el rango
        Dim promedioRange As Range
        Set promedioRange = Range(nextColumnCell, Cells(4, nextColumnCell.Column))
        Dim promedio As Double
        promedio = Application.WorksheetFunction.Average(promedioRange)
        
        .Range("N3") = "Separacion promedio"
        .Range("N4") = promedio * 1000
    End With
End Sub
