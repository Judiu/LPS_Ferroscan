Sub OrdenarQuiscan()
'
' OrdenarQuiscan Macro
'
' Acceso directo: Ctrl+Mayús+Q
'
    Columns("A:A").Select
    Selection.TextToColumns Destination:=Range("A1"), DataType:=xlDelimited, _
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=True, Tab:=True, _
        Semicolon:=False, Comma:=False, Space:=True, Other:=True, OtherChar:= _
        ";", FieldInfo:=Array(Array(1, 1), Array(2, 1), Array(3, 1), Array(4, 1), Array(5, 1), _
        Array(6, 1), Array(7, 1), Array(8, 1), Array(9, 1), Array(10, 1), Array(11, 1), Array(12, 1) _
        ), TrailingMinusNumbers:=True
    Range("E4").Select
    ActiveWindow.SmallScroll Down:=0
    Range(Selection, Selection.End(xlDown)).Select
    ActiveWindow.SmallScroll Down:=-32
    Range("N4").Select
    ActiveCell.FormulaR1C1 = "Diametro"
    Range("O4").Select
    Application.CutCopyMode = False
    ActiveCell.FormulaR1C1 = "=AVERAGE(RC[-10]:R[63]C[-10])"
    Range("O5").Select
    ActiveWindow.SmallScroll Down:=-4
    Range("N5").Select
    ActiveCell.FormulaR1C1 = "Cover"
    Range("O5").Select
    Application.CutCopyMode = False
    ActiveCell.FormulaR1C1 = "=AVERAGE(R[-1]C[-11]:R[62]C[-11])"
    Range("O6").Select
    ActiveWindow.SmallScroll Down:=-4
    Range("L5").Select
    Application.CutCopyMode = False
    ActiveCell.FormulaR1C1 = "=RC[-9]-R[-1]C[-9]"
    Range("L5").Select
    Selection.AutoFill Destination:=Range("L5:L67")
    Range("L5:L67").Select
    ActiveWindow.SmallScroll Down:=0
    Range("N11").Select
End Sub
