Sub StockCounter()

Dim i As Long
Dim Stock_name As String                'stock name
Dim Stock_volume_total As LongLong       'stock volume total
Dim sum_table_row As Long           'var to increase summary table to next row
Dim LastRow As Long

LastRow = Sheet2.Range("A" & Rows.Count).End(xlUp).Row  'sheet 2 is 2015 data
sum_table_row = 2

'MsgBox (LastRow)
For i = 2 To LastRow


    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

    Stock_name = Cells(i, 1).Value
    Stock_volume_total = Stock_volume_total + Cells(i, 7).Value

    Range("I" & sum_table_row).Value = Stock_name

    Range("J" & sum_table_row).Value = Stock_volume_total

    sum_table_row = sum_table_row + 1

    Stock_volume_total = 0

Else

    Stock_volume_total = Stock_volume_total + Cells(i, 7).Value

End If

Next i


End Sub

