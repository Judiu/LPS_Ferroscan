Sub ProcesarTodosLosCSV()
    Dim folderPath As String
    Dim wb As Workbook
    Dim ws As Worksheet
    Dim fso As Object
    Dim folder As Object
    Dim file As Object

    ' Ruta de la carpeta que contiene los archivos CSV
    folderPath = "E:\LPS Ingenieria Estructural\LPS Ingenieria Estructural - Ferroscan\Informes Entrega Final\Colegio Ricaurte\Datos"

    ' Crear un objeto FileSystemObject
    Set fso = CreateObject("Scripting.FileSystemObject")
    Set folder = fso.GetFolder(folderPath)

    ' Desactivar actualizaciones de pantalla para mejorar el rendimiento
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

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

    ' Restaurar configuraciones de Excel
    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic

    ' Limpiar objetos
    Set fso = Nothing
    Set folder = Nothing
    Set file = Nothing
End Sub

Sub OrdenarObjetos(ws As Worksheet)
    Dim lastrow As Long
    Dim sumRange As Range, sumRangeCover As Range
    Dim avgValue As Double, avgValueCover As Double
    Dim userInput As Integer
    Dim filteredValues As Variant
    Dim cel As Long
    Dim promedio As Double

    With ws
        ' Encontrar la última fila con datos en la columna A
        lastrow = .Cells(.Rows.Count, "A").End(xlUp).Row

        ' Calcular el número de filas de datos
        .Range("L2").Value = lastrow - 3

        ' Rango de datos para cálculos
        Set sumRange = .Range("D4:D" & lastrow)
        Set sumRangeCover = .Range("C4:C" & lastrow)

        ' Limpiar y calcular promedios
        sumRange.Replace "mm", "", xlPart
        avgValue = WorksheetFunction.Average(sumRange)
        avgValueCover = WorksheetFunction.Average(sumRangeCover)

        ' Escribir resultados en las celdas
        .Range("L3").Value = "Diametro Medio"
        .Range("L4").Value = avgValue
        .Range("M3").Value = "Promedio Cover"
        .Range("M4").Value = avgValueCover

        ' Solicitar entrada del usuario
        userInput = InputBox("Please enter a value between 1 and 5:")
        If userInput >= 1 And userInput <= 5 Then
            ' Filtrar y copiar valores en una sola operación
            filteredValues = Application.Index(.Range("B4:B" & lastrow).Value, _
                                               Evaluate("ROW(1:" & lastrow - 3 & ")"), 1)
            cel = Application.WorksheetFunction.CountIf(.Range("I4:I" & lastrow), userInput)
            If cel > 0 Then
                .Range("P4").Resize(cel).Value = filteredValues
            End If
        Else
            MsgBox "Invalid input. Please enter a value between 1 and 5."
        End If

        ' Escribir el número de objetos encontrados
        .Range("O3").Value = "Numero de objetos encontrados"
        .Range("O4").Value = cel

        ' Calcular la separación promedio
        Dim diffRange As Range
        Dim lastCell As Range
        Dim nextColumnCell As Range

        ' Encuentra la última celda utilizada en la columna P
        Set lastCell = .Cells(.Rows.Count, "P").End(xlUp)

        ' Escribir fórmula en la siguiente columna
        Set nextColumnCell = lastCell.Offset(0, 1)
        nextColumnCell.FormulaR1C1 = "=RC[-1]-R[-1]C[-1]"

        ' Rellenar automáticamente la fórmula
        Set diffRange = .Range(nextColumnCell, .Cells(4, nextColumnCell.Column))
        nextColumnCell.AutoFill Destination:=diffRange, Type:=xlFillDefault

        ' Calcular el promedio de las diferencias
        promedio = WorksheetFunction.Average(diffRange)
        .Range("N3").Value = "Separacion promedio"
        .Range("N4").Value = promedio * 1000
    End With
End Sub
