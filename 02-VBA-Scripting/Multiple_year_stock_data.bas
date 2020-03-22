Attribute VB_Name = "Module1"
Option Explicit

Sub Stocks():



'Create a loop for to apply the code to all active worksheets:

    Dim ws As Worksheet
    'Set ws = Worksheets("P")  'to work in a specific sheet
    
    'Set WS_Count equal to the number of worksheets in the active workbook
    Dim ws_count As Long
    ws_count = ActiveWorkbook.Worksheets.Count
    
    Dim W As Long
    
    For W = 1 To ws_count
    
        Set ws = ActiveWorkbook.Worksheets(W)
        
        'ws.Select
                           
    'For Each ws In Worksheets 'Another way to loop trough active worksheets
    


'Define variable's data type:

    'Where the information starts in the worksheet
    Dim initial_row As Long
    initial_row = 2
    
    'Determine the last row of the active worksheet
    Dim LastRow As Long
    LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
    Dim I As Long
        
    Dim Ticker_symbol As String
        
    Dim Yearly_change As Double
            
    Dim Percentage_change As Double
        
    Dim Stock_volume As Double
    
    'Variable to know the number of rows per ticket to calculate later the opening price at the beginning of a given year
    Dim Count As Double
    Count = 0
                           
    
    
'Add columns where we will calculate the values
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Yearly Change"
    ws.Cells(1, 11).Value = "Percentage Change"
    ws.Cells(1, 12).Value = "Total Stock Volume"
      
      
      
'Change the format of the column K
    ws.Range("K:K").NumberFormat = "0.00%"



'Create a loop to search the next different ticker and print it on Ticker Column
    For I = 2 To LastRow
    'For I = 2 To 30000  'to loop with less rows
     
     
     
'Conditional to identify if the next ticker is different
'if it is then print the ticket symbol, the yearly change, percentage change and stock volume
            If ws.Cells(I + 1, 1).Value <> ws.Cells(I, 1).Value Then

                'Ticker symbol is localed in column A
                Ticker_symbol = ws.Cells(I, 1).Value
                
                'Yearly change calculation: closing price at the end of that year minus opening price at the beginning of a given year
                Yearly_change = ws.Cells(I, 6).Value - Cells(I - Count, 3).Value
 
                'conditional to avoid 'divisible by zero' error
                If ws.Cells(I - Count, 3).Value <> "0" Then
                
                Percentage_change = Yearly_change / ws.Cells(I - Count, 3).Value
                
                Else
                
                ws.Range("K" & initial_row).Value = "N/A - Opening price was zero"
                
                End If
            
                'Total stock volume of the stock
                Stock_volume = Stock_volume + ws.Cells(I, 7).Value
                


'Print values: ticker symbol, yearly change, percentage change, and stock volume
                ws.Range("I" & initial_row).Value = Ticker_symbol
        
                ws.Range("J" & initial_row).Value = Yearly_change
            
                ws.Range("K" & initial_row).Value = Percentage_change
            
                ws.Range("L" & initial_row).Value = Stock_volume
                                            
                'Add one to my initial row so it can print in the row below
                initial_row = initial_row + 1
                
                'Reset values for yearly change, count, percentage change and stock valume
                Yearly_change = 0
                
                Count = 0
            
                Percentage_change = 0

                Stock_volume = 0
            
            Else
                
                'Add one to my count to know the total rows per ticker set
                Count = Count + 1
                
                'Add to the stock volume
                Stock_volume = Stock_volume + ws.Cells(I, 7).Value
        
           
            End If

        Next I
     
    Next W
    'Next ws  'to work in a specific sheet
    
   
End Sub

